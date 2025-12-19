import json
class Search:
    def search_data(self):
        if len(self.api_details)>0:
            key_entry=input("Please enter the key: ")

            for item in self.api_details["docs"]:
                for data in item["editions"]["docs"]:
                    if key_entry == data["key"]:
                        print(json.dumps(item,indent=4))
                        return
            else:
                print("not found")
        else:
            print("Please enter a digit not alphabet")  