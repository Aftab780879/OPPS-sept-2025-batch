from menu_view import Menu
from req import ApiRequest
from searching import Search


class Execution:
    def __init__(self):
        api_details=ApiRequest.requesting_api(self)
        self.api_details=api_details

    def execution(self):
        while 1:
            menu_choice=Menu.menu_view(self)
            if menu_choice==1:
                while 1:
                    search_menu_choice=Menu.search_menu(self)
                    if search_menu_choice==1:
                        Search.search_data(self)
                    elif search_menu_choice==2:
                        break
                    else:
                        print("Wrong Input")
            elif menu_choice==2:
                break
            else:
                print("Wrong input")        