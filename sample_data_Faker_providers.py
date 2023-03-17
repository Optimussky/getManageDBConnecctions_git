# sample_data_Faker_providers.py

from faker import Faker
from faker.providers import bank, company, internet, person

fake = Faker()
fake.add_provider(bank)
fake.add_provider(company)
fake.add_provider(internet)
fake.add_provider(person)

for _ in range(5):
    #print(fake.first_name())
    #print(fake.last_name())
    print(fake.name())
    #print(fake.address())
    #print(fake.text())
    #print(f"Cuenta Clabe: {fake.bban()}")
    print(fake.company())

