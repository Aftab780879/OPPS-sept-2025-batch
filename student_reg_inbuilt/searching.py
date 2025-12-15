from student_reg_inbuilt.search_menu import search_menu_view
import json
def search_file(student_list):
    try:
        if len(student_list)>0:
            while 1:
                search_menu_choice=search_menu_view()
                if search_menu_choice==1:
                    first_name_search_entry=input("Please enter First Name: ").lower()
                    if first_name_search_entry.isalpha():
                        last_name_search_entry=input("Please enter the Last Name: ").lower()
                        if last_name_search_entry.isalpha():
                            for item in student_list:
                                if item["first_name"]==first_name_search_entry and item["last_name"]==last_name_search_entry:
                                        print(json.dumps(item,indent=4))
                                else:
                                    print("No detals with the following name")        
                        else:
                            print("please use characters only")
                    else:
                        print("please use characters only")        
                elif search_menu_choice==2:
                    address_search_entry=input("Please enter Address: ").lower()
                    if address_search_entry.isalnum() or address_search_entry.strip():
                        for item in student_list:
                            if item["address"]==address_search_entry:
                                print(json.dumps(item,indent=4))
                            else:
                                print("No Details with the following address")   
                    else:
                        print("please enter the address correctly")             

                elif search_menu_choice==3: 
                    contact_number_search=input("Please enter the contact of the student: ")
                    if contact_number_search.isdigit() and len(contact_number_search)==10:
                        contact_number_search=int(contact_number_search)
                        for item in student_list:
                            if item["contact"]==contact_number_search:
                                print(json.dumps(item,indent=4))
                            else:
                                print("\nNo details with the following contact number") 
                    else:
                        print("\nPlease use only number and of 10 digits")               

                elif search_menu_choice==4:
                    print(json.dumps(student_list,indent=4))

                elif search_menu_choice==5:
                    break     
                else:
                    print("\nWrong Input Please select number 1 to 5 ")           
        else:
            print("\nThere Is No Data Available to Search")
    except Exception:
        print("\nServer is Busy , Try After some time")        