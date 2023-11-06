from ex5 import client

def total_amount(client):
    total = 0
    for x in client:
        total += x['montant']
    return total

print("Total dépensé par les clients : ", total_amount(client))