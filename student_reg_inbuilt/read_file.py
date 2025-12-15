import os

def read_json():
    try:
        json_file=r"C:\indixpert\OPPS\OPPS-sept-2025-batch\student_reg_inbuilt\student.json"

        if os.path.exists(json_file):
            with open(json_file,'r') as file:
                data= file.read().strip()
                if data=="":
                    return "[]"
                return data
        else:
            with open(json_file,'w') as file:
                file.write("[]")
                return "[]"
    except Exception:
        print("\nServer is Busy , Try After some time")      
