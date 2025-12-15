def update_menu_view():
    try:

        print("\nPlease select one of the options to be Updated")
        print("1. First Name")
        print("2. Last Name")
        print("3. Address")
        print("4. Contact")
        print("5. Back")

        update_menu_choice=input("Please enter Your Choice: ")
        if update_menu_choice.isdigit():
            update_menu_choice=int(update_menu_choice)

            
        return update_menu_choice   
    except Exception:
        print("\nServer is Busy , Try After some time")   