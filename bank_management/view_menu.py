class Menu:
    def menu(self):
        print("1. To Deposit")
        print("2. To Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        menu_choice=input("Please enter Your Choice: ")
        if menu_choice.isdigit():
            menu_choice=int(menu_choice)
        return menu_choice    