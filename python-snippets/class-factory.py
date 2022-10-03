def apple_function():
    """Return an Apple class, built using the 
    class keyword"""
    class Apple(object):
        def __init__(self, color):
            self.color = color
  
        def getColor(self):
            return self.color
    return Apple
  
  
# invoking class factory function
Apple = apple_function()
appleObj = Apple('red')
print(appleObj.getColor())