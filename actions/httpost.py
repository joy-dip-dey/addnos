import sys
from st2common.runners.base_action import Action
import requests
import json

class MyAction(Action):

    def run(self, inp1, inp2, inp3, inp4, inp5, inp6):
        URL = "https://fakerestapi.azurewebsites.net/api/Books"
        inpdata = {
                   "ID": inp1,
                   "Title": inp2,
                   "Description": inp3,
                   "PageCount": inp4,
                   "Excerpt": inp5,
                   "PublishDate": inp6
                  }
		  
        header = {
		          'Content-Type': 'application/json',
		          'Accept': 'application/json'
                 }
        DATA = json.dumps(inpdata)		  
        r = requests.post(url = URL, data = DATA, headers = header)
        output = r.json()
        print(output)	   
        return(True)