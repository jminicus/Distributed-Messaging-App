# CLIENT SIDE OF GRPC APPLICATION
from __future__ import print_function
import sys

import grpc
import app_pb2
import app_pb2_grpc


# logs in existing user
def login(stub):
    while True:
        username = input("Enter your username to log in: ")
        login_request = app_pb2.Account(username=username)
        login_response = stub.LogIn(login_request)

        print(login_response.message + "\n")
        if login_response.success:
            return username


# adds new account to server if username is unique
def create_account(stub):
    while True:
        username = input("Enter your desired username to create an account: ")
        create_account_request = app_pb2.Account(username=username)
        create_account_response = stub.CreateAccount(create_account_request)
        print(create_account_response.message + "\n")
        if create_account_response.success:
            return username


# when user first opens client or when user is logged out, handle login or account creation
def set_username(stub):
    while True:
        has_account = input("Do you have an account already? (y/n): ")

        if has_account == "y" or has_account == "Y":
            username = login(stub)
            return username

        if has_account == "n" or has_account == "N":
            username = create_account(stub)
            return username


# continuously print new messages to terminal (and all undelivered messages upon login)
def get_messages(stub, username):
    get_messages_request = app_pb2.Account(username=username)
    get_messages_response = stub.GetMessage(get_messages_request)

    for message in get_messages_response:
        print("<" + message.sender + ">: " + message.text)

    print("No more new messages to display.\n")

        
# send message by specifying a recipient and text to send
def send_message(stub, sender):
    while True:
        recipient = input("Desired recipient: ")
        text = input("Message to send: ")
        send_messages_request = app_pb2.Message(
            sender=sender,
            recipient=recipient,
            text=text
        )
        send_messages_response = stub.SendMessage(send_messages_request)

        print(send_messages_response.message + "\n")
        return


# lists all accounts currently on server by text wildcard
def list_accounts(stub):
    text = input("Search for subset (blank input will show all accounts): ")
    list_accounts_request = app_pb2.UserSearch(text=text)
    list_accounts_response = stub.ListAccounts(list_accounts_request)

    for account in list_accounts_response:
        print(account.username)

    print("No more accounts to display.\n")


# deletes current account currently logged in and empties unread messages to
# terminal before doing so
def delete_account(stub, username):
    print("Displaying unread messages before deleting...\n")
    get_messages(stub, username)
    delete_account_request = app_pb2.Account(username=username)
    delete_account_response = stub.DeleteAccount(delete_account_request)
    print(delete_account_response.message)


# logs out current user
def log_out(stub, username):
    log_out_request = app_pb2.Account(username=username)
    log_out_response = stub.LogOut(log_out_request)
    print(log_out_response.message)


# runs main control flow
def run(server_addr):
    with grpc.insecure_channel(server_addr + ":6000") as channel:
        stub = app_pb2_grpc.AppStub(channel)
        print("Welcome to the messaging center.\n")
        # maintain username to essentially "sign in" the client to a username
        username = set_username(stub)
        # keep track of whether the user deletes the account or not so we don't
        # try to log out ot deleted account
        deleted = False

        try:
            # continuously ask for action denoted by user key stroke
            while True:
                print("l = List accounts")
                print("s = Send message")
                print("g = Get messages")
                print("d = Delete account")
                print("e = Exit")
                action = input("Action: ")

                if action.lower() == 'l':
                    list_accounts(stub)
                
                if action.lower() == 's':
                    send_message(stub, username)

                if action.lower() == 'g':
                    get_messages(stub, username)

                if action.lower() == 'd':
                    delete_account(stub, username)
                    deleted = True
                    break

                if action.lower() == 'e':
                    break
        
        # executes a log out when the user exits in correctly (pressing "e") or exits
        # incorrectly by just cancelling the terminal. Ensures that one (and only one)
        # terminal can always access the account. Also does not attempt to log out of the
        # account if user has just deleted it with "d" command
        finally:
            if not deleted:
                log_out(stub, username)


# take in server address as argument to run command, specified by user.
# When server is ran, it will display to the server terminal which IP address
# to specify when running the client
if __name__ == "__main__":
    server_addr = sys.argv[1]
    if not server_addr:
        print("Please try again and enter the server IP address as an argument.")
    else:
        run(server_addr)