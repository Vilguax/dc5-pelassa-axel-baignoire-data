from ex5 import client

for x in client:
    if x['montant'] > 100:
        print(x['nom'], x['email'], x['montant'])