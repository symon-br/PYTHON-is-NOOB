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


#default parameters
def cal_para(a, b=2): #first parameter is not able to make default as when we call the function, we have to provide value for a and b (i.e. cal_para(1) while the value of a) and if we did def cal_para(a=1, b) then will return SyntaxError: as the default parameter should be at the end of the parameter list.

    print(a * b) #b is a default parameter
    return a * b

cal_para(1) #This will use the default value of b which is 2, so it will return 1*2=2
cal_para(1, 3) #This will override the default value of b and use


# Question 2
#WAF to print the length of the list.
country = ["India", "USA", "UK", "Australia", "Germany", "Nepal", "Bhutan", "Bangladesh", "Sri Lanka", "Pakistan"]

def cal(list):
    print(len(list))
    return len(list)

cal(country)
