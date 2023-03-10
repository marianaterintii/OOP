# dynamic

class Box:
    
    #defalut behavior
    def __init__(self, value):
     self.value = value
    
   # HW2:
   #  add default < , >, ==, comparison methods __lt__, __gt__, __eg__ ---> overloading
   
    def __gt__(self, x):
       if (self.value > x.value):
          return "b1 is greater than b2"
       else:
          return "b2 is greater than b1"
       
    def __lt__(self, x):
       if (self.value < x.value):
          return "b1 is less than b2"
       else:
          return "b2 is less than b1"
    
    def __eq__(self, x):
       if (self.value == x.value):
          return "both are equal"
       else:
          return "not equal"

    # intended behavior
    def isEmpty(self):
       if self.value == None:
          return True
       else:
          return False
    
#################################
b1 = Box(5)
b2 = Box(1000)

if b1.isEmpty():
   print("The box1 is empty!")

if b2.isEmpty():
   print("The box2 is empty!")

print(b1>b2)
print(b1<b2)
print(b1==b2)
