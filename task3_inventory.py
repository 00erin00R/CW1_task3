import json

with open('inventory.json', 'r') as file:
    loaded_inventory = json.load(file)

print(loaded_inventory)