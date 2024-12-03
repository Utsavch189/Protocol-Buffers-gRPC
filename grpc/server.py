import grpc
from concurrent import futures
import asyncio
from grpc.aio import server
from person_pb2 import Person, PersonResponse
from person_pb2_grpc import PersonServiceServicer, add_PersonServiceServicer_to_server

class PersonService(PersonServiceServicer):
    def GetPerson(self, request, context):
        person = Person(id=request.id, name="Alice", email="alice@example.com")
        print(f"REQUEST ====> {request}")
        return PersonResponse(person=person)

# server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
# add_PersonServiceServicer_to_server(PersonService(), server)
# server.add_insecure_port('[::]:50051')
# server.start()
# server.wait_for_termination()

async def serve():
    _server = server()
    add_PersonServiceServicer_to_server(PersonService(), _server)
    _server.add_insecure_port('[::]:50051')
    await _server.start()
    await _server.wait_for_termination()

if __name__=="__main__":
    asyncio.run(serve())
