from random import randint

class BankAccount:
  def __init__(self, full_name):
    self.full_name = full_name
    self.account_number = randint(100000000, 999999999)
    self.routing_number = 98765432
    self.balance = float(0)
  
  def deposit(self, amount):
    self.balance += float(amount)
    return f"Amount Deposited: ${amount}"
  
  def withdraw(self, amount):
    self.balance -= float(amount)
    if self.balance >= 0:
      return f"Amount Withdraw: ${amount}"
    else: 
      self.balance -= 10 
      return f"Insufficient funds. An overdraft fee of $10 has been charged."
  
  def get_balance(self):
    return f"Thank for using Chase Bank, your current account balance is ${self.balance}"

  def add_interest(self):
    interest = self.balance * 0.00083
    self.balance += interest
    return f"Your interest got added for this month!"

  def print_receipt(self):
    return f"{self.full_name}\nAccount No.: {self.account_number}\nRouting No.: {self.routing_number}\nBalance: ${self.balance}"

edison_account = BankAccount("Edison Li")
nolan_account = BankAccount("Nolan Ngo")
sergio_account = BankAccount("Sergio Cuh")
iggi_account = BankAccount("Iggi jim")

print(edison_account.deposit(90))
print(nolan_account.withdraw(92))
print(nolan_account.print_receipt())