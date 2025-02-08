def add(n1, n2): 
    return n1 + n2 

def subtract(n1, n2): 
    return n1 - n2 

def multiply(n1, n2): 
    return n1 * n2 

def divide(n1, n2): 
    return n1 / n2 

def percentage(n1, n2): 
    return (n1 * n2) / 100 

print("Please select operation -\n"  
      "1. Add\n" 
      "2. Subtract\n"  
      "3. Multiply\n"  
      "4. Divide\n"
      "5. Percentage\n") 

select = input("Select operation from 1, 2, 3, 4, 5: ") 

n_1 = float(input("Enter first number: ")) 
n_2 = float(input("Enter second number: ")) 

if select == '1': 
    print(n_1, "+", n_2, "=", add(n_1, n_2)) 
elif select == '2': 
    print(n_1, "-", n_2, "=", subtract(n_1, n_2)) 
elif select == '3': 
    print(n_1, "*", n_2, "=", multiply(n_1, n_2)) 
elif select == '4': 
    if n_2 != 0:
        print(n_1, "/", n_2, "=", divide(n_1, n_2)) 
    else:
        print("Error! Division by zero is not allowed.")
elif select == '5': 
    print(n_1, "% of", n_2, "=", percentage(n_1, n_2)) 
else: 
    print("Invalid input")
