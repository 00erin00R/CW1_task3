# import the json file so the programme can read, write and work with json file
import json

#function to load the inventory.json file
def load_inventory(file):
    try:
        with open('inventory.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError: # if not found the programme returns an error message
        print("Error: 'inventory.json' file not found.")
        return []
    except json.JSONDecodeError: # if the json file is brocken programme returns a different error
        print("Error: Failed to decode JSON from 'inventory.json'.")
        return []

#function to generate a reort based on contents of the json file   
def generate_report(data):
    total_items = sum(item.get("stock", 0) for item in data) # finds the total amount of items in stock using sum
    # finds the highest priced item from the file and creates a small anonymous function to look through the dictionary
    highest_price = max(data, key=lambda item: item.get("price",0)) 
    out_stock = [item for item in data if item.get("stock", 0)== 0] # searches dictionary for any items that are out of stock

    # returns data found
    return total_items, highest_price, out_stock

# function to restock items with given product id
def restock_item(data, product_id, amount):
    for item in data: # goes through items in the dictionary
        if item.get("id")==product_id: # if user input matches an id in the json file
            item["stock"] += amount # add users inputted stock amount
            print(f"Restocked {item['name']}. New stock: {item['stock']}") # print new stock levels
            return
    
    print(f"Error: Product with ID {product_id}not found.") # prints error if id not found

# function to save new retocked inventory list
def save_inventory(filename, data):
    with open("updated_inventory.json","w") as f: # makes new json file that can have data written to it
        json.dump(data, f, indent=1)

# checks if the file is being run directly by the user, or is it being imported to another file
# if false the code does not run 
if __name__ == "__main__":
    inventory = load_inventory('inventory.json') # loads the json file stored as the varial inventory

    # if file doesnt exist or empty error is displayed
    if not inventory:
        print("Inventory is empty or failed to load.")
        exit()

    # generates the report using the function generate report on inventory
    total_items, highest_price, out_stock = generate_report(inventory)

    print("Your total stock is: ", total_items) # prints total amount of items
    print("Your highest priced item is: ", highest_price.get("name"), "at £", highest_price.get("price")) # displays name and price of the most expensive item
    print("The items out of stock are: ") # prints what items are out of stock

    # gets the name of item if it is out of stock 
    if out_stock:
        for item in out_stock:
            print("-", item.get("name"))
    else:
        print("None")

    try:
        user_id = int(input("Enter the product ID to be restocked: ")) # asks user to input product id
        amount = int(input("Enter amount to restock: ")) # asks user to input amount that they want to increase the stock by
    except ValueError:
        print("Invalid ID. Must be a number.") # if input isnt a number error message is displayed
        exit()

    # calls the functions restock item and save inventory 
    restock_item(inventory, user_id, amount)
    save_inventory("invntory.json",inventory)