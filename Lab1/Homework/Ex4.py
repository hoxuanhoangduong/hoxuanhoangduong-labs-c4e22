from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)
db = client.get_default_database()

customers = db['customers']

customers_list = customers.find()

from collections import Counter
customer_ref = []

for p in customers_list:
    customer_ref.append(p["ref"])

customer_groups = Counter(customer_ref)

import matplotlib.pyplot as plt

sizes = customer_groups.values()

groups = customer_groups.keys()

plt.pie(sizes, labels=groups, autopct='%1.1f%%',startangle=90, shadow=True, explode=[0, 0.2, 0.1, 0])
plt.axis('equal')
plt.title('Number of customers by groups of reference')
plt.show()