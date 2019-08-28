import sys
from st2common.runners.base_action import Action
import requests

class MyAction(Action):
    def run(self, inp1):
        r = requests.get(inp1, verify=False)
        data = r.json()
        print (data)