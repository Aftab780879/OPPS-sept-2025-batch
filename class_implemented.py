import json
import os
import uuid


class Student_management:
     def __init__(self,json_file):
          self.json_file=json_file
          self.student_list=[]
          self.read_file()


     def read_file(self):
          if os.path.exists(self.json_file):
            with open(self.json_file,'r') as file:
                data= file.read().strip()
                if data=="":
                    self.student_list= []
                else:
                    self.student_list=json.loads(data)
          else:         
             with open(self.json_file,'w') as file:
                 file.write("[]")
                 self.student_list= []  

     def write_json(self):
         with open(self.json_file,'w') as file:
                    file.write(json.dumps(self.student_list,indent=4)) 

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
                                    self.write_json()
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
                 print("\nplease select one of the options to search with")
                 print("1. From Name")
                 print("2. From Address")
                 print("3. From Contact")
                 print("4. View All Records")
                 print("5. Go Back")

                 search_menu_choice=input("Please Enter Your Choice: ")
                 if search_menu_choice.isdigit():
                     search_menu_choice=int(search_menu_choice)


                
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

     def update(self):
         if len(self.student_list)>0:
            contact_number_search=input("Please enter the contact of the student: ")
            if contact_number_search.isdigit():
                contact_number_search=int(contact_number_search)
                for item in self.student_list:
                    if item["contact"]==contact_number_search:
                        print(json.dumps(item,indent=4))
                        while 1:
                            update_menu_choice=self.update_menu()
                            if update_menu_choice==1:
                                new_first_name=input("Please enter The correct First Nmae: ").lower()
                                if new_first_name.isalpha():
                                    item["first_name"]=new_first_name
                                    print(json.dumps(item,indent=4))
                                    self.write_json()
                                    print("\nFirst name Updated SuccessFully\n")
                                else:
                                    print("\nplease use only characters")   
                            elif update_menu_choice==2:
                                new_last_name=input("Please enter The correct Last Nmae: ").lower()
                                if new_last_name.isalpha():
                                    item["last_name"]=new_last_name
                                    print(json.dumps(item,indent=4))
                                    self.write_json()
                                    print("\nLast name Updated SuccessFully\n")
                                else:
                                    print("\nplease input only characters")    
                            elif update_menu_choice==3:
                                new_address=input("Please enter Your new address: ").lower()
                                item["address"]=new_address
                                print(json.dumps(item,indent=4))
                                self.write_json()
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
                                            self.write_json()
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
                        self.write_json()
                        print("\nData Deleted Successfully")
                        break
                else:
                    print("\nNo data Available with this details")    
            else:
                print("\nplease use only numbers and 10 digits only")
         else:
             print("\nThere Is No Data To Be Deleted")                                  
     
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
     
     def Main_menu(self):
         
         while 1:
            reg_menu_choice=self.menu_view()
            if reg_menu_choice==1:
                self.register()
            elif reg_menu_choice==2:
                self.search()
            elif reg_menu_choice==3:
                self.update()  
            elif reg_menu_choice==4:
                self.delete()
            elif reg_menu_choice==5:
                break
            else:
                print("\nWrong Input , Please try again numbers (1 to 5) ")        






