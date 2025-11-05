# Initial inventory with some items and their stock counts
inventory = {"laptop": 10, "mouse": 25, "keyboard": 15}

print("Initial Inventory:")
print(inventory)
print("-" * 20)
# Add a new item "monitor" with a stock of 5
inventory["monitor"] = 5

print("Inventory after adding 'monitor':")
print(inventory)
print("-" * 20)
# Update the stock of "laptop" to 2
inventory["laptop"] = 2

print("Inventory after updating 'laptop' stock:")
print(inventory)
print("-" * 20)

# Check the stock count for "keyboard"
item_to_check = "keyboard"
stock = inventory.get(item_to_check)

if stock is not None and stock > 0:
    print(f"'{item_to_check}' is in stock with a count of {stock}.")
elif stock is not None and stock == 0:
    print(f"'{item_to_check}' is out of stock.")
else:
    print(f"'{item_to_check}' is not found in the inventory.")

# Check for an item that is not in the inventory
item_to_check = "camera"
stock = inventory.get(item_to_check)

if stock is not None and stock > 0:
    print(f"'{item_to_check}' is in stock with a count of {stock}.")
else:
    print(f"'{item_to_check}' is not found in the inventory.")
print("-" * 20)

# Print the final, updated inventory
print("Final Inventory:")
for item, stock in inventory.items():
    print(f"{item}: {stock}")
