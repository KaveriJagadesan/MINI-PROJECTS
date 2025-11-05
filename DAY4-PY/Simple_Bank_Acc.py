class BankAccount:
    """A class to model a basic bank account with deposit and withdrawal functionality."""

    def __init__(self, initial_balance=0):
        
        self.balance = initial_balance
        print(f"Account created with initial balance of ${self.balance:.2f}.")

    def deposit(self, amount):
       
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance is ${self.balance:.2f}.")
        else:
            print("Invalid deposit amount. Amount must be positive.")

    def withdraw(self, amount):
        
        if amount > self.balance:
            print("Insufficient funds. Withdrawal failed.")
        elif amount <= 0:
            print("Invalid withdrawal amount. Amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance is ${self.balance:.2f}.")

    def get_balance(self):
       
        return self.balance

### Creating and using objects

#The following code demonstrates how to create a `BankAccount` object and use its methods.

# 1. Create an account with an initial balance
my_account = BankAccount(100)

# 2. Deposit money
my_account.deposit(50)

# 3. Attempt to withdraw more than the available balance
my_account.withdraw(200)

# 4. Withdraw a valid amount
my_account.withdraw(25)

# 5. Print the final balance
print(f"Final balance: ${my_account.get_balance():.2f}")
