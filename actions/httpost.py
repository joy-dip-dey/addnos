import sys
from st2common.runners.base_action import Action
import requests
import json
from datetime import datetime

class MyAction(Action):

    def run(self, bookid, booktitle, despcrip, pgcount, excerpt):
        URL = "https://fakerestapi.azurewebsites.net/api/Books"
        today = datetime.now()
        #nowintimestmp = datetime.timestamp(today)
        inpdata = {
                   "ID": bookid,
                   "Title": booktitle,
                   "Description": despcrip,
                   "PageCount": pgcount,
                   "Excerpt": excerpt,
                   "PublishDate": str(today)
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