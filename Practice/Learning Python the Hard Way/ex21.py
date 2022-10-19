def add(a,b):
    print(f"ADDING {a} + {b}")
    return a + b 

def subtract(a,b): 
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a,b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a,b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Lets do some math with just functions!")

age = add(30, 69)
height = subtract(787, 90)
weight = multiply(6, 95)
iq = divide(300, 1)

print(f"Age: {age}, Height: {height}, Weight: {weight}, iq: {iq}")


print("Here is a puzzle")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
           
print("That becomes: ", what, "Can you do it by hand?")

