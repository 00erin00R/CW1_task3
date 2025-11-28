import json

def load_inventory(file):
    try:
        with open('inventory.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: 'inventory.json' file not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from 'inventory.json'.")
        return []
    
def generate_report(data):
    total_items = sum(item.get("stock", 0) for item in data)
    highest_price = max(data, key=lambda item: item.get("price",0))
    out_stock = [item for item in data if item.get("stock", 0)== 0]

    return total_items, highest_price, out_stock

def restock_item(data, product_id, amount):
    for item in data:
        if item.get("id")==product_id:
            item["stock"] += amount
            print(f"Restocked {item['name']}. New stock: {item['stock']}")
            return
    
    print(f"Error: Product with ID {product_id}not found.")

def save_inventory(filename, data):
    with open("updated_inventory.json","w") as f:
        json.dump(data, f, indent=1)

inventory = load_inventory('inventory.json')

if not inventory:
    print("Inventory is empty or failed to load.")
    exit()

total_items, highest_price, out_stock = generate_report(inventory)

print("Your total stock is: ", total_items)
print("Your highest priced item is: ", highest_price.get("name"), "at £", highest_price.get("price"))
print("The items out of stock are: ")

if out_stock:
    for item in out_stock:
        print("-", item.get("name"))
else:
    print("None")

try:
    user_id = int(input("Enter the product ID to be restocked: "))
    amount = int(input("Enter amount to restock: "))
except ValueError:
    print("Invalid ID. Must be a number.")
    exit()

restock_item(inventory, user_id, amount)
save_inventory("invntory.json",inventory)