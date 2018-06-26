class BankAccount(object):
  balance = 0
  def __init__(self, name):
    self.name = name
  
  def __repr__(self):
    return "Account: %s, Balance $%.2f" % (self.name, self.balance)
  
  def show_balance(self):
    print "Balance: $%.2f" % (self.balance)
  
  def deposit(self, amount):
    self.amount = amount
    if self.amount <= 0:
      print "Minimal deposit is 1$"
      return
    else:
      print "Deposit: $%.2f" % (self.amount)
      self.balance += amount
      self.show_balance()
  
  def withdraw(self, amount):
    self.amount = amount
    if self.amount > self.balance:
      print "Can't withdraw more than you have. Balance: $%.2f" % (self.balance)
      return
    else:
      print "Withdrawing $%.2f" % (self.amount)
      self.balance -= self.amount
      self.show_balance()
#my_account = BankAccount("Sauel")

def start():
  error = "\nUnknown error. Shutting down."
  verror = "\nError. Enter value, not word."
  try:
    my_account = BankAccount(str(raw_input("Enter your name: ")))
  except KeyboardInterrupt:
    print error
    return
  print my_account.__repr__()
  while True:
    try:
      option = raw_input("\nWhat do you want to do? Enter 'B' to check balance, 'D' to deposit and 'W' for withdraw. Press 'X' to exit: ").lower()
    except:
      print error
      return
    if option == "b":
      my_account.show_balance()
    elif option == "d":
      try:
        dep_sum = raw_input("\nHow much do you want to deposit: ")
      except:
        print "\n"
      try:
        my_account.deposit(float(dep_sum))
      except: 
        print verror
    elif option == "w":
      try:
        wit_sum = raw_input("\nHow much do you want to withdraw: ")
      except:
        print "\n"
      try:
        my_account.withdraw(float(wit_sum))
      except:
        print verror
    elif option == "x":
      print "\nGoodbye."
      break
    else:
      break
#print my_account.__repr__()
start()