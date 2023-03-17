# sample_data_Faker_in_Pandas.py

# pip install Faker
# pip install pandas

import pandas as pd
from faker import Faker

fake = Faker()

print("""
        Using fake.profile() on DataFrame())""")

df = pd.DataFrame([fake.profile() for _ in range(10)])
print(df)

