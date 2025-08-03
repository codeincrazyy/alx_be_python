class BankAccount:
    def __init__(self, initial_balance=0):
       self.__balance = initial_balance
       
    def deposit(self, amount):
        self.__balance += amount
        
    def  withdraw(self, amount):
        
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: ${amount}")
            return True
        else:
            return False
    
    def display_balance(self):
        print(f"Current Balance: ${self.__balance:.2f}")

    
    