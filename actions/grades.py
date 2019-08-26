import sys
from st2common.runners.base_action import Action

class MyAction(Action):

    def run(self, inp1):
        if (inp1 <= 24): 
            print("Your Grade is F")
        elif (inp1 in range(25,44)): 
            print ("Your Grade is E")
        elif (inp1 in range(45,50)): 
            print ("Your Grade is D")
        elif (inp1 in range(51,60)): 
            print ("Your Grade is C")
        elif (inp1 in range(61,80)): 
            print ("Your Grade is B")
        elif (inp1 in range(81,100)): 
            print ("Your Grade is A")          
        else:
            print("Invalid Marks Entered ...")  
        return(True)