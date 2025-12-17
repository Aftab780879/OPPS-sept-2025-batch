import json
import os
import uuid
from read_write import ReadWrite
from all_menu import Menu


class Student_management:
     

     def register(self):
           student_dict={}
        
           student_dict["id"]=uuid.uuid4().hex[:8]
           student_dict["first_name"]=input("please enter student first name: ").lower()
           if student_dict["first_name"].isalpha():
                student_dict["last_name"]=input("please enter student last name: ").lower()
                if student_dict["last_name"].isalpha():
                    student_dict["address"]=input("please enter student address: ").lower()
                    if student_dict["address"].isalnum() or student_dict["address"].strip():

                        while 1:
                            contact_check_entry=input("Please enter the contact number: ")
                            if contact_check_entry.isdigit() and len(contact_check_entry)==10:
                                contact_check_entry=int(contact_check_entry)
                                for item in self.student_list:
                                    if item["contact"]==contact_check_entry:
                                        print("\nthis phone number exist whit somebody else , please enter some other number")
                                        break
                                else:
                                    student_dict["contact"]=contact_check_entry  
                                    self.student_list.append(student_dict)
                                    ReadWrite.write_json(self)
                                    print("\nSuccessfully added student")
                                    break
                            else:
                                print("Please enter a 10 digit contact number")            
                    else:
                        print("\nplease use only characters")               
                else:
                    print("\nplease use only characters")    
           else:
                print("\nplease use only characters")     

     def search(self):
         
         if len(self.student_list)>0:
            while 1:
                     search_menu_choice=Menu.search_menu(self)       
                     if search_menu_choice==1:
                         
                         first_name_search_entry=input("Please enter First Name: ").lower()
                         if first_name_search_entry.isalpha():
                             last_name_search_entry=input("Please enter the Last Name: ").lower()
                             if last_name_search_entry.isalpha():
                                 for item in self.student_list:
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
                             for item in self.student_list:
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
                             for item in self.student_list:
                                 if item["contact"]==contact_number_search:
                                     print(json.dumps(item,indent=4))
                             else:
                                 print("\nNo details with the following contact number") 
                         else:
                             print("\nPlease use only number and of 10 digits")               

                     elif search_menu_choice==4:
                         print(json.dumps(self.student_list,indent=4))

                     elif search_menu_choice==5:
                         break     
                     else:
                         print("\nWrong Input Please select number 1 to 5 ")           
         else:
             print("\nThere Is No Data Available to Search")
          

     def update(self):
         if len(self.student_list)>0:
            contact_number_search=input("Please enter the contact of the student: ")
            if contact_number_search.isdigit():
                contact_number_search=int(contact_number_search)
                for item in self.student_list:
                    if item["contact"]==contact_number_search:
                        print(json.dumps(item,indent=4))
                        while 1:
                            update_menu_choice=Menu.update_menu(self)
                            if update_menu_choice==1:
                                new_first_name=input("Please enter The correct First Nmae: ").lower()
                                if new_first_name.isalpha():
                                    item["first_name"]=new_first_name
                                    print(json.dumps(item,indent=4))
                                    ReadWrite.write_json(self)
                                    print("\nFirst name Updated SuccessFully\n")
                                else:
                                    print("\nplease use only characters")   
                            elif update_menu_choice==2:
                                new_last_name=input("Please enter The correct Last Nmae: ").lower()
                                if new_last_name.isalpha():
                                    item["last_name"]=new_last_name
                                    print(json.dumps(item,indent=4))
                                    ReadWrite.write_json(self)
                                    print("\nLast name Updated SuccessFully\n")
                                else:
                                    print("\nplease input only characters")    
                            elif update_menu_choice==3:
                                new_address=input("Please enter Your new address: ").lower()
                                item["address"]=new_address
                                print(json.dumps(item,indent=4))
                                ReadWrite.write_json(self)
                                print("\nAddress updated Successfully\n")
                            elif update_menu_choice==4:
                                secret_key=491999
                                print("contact number update feature is not available for All, it needs secret key")
                                secret_key_entry=input("Please enter the secret key: ")
                                if secret_key_entry.isdigit():
                                    secret_key_entry=int(secret_key_entry)
                                    if secret_key_entry==secret_key:
                                        new_contact_number=input("Please enter the new contact number: ")
                                        if new_contact_number.isdigit():
                                            new_contact_number=int(new_contact_number)
                                            item["contact"]=new_contact_number
                                            print(json.dumps(item,indent=4))
                                            ReadWrite.write_json(self)
                                            print("\nContact Updated Successfully\n")
                                        else:
                                            print("\nPlease use only digits")
                                    else:
                                        print("Wrong Secret Key")    
                            elif update_menu_choice==5:
                                break
                            else:
                                ("\nWrong Input, Please try numbers 1 to 5")     
            else:
                print("please enter only digits")                       
         else:
             print("\nThere Is no data For Update")        
                                       
     def delete(self):
         if len(self.student_list)>0:
            contact_number_search=input("Please enter the contact of the student: ")
            if contact_number_search.isdigit():
                contact_number_search=int(contact_number_search)
                for item in self.student_list:
                    if item["contact"]==contact_number_search:
                        print(json.dumps(item,indent=4))
                        self.student_list.remove(item)
                        ReadWrite.write_json(self)
                        print("\nData Deleted Successfully")
                        break
                else:
                    print("\nNo data Available with this details")    
            else:
                print("\nplease use only numbers and 10 digits only")
         else:
             print("\nThere Is No Data To Be Deleted")                                  
     
   
     
           






