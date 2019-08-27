import sys
from st2common.runners.base_action import Action

class MyAction(Action):

    def run(self, inp1):
        print(" ")
        for i in range(inp1):
            for j in range((inp1 - i) - 1):
                print(end = " ")
                for j in range(i + 1):
                    print("*", end = " ")        
        print()
        return(True)