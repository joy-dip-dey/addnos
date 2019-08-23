import sys
from st2common.runners.base_action import Action

class MyAction(Action):

    def run(self, inp1, inp2):
        a = max(inp1,inp2)
        # a = int(inp1) + int(inp2)
        print(a)
        return(True,a)