class Calc:
    
    def add(self, x: int, y: int):
        return x + y
    
    def subtract(self, x, y):
        return x - y
    
    def multiply(self, x, y):
        return x * y
    
    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        
        return x / y
    
    
def main():
    calc = Calc()

    print(calc.add(1, 2))
    print(calc.subtract(3, 2))
    print(calc.multiply(3, 4))
    print(calc.divide(2, 1))

if __name__ == '__main__':
    main()