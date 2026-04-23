from inventory import stock

# ✅ MUST BE OUTSIDE FUNCTION
total_revenue = 0
sales_data = []

def process_purchase(cart):
    global total_revenue
    total = 0

    for item, qty in cart.items():
        if item in stock:
            price = stock[item][0]

            if stock[item][1] >= qty:
                total += price * qty
                stock[item][1] -= qty

                # 🔥 ADD THIS LINE
                sales_data.append({"item": item, "quantity": qty, "revenue": price * qty})

            else:
                print(f"Not enough stock for {item}")
        else:
            print(f"{item} not found")

    total_revenue += total
    return total