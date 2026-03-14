import json

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
            'description': description
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
