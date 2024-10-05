# Define the class BankAccount that takes information from a single account
class BankAccount:
  def __init__(self, account_number, balance):
    self.account_number = account_number
    self.balance = balance


# Define the class Bank that contains multiple operations for managing banking accounts
class Bank:
  def __init__(self):
    self.account_list = []
  
  # Method for adding a new account to the bank
  def create_account(self,new_account):
    from random import randint
    self.new_account = new_account
    new_account.account_number = randint(10000,99999)
    new_account.balance = round(float(input("Enter the amount you would like to deposit into the new account: ")), 2)
    while new_account.balance <= 0:
      new_account.balance = round(float(input("Deposit not above $0. Enter the amount you would like to deposit into the new account: ")), 2)


  # Method for obtaining information on an account
  def get_account(self, bank_account):
    self.bank_account = bank_account
    account = self.bank_account
    print("Account number:", account.account_number)
    print("Balance: $" + str(account.balance))
  
  # Method for depositing money into an account
  def deposit(self, bank_account):
    self.bank_account = bank_account
    account = self.bank_account
    amount = round(float(input("Enter the amount you would like to deposit: ")), 2)
    while amount <= 0:
      amount = round(float(input("Deposit not above $0. Enter the amount you would like to deposit: ")), 2)
    account.balance += amount
    print("Deposit successful! Your new balance is $" + str(account.balance))

  # Method for withdrawing money from an account
  def withdraw(self, bank_account):
    self.bank_account = bank_account
    account = self.bank_account
    amount = round(float(input("Enter the amount you would like to withdraw: ")), 2)
    while amount > account.balance or amount <= 0:
      amount = round(float(input("Withdraw not above balance or above $0. Enter the amount you would like to withdraw: ")), 2)
    account.balance -= amount
    print("Withdraw successful! Your new balance is $" + str(account.balance))

  # Method for transferring money from one account to another
  def transfer(self, bank_account1, bank_account2):
    self.bank_account1 = bank_account1
    self.bank_account2 = bank_account2
    amount = round(float(input("Enter the amount you would like to transfer: ")),2)
    while amount > bank_account1.balance or amount <= 0:
      amount = round(float(input("Transfer not above first balance or above $0. Enter the amount you would like to transfer: ")), 2)
    bank_account1.balance -= amount
    bank_account2.balance += amount
    print("Transfer successful!")
    print("Your new balance for the first account is $" + str(bank_account1.balance))
    print("Your new balance for the second account is $" + str(bank_account2.balance))







# Function for execting banking program operation in menu:
def execute_choice():
  account_list = {}
  acnum_list = []
  balance_list = []
  test_bank = Bank()

  
  while True:
    print("\nOptions:") 
    print("1. Create account")  
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Transfer")
    print("6. Quit")
    choice = int(input("\nEnter your choice: "))
    n = len(account_list)
    if choice == 1:
      n = len(account_list) + 1
      account_list[n] = {}
      account = BankAccount(000000,0)
      test_bank.create_account(account)
      
      while account.account_number in acnum_list:
        print("Account number already exists. Generating new account number...")
        from random import randint
        account.account_number = randint(10000,99999)
      
      print("Account created successfully!")
      print("Account number:", account.account_number)
      print("Balance: $" + str(account.balance))
      account_list[n]["Account Number"] = account.account_number
      account_list[n]["Balance"] = account.balance
      acnum_list.append(account_list[n]["Account Number"])
      balance_list.append(account_list[n]["Balance"])


    elif choice == 2:
      if n == 0:
        print("No accounts to deposit to.")
      else:
        choice_input = int(input("Enter account number: "))
        while choice_input not in acnum_list:
          choice_input = int(input("Account number not found. Enter a valid account number: "))
        for d in account_list:
          if choice_input == account_list[d]["Account Number"]:
            account = BankAccount(choice_input, account_list[d]["Balance"])
            test_bank.deposit(account)
            account_list[d]["Balance"] = account.balance
            balance_list[d-1] = account.balance



    elif choice == 3:
      if n == 0:
        print("No accounts to withdraw from.")
      else:
        choice_input = int(input("Enter account number: "))
        while choice_input not in acnum_list:
          choice_input = int(input("Account number not found. Enter a valid account number: "))
        for w in account_list:
          if choice_input == account_list[w]["Account Number"]:
            account = BankAccount(choice_input, account_list[w]["Balance"])
            if account.balance > 0:
              test_bank.withdraw(account)
              account_list[w]["Balance"] = account.balance
              balance_list[w-1] = account.balance
            else:
              print("Account balance is $0 or below. Withdrawal not possible.")




    elif choice == 4:
      if n == 0:
        print("No accounts to check balance of.")
      else:
        choice_input = int(input("Enter account number: "))
        while choice_input not in acnum_list:
          choice_input = int(input("Account number not found. Enter a valid account number: "))
        for g in account_list:
          if choice_input == account_list[g]["Account Number"]:
            account = BankAccount(choice_input, account_list[g]["Balance"])
            test_bank.get_account(account)



    elif choice == 5:
      if n <= 1:
        print("Not enough accounts to transfer.")
      else:
        choice_input1 = int(input("Enter the account number you would like to transfer funds out of: "))
        while choice_input1 not in acnum_list:
          choice_input1 = int(input("Account number not found. Enter a valid account number: "))
        choice_input2 = int(input("Enter the account number you would like to transfer funds into: "))
        while choice_input2 not in acnum_list or choice_input2 == choice_input1:
          choice_input2 = int(input("Account number not found or already used. Enter a valid account number: "))
        for t in account_list:
          if choice_input1 == account_list[t]["Account Number"]:
            account1 = BankAccount(choice_input1, account_list[t]["Balance"])
          elif choice_input2 == account_list[t]["Account Number"]:
            account2 = BankAccount(choice_input2, account_list[t]["Balance"])

        if account1.balance > 0:
          test_bank.transfer(account1, account2)
          for s in account_list:
            if choice_input1 == account_list[s]["Account Number"]:
              account_list[s]["Balance"] = account1.balance
              balance_list[s-1] = account1.balance
            elif choice_input2 == account_list[s]["Account Number"]:
              account_list[s]["Balance"] = account2.balance
              balance_list[s-1] = account2.balance
        else:
          print("Balance of first account is $0 or below. Transfer not possible.")


    elif choice == 6:
      print("Thank you! Please try again later.")
      break
    else:
      print("Invalid choice.")




  

# Calls the execute_choice function to start the banking program
execute_choice()


# Recursive function that repeats the program if the user chooses yes (y) or ends it if the user chooses no (n).

repeat = input("Would you like to repeat the program? (y/n): ")
while repeat.lower() != "y" and repeat.lower() != "n":
  repeat = input("Invalid input. Would you like to repeat the program? (y/n): ")
  
while repeat.lower() == "y":
  execute_choice()
  repeat = input("Would you like to repeat the program? (y/n): ")
if repeat.lower() == "n":
  print("Thank you! Goodbye.")


















