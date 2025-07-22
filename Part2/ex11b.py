def calculate(a, op,b):
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        if b == 0:
            return "Error"
        return a / b
    else:
        return "Error"
print(calculate(90, "+", 10)) 
print(calculate(90, "-", 10))  
print(calculate(90, "*", 10))  
print(calculate(10, "/", 0))
        
    
    