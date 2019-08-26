import sys
from st2common.runners.base_action import Action

class MyAction(Action):

    def run(self, inp1, inp2):
        if (inp1 > inp2): 
            print(inp1+" is greater "+inp2)
        elif inp1 == inp2:
            print (inp1+" is Equal To "+inp2)    
        else:
            print(inp2+" is greater "+inp1)  
        #a = max(inp1,inp2)
        #b = min(inp1, inp2)
        #c = a 
        # a = int(inp1) + int(inp2)
        #print(a)
        return(True)