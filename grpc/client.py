import grpc
from person_pb2 import PersonRequest
from person_pb2_grpc import PersonServiceStub

channel = grpc.insecure_channel('localhost:50051')
stub = PersonServiceStub(channel)

response = stub.GetPerson(PersonRequest(id=1))
print(response.person)
