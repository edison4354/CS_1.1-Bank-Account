from random import randint

class BankAccount:
  def __init__(self, full_name):
    self.full_name = full_name
    self.account_number = randint(100000000, 999999999)
    self.routing_number = 98765432
    self.balance = float(0)
  
  # def deposit(self, amount):
  #   self.balance += float(amount)
  #   return f"Amount Deposited: ${amount}"
  
  # def withdraw(self, amount):
  #   self.balance -= float(amount)
  #   if self.balance >= 0:
  #     return f"Amount Withdraw: ${amount}"
  #   else: 
  #     self.balance -= 10 
  #     return f"Insufficient funds. An overdraft fee of $10 has been charged."

  # Method that returns a input for the amount you wish to deposit 
  def deposit(self):
    """I've used a input function for "amount" instead of a parameter so the user can enter the amount they want to deposit in the termal instead of in the code"""
    amount = input("Please enter how much you would like to deposit:")
    self.balance += float(amount)
    return f"Amount Deposited: ${amount}"


  # Method that returns a input for the amount you wish to withdraw 
  def withdraw(self):
    """I've used a input function for "amount" instead of a parameter so the user can enter the amount they want to deposit in the termal instead of in the code"""
    amount = input("Please enter how much you would like to withdraw:")
    self.balance -= float(amount)
    if self.balance >= 0:
      return f"Amount Withdraw: ${amount}"
    else: 
      self.balance -= 10 
      return f"Insufficient funds. An overdraft fee of $10 has been charged."


  # Method that returns the current balance of your account
  def get_balance(self):
    return f"Thank for using Chase Bank, your current account balance is ${self.balance}"


  # Method that returns a new balance with the interest added
  def add_interest(self):
    interest = self.balance * 0.00083
    self.balance += interest
    return f"Your interest got added for this month!"


  # Method that returns a receipt of your name, account number, routing number, and balance
  def print_receipt(self):
    return f"{self.full_name}\nAccount No.: {self.account_number}\nRouting No.: {self.routing_number}\nBalance: ${self.balance}"

# Creating the Objects
edison_account = BankAccount("Edison Li")
nolan_account = BankAccount("Nolan Ngo")
sergio_account = BankAccount("Sergio Cuh")
iggi_account = BankAccount("Iggi jim")

# Object Methods
print(edison_account.deposit())
print(edison_account.add_interest())
print(edison_account.print_receipt())

print(nolan_account.withdraw())
print(nolan_account.print_receipt())