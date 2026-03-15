import json
import datetime

class ExpenseTracker:
    def __init__(self, filename='expenses.json'):
        self.filename = filename
        self.expenses = self.load_expenses()

    def load_expenses(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_expenses(self):
        with open(self.filename, 'w') as file:
            json.dump(self.expenses, file)

    def __len__(self):        
        return len(self.expenses)

    def add_expense(self, amount, description):
        expense = {
            'id': len(self.expenses) + 1,
            'amount': f'${amount:.2f}',
            'description': description,
            'date': datetime.datetime.now().isoformat()
        }
        self.expenses.append(expense)
        self.save_expenses()
        if self.expenses:
            print(f"Expense added successfully: (ID: {expense['id']})")
        else:
            print("No expenses to add.")

    def expense_summary(self):
        total = sum(float(expense['amount'].strip('$')) for expense in self.expenses)
        print(f"Total expenses: ${total}")

    def expense_list(self):
        if not self.expenses:
            print("No expenses recorded.")
            return
        print("Expense List:\n")
        print(f"{'ID':<5} {'Date':<20} {'Description':<10} {'Amount':<10}")
        for expense in self.expenses:
            print(f"{expense['id']} {expense['date']} {expense['description']} {expense['amount']}\n")

    def delete_expense(self, expense_id):
        for expense in self.expenses:
            if expense['id'] == expense_id:
                self.expenses.remove(expense)
                self.save_expenses()
                print(f"Expense with ID {expense_id} deleted successfully.")
                return
        print(f"Expense with ID {expense_id} not found.")

