class BankAccount:
    def __init__(self, inital_balance =0):
       self.__balance = inital_balance
       
    def deposit(self, amount):
        self.__deposit += amount
        
    def  withdraw(self, amount):
        self.__withdraw -= amount
        
        if self.__withdraw <= self.__balance:
            print(f"Withdrew: {self.__withdraw}")
        else:
            print("Insufficient funds.")
    
    def display_balance(self):
        print(f"Current Balance: '$'{self.__balance}")
    
    