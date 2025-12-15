def reg_menu():
    try:

        print("\n*****DASHBOARD*****")
        print("   1. To Register")
        print("   2. To Search")
        print("   3. To Update")
        print("   4. To Delete")
        print("   5. To Exit")

        reg_menu_choice=input("please enter your choice: ")
        if reg_menu_choice.isdigit():
            reg_menu_choice=int(reg_menu_choice)
            

        return reg_menu_choice      
    except Exception:
        print("\nServer is Busy , Try After some time")    