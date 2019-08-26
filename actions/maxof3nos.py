import sys
from st2common.runners.base_action import Action

class MyAction(Action):

    def run(self, inp1, inp2, inp3):
        
        a = max(inp1,inp2,inp3)
        
        print("Maximum of "+str(inp1)+" "+str(inp2)+" "+str(inp3)+" is "+str(a))
        return(True)