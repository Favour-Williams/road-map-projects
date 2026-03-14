import argparse
from services import ExpenseTracker

def main():
    tracker = ExpenseTracker()
    try:
        while True:
            parser = argparse.ArgumentParser(description="Expense Tracker CLI")
            parser.add_argument("command", choices=["add", "view", "delete", "update", "exit", "summary"], help="Command to execute")
            
            parser.add_argument("--description", type=str, help="Description of the expense")
            parser.add_argument("--amount", type=float, help="Amount of the expense")

            args = parser.parse_args()

            if args.command == "add":
                if args.description and args.amount:
                    print(f"Adding expense: {args.description}, Amount: {args.amount}")
                    tracker.add_expense(args.amount, args.description)
                    break
                else:
                    print("Please provide description and amount to add an expense.")

            elif args.command == "summary":
                tracker.expense_summary()
                break
            
    except KeyboardInterrupt:
        print("\nExiting the Expense Tracker. Goodbye!")

if __name__ == "__main__":
    main()
