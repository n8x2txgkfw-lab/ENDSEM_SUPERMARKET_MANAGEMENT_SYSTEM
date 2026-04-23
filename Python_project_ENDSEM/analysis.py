import pandas as pd
import os
from billing import sales_data
from inventory import stock


def low_stock_alert():
    low_items = []

    for item, details in stock.items():
        if details[1] < 5:
            low_items.append(item)

    return low_items


def sales_report():
    if not sales_data:
        print("No sales yet")
        return

    df = pd.DataFrame(sales_data)

    print("\n--- Sales Data ---")
    print(df)

    print("\n--- Total Sales by Item ---")
    print(df.groupby("item")["quantity"].sum())

    print("\n--- Revenue by Item ---")
    print(df.groupby("item")["revenue"].sum())

    # DEBUG + SAVE CSV
    print("\nCurrent Working Directory:", os.getcwd())

    file_path = os.path.join(os.getcwd(), "sales_report.csv")
    print("Saving to:", file_path)

    df.to_csv(file_path, index=False)

    print("File saved successfully!")