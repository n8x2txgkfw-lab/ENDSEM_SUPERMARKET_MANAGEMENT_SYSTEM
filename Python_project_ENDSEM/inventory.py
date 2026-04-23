stock = {
    "rice": [50, 20],
    "oil": [120, 15],
    "sugar": [40, 10],
    "toothpaste": [30, 5],
    "soap": [25, 8],
    "shampoo": [60, 12],
    "biscuits": [20, 25],
    "chocolate": [10, 30],
    "bread": [15, 18],
    "milk": [25, 22],
    "eggs": [5, 50],
    "cheese": [80, 7],
    "butter": [70, 9],
    "yogurt": [35, 14],
    "juice": [45, 11],
    "cereal": [55, 13],
    "pasta": [65, 6],
    "sauce": [75, 4],
    
}

def display_stock():
    print("\n--- Current Stock ---")
    for item, details in stock.items():
        print(f"{item} -> Price: {details[0]}, Quantity: {details[1]}")