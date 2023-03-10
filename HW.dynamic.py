# dynamic

class Box:
    
    #defalut behavior
    def __init__(self, value=None):
     #HW1: modify init code, so it puts None when no arguments passed
     self.value = value
   
    # intended behavior
    def isEmpty(self):
       if self.value == None:
          return True
       else:
          return False
    
#################################
b1 = Box()
b2 = Box(1000)

if b1.isEmpty():
   print("The box1 is empty!")

if b2.isEmpty():
   print("The box2 is empty!")

