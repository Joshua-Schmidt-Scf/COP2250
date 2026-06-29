from functools import reduce

def main():
    expenses = []

    num_expenses = int(input("How many expenses would you like to enter? "))

    for i in range(num_expenses):
        expense_type = input(f"\nEnter expense #{i + 1} name (Home,Auto, Ect...): ")
        amount = float(input("Enter expense amount: $"))
        expenses.append((expense_type, amount))

    # Total amount of expenses
    total_expense = reduce(lambda total, expense: total + expense[1], expenses, 0)

    # Highest expense
    highest_expense = reduce(
        lambda highest, expense: expense if expense[1] > highest[1] else highest,
        expenses
    )

    # Lowest expense
    lowest_expense = reduce(
        lambda lowest, expense: expense if expense[1] < lowest[1] else lowest,
        expenses
    )

    print("\n----- Expense Summary -----")
    print(f"Total Expenses: ${total_expense:.2f}")
    print(f"Highest Expense: {highest_expense[0]} - ${highest_expense[1]:.2f}")
    print(f"Lowest Expense: {lowest_expense[0]} - ${lowest_expense[1]:.2f}")

main()