
from concurrent import futures

import grpc
from basic_pb2 import SumRequest, SumReply
from basic_pb2_grpc import SimpleActionsServicer
from basic_pb2_grpc import add_SimpleActionsServicer_to_server


class NumbersAdder(SimpleActionsServicer):
    def AddNumbers(self, request: SumRequest, context):
        res = request.a + request.b
        return SumReply(c=res)


def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    add_SimpleActionsServicer_to_server(NumbersAdder(), server)
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    print(f'Server started, listening on {port}')
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
