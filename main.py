from person_pb2 import Person

# Create a new Person object
person = Person(id=1, name="Alice", email="alice@example.com")

# Serialize to binary format
serialized_data = person.SerializeToString()
print(f"Serialized Data: {serialized_data}")

# Deserialize back into a Person object
new_person = Person()
new_person.ParseFromString(serialized_data)
print(f"Deserialized Data: {new_person}")

"""
Optional Fields:
Protobuf allows you to omit fields during serialization.
"""

person1 = Person(id=1, name="Bob") # Omits unset fields
serialized_data1 = person1.SerializeToString()
print(f"Serialized Data [person1] : {serialized_data1}")
new_person1 = Person()
new_person1.ParseFromString(serialized_data1)
print(f"Deserialized Data: {new_person1}")

"""
Nested Messages:
You can define a message inside another message.
"""

from company_pb2 import Company

company = Company(name="TechCorp")
employee1 = company.employees.add(id=1, name="Alice")
employee2 = company.employees.add(id=2, name="Bob")

# Serialize to binary format
serialized_data = company.SerializeToString()
print(f"Serialized Company Data: {serialized_data}")

# Deserialize back into a Person object
new_company = Company()
new_company.ParseFromString(serialized_data)
print(f"Deserialized Company Data: {new_company}")

"""
Repeated Fields:
Use repeated to create lists.
"""

from test_pb2 import Numbers

nums = Numbers(values=[1, 2, 3, 4])
print(nums)

# Serialize to binary format
serialized_data = nums.SerializeToString()
print(f"Serialized nums Data: {serialized_data}")

# Deserialize back into a Person object
new_nums = Numbers()
new_nums.ParseFromString(serialized_data)
print(f"Deserialized nums Data: {new_nums}")

# Oneof or Mutually Exclusive fields

from test_pb2 import Person2

# Create a Person object
person = Person2()

# Set the name and id fields
person.name = "Alice"
person.id = 123

# Set the email field in the oneof group
person.email = "alice@example.com"
print(person)  # Prints: name: "Alice" id: 123 email: "alice@example.com"

# Set the phone field in the oneof group
person.phone = "123-456-7890"
print(person)  # Prints: name: "Alice" id: 123 phone: "123-456-7890"

# Notice that email is cleared because phone was set
print(person.HasField("email"))  # False
print(person.HasField("phone"))  # True

"""
Key Points:

Only one field in the oneof group can be set at a time.

Setting a field automatically clears the other fields in the oneof group.

You can check which field is currently set using WhichOneof
"""

print(person.WhichOneof("contact"))  # Outputs: "phone"

"""
Validation Use Case:
oneof ensures that only one of the mutually exclusive options is provided. For example:

A Person can be contacted via email or phone, but not both at the same time.
It avoids mistakes like sending both options or leaving both blank unintentionally.
"""