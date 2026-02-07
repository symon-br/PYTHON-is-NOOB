#Functions definition
def calc_Sum(a, b): #Parameters
    return a + b

sum = calc_Sum(1, 4) #Function call with Arguments
print(sum)

# Function is made to reduce the code redundancy and to make the code more modular and reusable.


def No_params():
    print(" ") #Free space; can write anything here.

y= No_params() #Function call without arguments 
print(y) #This will print None because the function does not return anything.


# Question 1

def ave(a, b, c): 
    sum = a + b + c
    average = sum / 3
    print(average) #This will print the average but the function will not return anything, so it will return None by default. If we want to return the average, we should use return statement instead of print statement.
    return average #Only return; no print 

# print(ave(1, 2, 3)) #IN decimal points
# print(int(ave(1, 2, 3))) #IN whole number

ave(1, 1, 1) #Function call

