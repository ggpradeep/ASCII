items = ["Pencil", "Eraser", "Notebook", "Sharpener", "Binder"]
stock_counts = [3, 2, 6, 4, 9]
inventory = {item: count for item, count in zip(items, stock_counts)}
print("Full inventory:", inventory)
in_stock_items = [item for item in items if inventory[item] > 0]
print("In stock items:", in_stock_items)
chosen_item = input("Which item do you want to buy?")
if chosen_item not in inventory or inventory[chosen_item] == 0:
    print(chosen_item, "is out of stock")
    exit()
prices = [7, 10, 15, 4, 20]
markup = int(input("Enter the markup ammount to add every price."))
marked_up_prices = list(map(lambda p: p + markup, prices))
print("Final price:", marked_up_prices)