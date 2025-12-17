class Menu:
    def menu_view(self):
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
    
    def update_menu(self):
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
    
    def search_menu(self):
         print("\nplease select one of the options to search with")
         print("1. From Name")
         print("2. From Address")
         print("3. From Contact")
         print("4. View All Records")
         print("5. Go Back")

         search_menu_choice=input("Please Enter Your Choice: ")
         if search_menu_choice.isdigit():
             search_menu_choice=int(search_menu_choice)
         return search_menu_choice 