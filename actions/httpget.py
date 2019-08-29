import sys
from st2common.runners.base_action import Action
import requests
import json
from datetime import datetime

class MyAction(Action):

    def run(self, inp1):
        URL = "https://fakerestapi.azurewebsites.net/api/Books"
        r = requests.get(URL, params = {"ID": inp1}, verify=False)
        data = r.json()
        fout = json.dumps(data, indent=4, sort_keys=True)
        print (fout)
        return(True)