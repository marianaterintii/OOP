''' 
HW1: create the function "setContainerValue() to recieve args:
    1. the reference to class 
    2. a new integer value
    the function sets the valuee in side the class
    NOTE: the function should update is_empty to False

 HW2: create the function "unsetContainerValue()"<- args:
    1. the class reference
    the function sets the vlaue in side the class to None
    NOTE: the function should update is_empty to True

HW3: create the function printContainerValue() <-args:
    1. the class reference
    the function checks if the class Container is empty#if it's
    empty, it prints: "Container is empty
    if it has a value:"container<123>
    '''
#HW1:

class Container:        # cutie
    is_empty = True     # attribute tip boolen
    value    = None

def setContainerValue(container, new_value):
    container.is_empty = False
    container.value = new_value
    
container = Container() 
setContainerValue(container, 20)
print(container.value)
print(container.is_empty)
print("#"*20)

###################################################
#HW:2
class Container:        
    is_empty = False     
    value = 123

def unsetContainerValue(container):
    container.is_empty = True
    container.value = None

container = Container()
unsetContainerValue(container)
print(container.is_empty)
print(container.value)
print("#"*20)
###################################################
#HW:3
class Container:        
    value = 123

def printContainerValue(container):
    if container.value is None:
        print("Container is empty")
    else:
        print(f"Container: <{ container.value }>")

container = Container()
printContainerValue(container)
print("#"*20)
###################################################