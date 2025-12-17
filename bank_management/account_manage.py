import time
class BankAccount:
    def __init__(self,account_number):
        self.account_number=account_number
        self.__balance=0
        self.__pin=4268
    
    def deposit(self,deposit_input,pin):
        if pin==self.__pin:
            if deposit_input>0:

                total_balance_ad=self.__balance+deposit_input
                self.__balance=total_balance_ad
                print(f"\nDeposit of {deposit_input} Successful")
            else:
                print("\nDeposit Amount cant be 0")    
        else:
            print("\nPin is Incorrect")   

    def withdrawl(self,withdrawl_input,pin):
        if pin==self.__pin:
            if withdrawl_input<self.__balance:
                total_balance_aw=self.__balance-withdrawl_input
                self.__balance=total_balance_aw
                print(f"\nWithdrawl of amount {withdrawl_input} Successful")
            else:
                print("\nInsufficient Balance")  
        else:
            print("\nWrong Pin ") 

    def balence_check(self,pin):
        if pin==self.__pin:
            print(f"\nAccount Number= {self.account_number}")
            print(f"Balance= {self.__balance}")

            


