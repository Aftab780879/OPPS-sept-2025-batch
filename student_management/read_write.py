import json
import os
class ReadWrite:
    def __init__(self):
        pass

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