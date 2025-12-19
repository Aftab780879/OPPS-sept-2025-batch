class Menu:
    def menu_view(self):
        print("1.To search")
        print("2.Exit")

        menu_choice=input("please enter your choice:  ")
        if menu_choice.isdigit():
            menu_choice=int(menu_choice)
        return menu_choice

    def search_menu(self):
        print("1. From Key")
        print("2. Back")    

        search_menu_choice=input("please enter your choice:  ")
        if search_menu_choice.isdigit():
            search_menu_choice=int(search_menu_choice)
        return search_menu_choice    