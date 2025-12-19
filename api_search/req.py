import requests

class ApiRequest:
    def requesting_api(self):
        response=requests.get("https://openlibrary.org/search.json?q=crime+and+punishment&fields=key,title,author_name,editions")
        api_details=response.json()
        return api_details