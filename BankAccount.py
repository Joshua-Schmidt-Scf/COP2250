class BankAcct:
    def __init__(self, name, account_number, amount, interest_rate):
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate

    # Deposit money
    def deposit(self, deposit_amount):
        if deposit_amount > 0:
            self.amount += deposit_amount
            print(f"Deposited: ${deposit_amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    # Withdraw money
    def withdraw(self, withdraw_amount):
        if withdraw_amount <= 0:
            print("Withdrawal amount must be positive.")
        elif withdraw_amount > self.amount:
            print("Insufficient funds.")
        else:
            self.amount -= withdraw_amount
            print(f"Withdrew: ${withdraw_amount:.2f}")

    # Adjust the interest rate
    def adjust_interest_rate(self, new_rate):
        self.interest_rate = new_rate
        print(f"Interest rate changed to {new_rate:.2f}%")

    # Return the account balance
    def get_balance(self):
        return self.amount

    # Calculate simple interest based on number of days
    def calculate_interest(self, days):
        interest = self.amount * (self.interest_rate / 100) * (days / 365)
        return interest

    # Display account information
    def __str__(self):
        return (f"Account Holder Name: {self.name}\n"
                f"Account Number: {self.account_number}\n"
                f"Account Balance: ${self.amount:.2f}\n"
                f"Account Interest Rate: {self.interest_rate:.2f}%")

# Test function
def test_bank_account():
    # Create account
    account = BankAcct("Dave Jones", "5555555555", 1000000.00, 4.5)

    print("Checking Account")
    print(account)
    print()

    # Deposit
    account.deposit(500)
    print(account)
    print()

    # Withdraw
    account.withdraw(250)
    print(account)
    print()

    # Change interest rate
    account.adjust_interest_rate(5.0)
    print(account)
    print()

    # Show account balance
    print(f"Current Balance: ${account.get_balance():.2f}")
    print()

    # Calculate interest for 90 days
    interest = account.calculate_interest(90)
    print(f"Interest earned in 90 days: ${interest:.2f}")
    print()

    # Final account information
    print("Final Account Information")
    print(account)


# Run the test function
test_bank_account()