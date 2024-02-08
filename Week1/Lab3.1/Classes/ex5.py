class Bank():
   def __init__(self,owner,balance):
       self.owner=owner
       self.balance=balance

   def deposit(self,amount):
      self.balance += amount
      print(f"The deposit in the amount of {amount} has been successfully completed. New balance")

   def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"The withdrawal of funds in the amount of {amount} has been successfully completed. New balance: {self.balance}")
        else:
            print("There are not enough funds in the account")


owner1 = Bank("Linus", 18000)
owner2 = Bank("Sasha", 19000)

owner1.deposit(500)  # Депозит 500 на счет Sasha
owner1.withdraw(2000)  # Снятие 2000 со счета Sasha
owner2.withdraw(500)  # Снятие 500 со счета Linus