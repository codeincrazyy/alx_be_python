class BankAccount:
    def __init__(self, initial_balance=0):
       self.__balance = initial_balance
       
    def deposit(self, amount):
        self.__balance += amount
        
    def  withdraw(self, amount):
        
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Insufficient funds.")
    
    def display_balance(self):
        print(f"Current Balance: ${self.__balance}")
    
    