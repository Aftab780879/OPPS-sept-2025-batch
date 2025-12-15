from student_reg_inbuilt.menu import reg_menu
from student_reg_inbuilt.registration import registration
from student_reg_inbuilt.read_file import read_json
from student_reg_inbuilt.searching import search_file
from student_reg_inbuilt.update import update_file
from student_reg_inbuilt.delete import delete_student_data
import json
student_list=[]
json_file=r"C:\indixpert\OPPS\OPPS-sept-2025-batch\student_reg_inbuilt\student.json"
def operations():
    try:
        data=read_json()
        student_list=json.loads(data)
        while 1:
            reg_menu_choice=reg_menu()
            if reg_menu_choice==1:
                registration(student_list)
            elif reg_menu_choice==2:
                search_file(student_list)
            elif reg_menu_choice==3:
                update_file(student_list,json_file)  
            elif reg_menu_choice==4:
                delete_student_data(student_list,json_file)
            elif reg_menu_choice==5:
                break
            else:
                print("\nWrong Input , Please try again numbers (1 to 5) ")
    except Exception:
        print("\nServer is Busy , Try After some time")              