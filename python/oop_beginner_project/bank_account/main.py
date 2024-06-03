from bank_account import *

print("\n")
Dave = BankAccount(1000,"Dave")
Sara = BankAccount(2000,"Sara")

Dave.getBalance()
Sara.getBalance()

Sara.deposit(500)
Dave.withdraw(2000)
Dave.withdraw(10)
Dave.transfer(100,Sara)

Jim = InterestRewardsAccount(1000,"Jim")
Jim.getBalance()
Jim.deposit(100)
Jim.transfer(100,Dave)

Blaze = SavingsAccount(1000,"Blaze")
Blaze.getBalance()
Blaze.deposit(100)
Blaze.withdraw(100)