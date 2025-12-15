from student_reg_inbuilt.write_file import write_json
import uuid

def registration(student_list):
    try:
         
        json_file=r"C:\indixpert\OPPS\OPPS-sept-2025-batch\student_reg_inbuilt\student.json"
        

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
                            for item in student_list:
                                if item["contact"]==contact_check_entry:
                                    print("\nthis phone number exist whit somebody else , please enter some other number")
                                    break
                            else:
                                student_dict["contact"]=contact_check_entry  
                                student_list.append(student_dict)
                                write_json(json_file,student_list)
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
    except Exception:
        print("\nServer is Busy , Try After some time")         