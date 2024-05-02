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
    transactions.append({'Type': transaction_type, 'Category': category, 'Amount': float(amount)})
    write_transactions(transactions)
    print(f"Transaction added successfully.")

def calculate_budget(transactions):
    income = sum(float(transaction['Amount']) for transaction in transactions if transaction['Type'] == 'Income')
    expenses = sum(float(transaction['Amount']) for transaction in transactions if transaction['Type'] == 'Expense')
    budget = income - expenses
    return budget

def analyze_expenses(transactions):
    expense_categories = {}
    total_expenses = 0
    total_income = sum(float(transaction['Amount']) for transaction in transactions if transaction['Type'] == 'Income')
    highest_expense = {'Category': None, 'Amount': float('-inf')}
    lowest_expense = {'Category': None, 'Amount': float('inf')}
    for transaction in transactions:
        if transaction['Type'] == 'Expense':
            category = transaction['Category']
            amount = float(transaction['Amount'])
            total_expenses += amount
            if amount > highest_expense['Amount']:
                highest_expense['Category'] = category
                highest_expense['Amount'] = amount
            if amount < lowest_expense['Amount']:
                lowest_expense['Category'] = category
                lowest_expense['Amount'] = amount
            if category in expense_categories:
                expense_categories[category] += amount
            else:
                expense_categories[category] = amount
    
    if expense_categories:
        print("Expense Analysis:")
        for category, amount in expense_categories.items():
            print(f"{category}: ₹ {amount:,.2f}")  # Format amount with commas, two decimal places, and prepend ₹ symbol with space
    else:
        print("No expenses recorded.")

    print(f"Highest Expense: {highest_expense['Category']}: ₹ {highest_expense['Amount']:,.2f}")
    print(f"Lowest Expense: {lowest_expense['Category']}: ₹ {lowest_expense['Amount']:,.2f}")
    expense_percentage = (total_expenses / total_income) * 100 if total_income != 0 else 0
    print(f"Percentage of Total Income Spent: {expense_percentage:,.2f}%")

    # Check if 50% of income covers 30% of expenses
    income_cover = 0.5 * total_income
    expense_cover = 0.3 * total_expenses
    if income_cover >= expense_cover:
        print("Expenses are healthy.")
    else:
        print("Expenses are too high.")

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
            print(f"Remaining budget: ₹ {budget:,.2f}")
        elif choice == '4':
            analyze_expenses(transactions)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
