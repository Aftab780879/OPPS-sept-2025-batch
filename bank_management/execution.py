from view_menu import Menu
from account_manage import BankAccount
from amount_input import Amount
class Execution():
    def main_execution(self):
        account=BankAccount(1010101010)
        while 1:
            menu_choice=Menu.menu(self)
            if menu_choice==1:
                deposit_amount=Amount.deposit_amoumt(self)
                pin=Amount.pin_entry(self)
                account.deposit(deposit_amount,pin)
            elif menu_choice==2:
                withdraw_amount=Amount.withdraw_amoumt(self)
                pin=Amount.pin_entry(self)
                account.withdrawl(withdraw_amount,pin)
            elif menu_choice==3:
                pin=Amount.pin_entry(self)
                account.balence_check(pin)
            elif menu_choice==4:
                break
            else:
                print("Wrong Input , try (1-4)")

