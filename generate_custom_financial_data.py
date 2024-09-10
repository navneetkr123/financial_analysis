import csv
import random
from datetime import date

def generate_csv(n):
    """
    Generates a CSV file with random revenue, expenses, profit, month, and day, ensuring the following constraints:
    - Months and days are in order.
    - Revenue is always greater than profit.
    - Revenue - expenses = profit.

    Args:
        n: The number of rows to generate.
    """

    filename = "financial_data.csv"

    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['revenue', 'expenses', 'profit', 'year', 'month', 'day', 'company', 'date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        # Start with a random date
        current_date = date.today()

        for _ in range(n):
            # Generate random revenue and expenses
            revenue = random.randint(1000, 10000)
            expenses = random.randint(500, 10000)  # Allow expenses to be greater than revenue
            profit = revenue - expenses

            # Write the data to the CSV
            writer.writerow({
                'revenue': revenue,
                'expenses': expenses,
                'profit': profit,
                'year': current_date.year - 29,
                'month': current_date.month,
                'day': current_date.day,
                'company': "xyz",
                'date': current_date
            })

            # Increment the date for the next row
            current_date += date.resolution

    print(f"CSV file '{filename}' generated successfully.")

# Example usage:
n = 10000  # Generate 100 rows
generate_csv(n)