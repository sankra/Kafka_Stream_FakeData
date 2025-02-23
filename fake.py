#importing Faker module from faker
from faker import Faker
fake = Faker()

message= {
        'name':fake.name(),
        'address':fake.address(),
        'phone':fake.phone_number()
        }
print(message)
