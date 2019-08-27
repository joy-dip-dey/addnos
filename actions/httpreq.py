import sys
from st2common.runners.base_action import Action

class MyAction(Action):

    def run(self, inp1):
        import requests 
        URL = inp1
        r = requests.get(URL, verify=False)
        data = r.json()
        print (data)