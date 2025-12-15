from student_reg_inbuilt.write_file import write_json
import json
def delete_student_data(student_list,json_file):
    try:

        if len(student_list)>0:
            contact_number_search=input("Please enter the contact of the student: ")
            if contact_number_search.isdigit():
                contact_number_search=int(contact_number_search)
                for item in student_list:
                    if item["contact"]==contact_number_search:
                        print(json.dumps(item,indent=4))
                        student_list.remove(item)
                        write_json(json_file,student_list)
                        print("\nData Deleted Successfully")
                        break
                    else:
                        print("\nNo data Available with this details")    
            else:
                print("\nplease use only numbers and 10 digits only")
        else:
            print("\nThere Is No Data To Be Deleted")
    except Exception:
        print("\nServer is Busy , Try After some time")         