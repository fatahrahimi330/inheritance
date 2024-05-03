from checkingAccount import CheckingAccount
from savingsAccount import SavingsAccount

class Main:
    checking = CheckingAccount(1000)
    savings = SavingsAccount(2000, 500)

    checking.deposit(500)
    checking.withdraw(200)
    print()

Main()
