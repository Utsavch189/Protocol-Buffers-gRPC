import grpc
from person_pb2 import PersonRequest
from person_pb2_grpc import PersonServiceStub

with grpc.insecure_channel('localhost:50051') as channel:
        stub = PersonServiceStub(channel)
        # Call the remote method
        response = stub.GetPerson(PersonRequest(id=1))
        print(response.person)

"""
Remote Method Invocation:
    The client calls stub.GetPerson() as though it is a local method, but it is executed on the server. 
    The gRPC framework handles serialization, network transport, and deserialization.

Distributed Application:
    The server and client can run on different machines. 
    The client doesn't need to know the server's internal implementation, 
    only the service definition (person.proto).

Simplified Workflow:
    The client simply uses the PersonServiceStub object to invoke methods, 
    without worrying about how the communication happens.

This abstraction demonstrates how gRPC simplifies distributed application development.
"""