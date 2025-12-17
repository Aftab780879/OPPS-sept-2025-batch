from read_write import ReadWrite
from all_menu import Menu
from student_manage import Student_management
class MainExecution:
     def __init__(self,json_file):
          self.json_file=json_file
          self.student_list=[]
          ReadWrite.read_file(self)


     def Main_menu(self):
         
         while 1:
            reg_menu_choice=Menu.menu_view(self)
            if reg_menu_choice==1:
                Student_management.register(self)
            elif reg_menu_choice==2:
                Student_management.search(self)
            elif reg_menu_choice==3:
                Student_management.update(self)  
            elif reg_menu_choice==4:
                Student_management.delete(self)
            elif reg_menu_choice==5:
                break
            else:
                print("\nWrong Input , Please try again numbers (1 to 5) ") 