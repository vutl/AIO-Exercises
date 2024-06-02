import math

def is_number ( n ) :
    try :
        float ( n ) # Type - casting the string to ‘float ‘.
                        # If string is not a valid ‘float ‘ ,
                        # it ’ll raise ‘ValueError ‘ exception
    except ValueError :
        return False
    return True

def compute_sigmoid(x):
    return 1 / (1 + math.e**(-x))

def compute_relu(x):
    if (x <= 0):
        return 0
    else:
        return x

def compute_elu(x):
    a = 0.01
    if (x <= 0):
        return a * (math.e**(-x) - 1)
    else:
        return x

def activation_function():
    x = input("Input x: ")
    if (is_number(x)):
        x = float(x)
        function = input("Input activation Function ( sigmoid | relu | elu ) : ")
        function = function.lower()
        if (function == "sigmoid"):
            print(f"sigmoid: f({x}) = {compute_sigmoid(x)}")
        
        elif (function == "relu"):
            print(f"relu: f({x}) = {compute_relu(x)}")
        
        elif (function == "elu"):
            print(f"elu: f({x}) = {compute_elu(x)}")
        
        else:
            print(f"{function} is not supported")
    
    else:
        print("x must be a number")


activation_function()