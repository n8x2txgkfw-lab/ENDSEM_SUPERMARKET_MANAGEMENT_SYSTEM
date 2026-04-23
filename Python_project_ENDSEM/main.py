import sys
import os
from datetime import datetime

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from inventory import display_stock, stock
from billing import process_purchase, total_revenue
from analysis import low_stock_alert, sales_report


def show_datetime():
    now = datetime.now()
    print(now.strftime("\n%d-%m-%Y | %H:%M:%S"))


def main():
    while True:
        show_datetime()  # real-time date & time

        print("\n========== Supermarket System ==========")
        print("Welcome to SuperMart!")
        print("1. View Stock")
        print("2. Purchase Items")
        print("3. Low Stock Alert")
        print("4. Exit")
        print("5. View Total Revenue")
        print("6. Sales Report")

        choice = input("Enter choice: ")

        if choice == "1":
            display_stock()

        elif choice == "2":
            display_stock()

            cart = {}
            n = int(input("How many items? "))

            for _ in range(n):
                item = input("Enter item name: ").lower()

                if item not in stock:
                    print("Invalid item! Try again.")
                    continue

                qty = int(input("Enter quantity: "))
                cart[item] = qty

            total = process_purchase(cart)
            print("Total Bill:", total)

        elif choice == "3":
            print("Low Stock Items:", low_stock_alert())

        elif choice == "4":
            print("Exiting...")
            break

        elif choice == "5":
            print("Total Revenue:", total_revenue)

        elif choice == "6":
            sales_report()

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()