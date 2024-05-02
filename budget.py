import csv
import os

def read_transactions():
    transactions = []
    if not os.path.isfile('budget_data.csv'):
        with open('budget_data.csv', mode='w', newline='') as file:
            fieldnames = ['Type', 'Category', 'Amount']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
    with open('budget_data.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            transactions.append(row)
    return transactions

def write_transactions(transactions):
    with open('budget_data.csv', mode='w', newline='') as file:
        fieldnames = ['Type', 'Category', 'Amount']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for transaction in transactions:
            writer.writerow(transaction)

def add_transaction(transactions, transaction_type, category, amount):
    transactions.append({'Type': transaction_type, 'Category': category, 'Amount': amount})
    write_transactions(transactions)
    print(f"Transaction added successfully.")

def calculate_budget(transactions):
    income = sum(float(transaction['Amount']) for transaction in transactions if transaction['Type'] == 'Income')
    expenses = sum(float(transaction['Amount']) for transaction in transactions if transaction['Type'] == 'Expense')
    budget = income - expenses
    return budget

def analyze_expenses(transactions):
    expense_categories = {}
    for transaction in transactions:
        if transaction['Type'] == 'Expense':
            category = transaction['Category']
            amount = float(transaction['Amount'])
            if category in expense_categories:
                expense_categories[category] += amount
            else:
                expense_categories[category] = amount
    return expense_categories

def main():
    transactions = read_transactions()
    
    while True:
        print("\n1. Add Income")
        print("2. Add Expense")
        print("3. Calculate Budget")
        print("4. Analyze Expenses")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            category = input("Enter income category: ")
            amount = input("Enter income amount: ")
            add_transaction(transactions, 'Income', category, amount)
        elif choice == '2':
            category = input("Enter expense category: ")
            amount = input("Enter expense amount: ")
            add_transaction(transactions, 'Expense', category, amount)
        elif choice == '3':
            budget = calculate_budget(transactions)
            print(f"Remaining budget: {budget}")
        elif choice == '4':
            expense_analysis = analyze_expenses(transactions)
            print("Expense Analysis:")
            for category, amount in expense_analysis.items():
                print(f"{category}: {amount}")
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
