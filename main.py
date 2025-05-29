import json
import csv
from datetime import datetime

FILENAME = "transactions.json"

# Load transactions from JSON file
def load_data():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save transactions to JSON file
def save_data(data):
    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4)

# Add a new transaction
def add_transaction(transactions):
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    t_type = input("Type (income/expense): ").strip().lower()
    if t_type not in ["income", "expense"]:
        print("Invalid type. Please enter 'income' or 'expense'.")
        return

    description = input("Description: ").strip()
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    transaction = {
        "amount": amount,
        "type": t_type,
        "description": description,
        "date": date
    }
    transactions.append(transaction)
    save_data(transactions)
    print("✅ Transaction added!")

# Display all transactions
def view_transactions(transactions):
    if not transactions:
        print("No transactions found.")
        return

    print("\n📋 Your Transactions:")
    for t in transactions:
        print(f"[{t['date']}] {t['type'].capitalize()} - ₹{t['amount']} | {t['description']}")
    print()

# Display balance summary
def view_balance(transactions):
    income = sum(t["amount"] for t in transactions if t["type"] == "income")
    expense = sum(t["amount"] for t in transactions if t["type"] == "expense")
    balance = income - expense

    print("\n📈 Balance Summary:")
    print(f"Total Income: ₹{income}")
    print(f"Total Expense: ₹{expense}")
    print(f"Current Balance: ₹{balance}\n")

# Export transactions to CSV
def export_to_csv(transactions):
    if not transactions:
        print("No transactions to export.")
        return

    try:
        with open("transactions.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["date", "type", "amount", "description"])
            writer.writeheader()
            writer.writerows(transactions)
        print("✅ Transactions exported to 'transactions.csv'")
    except Exception as e:
        print(f"Error exporting to CSV: {e}")

# Main menu
def main():
    transactions = load_data()

    while True:
        print("\n📊 Expense Tracker Menu:")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. View Balance")
        print("4. Export to CSV")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_transaction(transactions)
        elif choice == "2":
            view_transactions(transactions)
        elif choice == "3":
            view_balance(transactions)
        elif choice == "4":
            export_to_csv(transactions)
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

# Run the app
if __name__ == "__main__":
    main()
