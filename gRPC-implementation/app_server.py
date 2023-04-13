# SERVER SIDE OF GRPC APPLICATION
import logging
import sqlite3
from concurrent import futures
import socket

import grpc
import app_pb2
import app_pb2_grpc

class AppServicer(app_pb2_grpc.AppServicer):

    # creates an account if it does not already exist. Since client side will automatically
    # log in after account creation, set the log-in indicator to true
    def CreateAccount(self, request, context):
        cur.execute("SELECT COUNT(*) FROM users WHERE username = ?",(request.username,))
        account_exists = cur.fetchone()[0] == 0
        if account_exists:
            cur.execute('INSERT INTO users (username, logged_in) VALUES (?, 1)',(request.username,))
            con.commit()
            return app_pb2.SuccessResponse(
                success=True, 
                message="Account successfully created!"
            )
        else:
            return app_pb2.SuccessResponse(
                success=False,
                message="Sorry, that username is taken already."
            )
    

    # will log in successfully if the account exists and if no other client is currently logged
    # into the account, done by checking the account dict for username key and log-in indicator
    def LogIn(self, request, context):
        cur.execute("SELECT COUNT(*) FROM users WHERE username = ?",(request.username,))
        account_exists = cur.fetchone()[0] != 0

        if not account_exists:
            return app_pb2.SuccessResponse(
                success=False,
                message="There was an issue logging in -- please make sure this account exists."
            )

        cur.execute("SELECT logged_in FROM users WHERE username = ?",(request.username,))
        logged_in = cur.fetchone()[0]

        if not logged_in:
            cur.execute("UPDATE users SET logged_in = 1 WHERE username = ?",(request.username,))
            con.commit()
            return app_pb2.SuccessResponse(
                success=True,
                message="You are logged in!"
            )
        else:
            return app_pb2.SuccessResponse(
                success=False,
                message="There was an issue logging in -- please make sure this account is logged out of other clients."
            )


    # returns list of accounts which contain the wildcard text supplied by the client
    def ListAccounts(self, request, context):
        cur.execute("SELECT username FROM users")
        rows = cur.fetchall()
        accounts = [row[0] for row in rows]

        for account in accounts:
            if request.text in account:
                yield app_pb2.Account(username=account)


    # "sends" message to another user by adding it to their message queue. Also verifies
    # that the recipient exists before doing so
    def SendMessage(self, request, context):
        cur.execute("SELECT COUNT(*) FROM users WHERE username = ?",(request.recipient,))
        recipient_exists = cur.fetchone()[0] != 0

        if recipient_exists:
            cur.execute('INSERT INTO messages (recipient, sender, text) VALUES (?, ?, ?)',(
                request.recipient,
                request.sender,
                request.text,
                ))
            con.commit()
            return app_pb2.SuccessResponse(
                success=True,
                message="Message sent!"
            )
        else:
            return app_pb2.SuccessResponse(
                success=False,
                message="There was an issue sending the message -- please make sure this account exists."
            )


    # empties all messages in a specified account's queue to the client side along with
    # relevant metadata
    def GetMessage(self, request, context):
        cur.execute('SELECT * FROM messages WHERE recipient = ?',(request.username,))
        messages = cur.fetchall()
        cur.execute('DELETE FROM messages WHERE recipient = ?',(request.username,))
        con.commit()

        for message in messages:
            yield app_pb2.Message(
                sender=message[1],
                recipient=message[0],
                text=message[2]
            )


    # logs out user by setting the account's indicator variable to false
    def LogOut(self, request, context):
        cur.execute("UPDATE users SET logged_in = 0 WHERE username = ?",(request.username,))
        con.commit()
        return app_pb2.SuccessResponse(
            success=True,
            message="You have been logged out."
        )


    # deletes account by simply deleting account's key in dictionary
    def DeleteAccount(self, request, context):
        cur.execute("DELETE FROM users WHERE username = ?",(request.username,))
        con.commit()
        return app_pb2.SuccessResponse(
            success=True,
            message="Account deleted. Goodbye!"
        )
    

# run server with 10 threads to handle multiple clients
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    app_pb2_grpc.add_AppServicer_to_server(AppServicer(), server)

    # get ip address of current server and make sure server listens on port 6000
    ip_address = socket.gethostbyname(socket.gethostname())
    print("When running your client, specify " + ip_address + " as an argument to the terminal.")
    server.add_insecure_port(ip_address + ':6000')

    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    # setup conneciton to database
    con = sqlite3.connect("store.db", check_same_thread=False)
    cur = con.cursor()

    logging.basicConfig()
    serve()

    # close cursor and database connection
    cur.close()
    con.close()