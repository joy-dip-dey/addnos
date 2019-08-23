import sys
from st2common.runners.base_action import Action

class MyAction(Action):

    def run(self, inp1, inp2):
        a = int(inp) + int(inp2)
        print(a)
        return(True)