# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import app_pb2 as app__pb2


class AppStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateAccount = channel.unary_unary(
                '/app.App/CreateAccount',
                request_serializer=app__pb2.Account.SerializeToString,
                response_deserializer=app__pb2.SuccessResponse.FromString,
                )
        self.LogIn = channel.unary_unary(
                '/app.App/LogIn',
                request_serializer=app__pb2.Account.SerializeToString,
                response_deserializer=app__pb2.SuccessResponse.FromString,
                )
        self.LogOut = channel.unary_unary(
                '/app.App/LogOut',
                request_serializer=app__pb2.Account.SerializeToString,
                response_deserializer=app__pb2.SuccessResponse.FromString,
                )
        self.ListAccounts = channel.unary_stream(
                '/app.App/ListAccounts',
                request_serializer=app__pb2.UserSearch.SerializeToString,
                response_deserializer=app__pb2.Account.FromString,
                )
        self.SendMessage = channel.unary_unary(
                '/app.App/SendMessage',
                request_serializer=app__pb2.Message.SerializeToString,
                response_deserializer=app__pb2.SuccessResponse.FromString,
                )
        self.GetMessage = channel.unary_stream(
                '/app.App/GetMessage',
                request_serializer=app__pb2.Account.SerializeToString,
                response_deserializer=app__pb2.Message.FromString,
                )
        self.DeleteAccount = channel.unary_unary(
                '/app.App/DeleteAccount',
                request_serializer=app__pb2.Account.SerializeToString,
                response_deserializer=app__pb2.SuccessResponse.FromString,
                )


class AppServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateAccount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LogIn(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LogOut(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListAccounts(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteAccount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AppServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateAccount,
                    request_deserializer=app__pb2.Account.FromString,
                    response_serializer=app__pb2.SuccessResponse.SerializeToString,
            ),
            'LogIn': grpc.unary_unary_rpc_method_handler(
                    servicer.LogIn,
                    request_deserializer=app__pb2.Account.FromString,
                    response_serializer=app__pb2.SuccessResponse.SerializeToString,
            ),
            'LogOut': grpc.unary_unary_rpc_method_handler(
                    servicer.LogOut,
                    request_deserializer=app__pb2.Account.FromString,
                    response_serializer=app__pb2.SuccessResponse.SerializeToString,
            ),
            'ListAccounts': grpc.unary_stream_rpc_method_handler(
                    servicer.ListAccounts,
                    request_deserializer=app__pb2.UserSearch.FromString,
                    response_serializer=app__pb2.Account.SerializeToString,
            ),
            'SendMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.SendMessage,
                    request_deserializer=app__pb2.Message.FromString,
                    response_serializer=app__pb2.SuccessResponse.SerializeToString,
            ),
            'GetMessage': grpc.unary_stream_rpc_method_handler(
                    servicer.GetMessage,
                    request_deserializer=app__pb2.Account.FromString,
                    response_serializer=app__pb2.Message.SerializeToString,
            ),
            'DeleteAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteAccount,
                    request_deserializer=app__pb2.Account.FromString,
                    response_serializer=app__pb2.SuccessResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'app.App', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class App(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateAccount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/app.App/CreateAccount',
            app__pb2.Account.SerializeToString,
            app__pb2.SuccessResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LogIn(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/app.App/LogIn',
            app__pb2.Account.SerializeToString,
            app__pb2.SuccessResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LogOut(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/app.App/LogOut',
            app__pb2.Account.SerializeToString,
            app__pb2.SuccessResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListAccounts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/app.App/ListAccounts',
            app__pb2.UserSearch.SerializeToString,
            app__pb2.Account.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/app.App/SendMessage',
            app__pb2.Message.SerializeToString,
            app__pb2.SuccessResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/app.App/GetMessage',
            app__pb2.Account.SerializeToString,
            app__pb2.Message.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteAccount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/app.App/DeleteAccount',
            app__pb2.Account.SerializeToString,
            app__pb2.SuccessResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)