class Calculator:
    
    @staticmethod        
    def add(a,b):            #static method
        return a+b
    
    @staticmethod
    def multiply(a,b):       #static method
        return a*b
    
    def divide(self,a,b):    #instance method
        return a/b
    
print("Result =",Calculator.add(2,3))
print("Result =",Calculator.multiply(2,3))

result1 = Calculator()
print("Result =",result1.divide(2,3))
