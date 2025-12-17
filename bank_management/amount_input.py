class Amount:
    def deposit_amoumt(self):
        print("\n********** DEPOSIT **********")
        deposit_input=input("Please enter the deposit amount: ")
        if deposit_input.isdigit():
            deposit_input=int(deposit_input)
        return deposit_input 

    def withdraw_amoumt(self):
        print("\n********** WITHDRAW **********")
        withdraw_input=input("Please enter the withdraw amount: ")
        if withdraw_input.isdigit():
            withdraw_input=int(withdraw_input)
        return withdraw_input
    
    def pin_entry(self):
        
        pin_input=input("please enter the pin: ")
        if pin_input.isdigit():
            pin_input=int(pin_input)
        return pin_input    
 