class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, balance, name):
        self.balance = balance
        self.name = name
        print(f"Account {self.name} created.\n${self.balance:.2f}\n")
    
    def getBalance(self):
        print(f"Account {self.name} balance = ${self.balance:.2f}")
    
    def deposit(self,amount):
        print(f"\nAccount {self.name} want to deposit ${amount:.2f}")
        self.balance = self.balance + amount
        print(f"Deposit ${amount:.2f} complete.")
        self.getBalance()
    
    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"Sorry, account {self.name} only has a balance of ${self.balance:.2f}"
            )
    
    def withdraw(self, amount):
        print(f"\nAccount {self.name} want to withdraw ${amount:.2f}")
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print(f"Withdraw ${amount:.2f} complete.")
            self.getBalance()
        except BalanceException as error:
            print(f"Withdraw interrupted: {error}")
    
    def transfer(self, amount, target):
        print(f"\nAccount {self.name} want to transfer ${amount:.2f} to {target.name}")
        try:
            print("********************\nBeginning Transfer...")
            self.viableTransaction(amount)
            # self.withdraw(amount)
            self.balance = self.balance - amount
            # target.deposit(amount)
            target.balance = target.balance + amount
            print(f"Transfer ${amount:.2f} complete.\n\n********************")

        except BalanceException as error:
            print(f"Transfer interrupted: {error}\n\n********************")

class InterestRewardsAccount(BankAccount):
    def deposit(self,amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete.")
        self.getBalance()

class SavingsAccount(InterestRewardsAccount):
    def __init__(self, balance, name):
        super().__init__(balance, name)
        self.fee = 5
    
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw completed.")
            self.getBalance()
        except BalanceException as error:
            print(f"Withdraw interrupted: {error}")
    