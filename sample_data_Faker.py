# sample_data_Faker.py

#pip install Faker

import pprint
from faker import Faker
fake = Faker()

fake.name()
fake.address()
fake.company()
fake.text()


print("""
        Print fake data using: name(), street_address(), job(), company()\n""")
for _ in range(5):
    print('Name: ', fake.name())
    print('Address: ', fake.street_address())
    print('Job: ', fake.job())
    print('Company: ', fake.company())
    print()

print("""
    Print fake data using: profile()\n""")

for _ in range(3):
    pprint.pprint(fake.profile())
    print()

