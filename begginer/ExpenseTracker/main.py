import argparse
from services import ExpenseTracker

def main():
    tracker = ExpenseTracker()
    try:
        while True:
            parser = argparse.ArgumentParser(description="Expense Tracker CLI")
            parser.add_argument("command", choices=["add", "list", "delete", "update", "exit", "summary"], help="Command to execute")
            
            parser.add_argument("--description", type=str, help="Description of the expense")
            parser.add_argument("--amount", type=float, help="Amount of the expense")
            parser.add_argument("--id", type=int, help="ID of the expense to delete or update")
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

            elif args.command == "list":
                tracker.expense_list()
                break
            elif args.command == "delete":
                if args.id:
                    tracker.delete_expense(args.id)
                    break
                else:
                    print("Please provide the ID of the expense to delete.")
                    break
            
            
    except KeyboardInterrupt:
        print("\nExiting the Expense Tracker. Goodbye!")

if __name__ == "__main__":
    main()