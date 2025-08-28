# 1. Create a variable named pi and store the value 22/7 in it.
#  Now check the data type of this variable. 

pi = 22/7
print(pi)              
print(type(pi))         



# 2. Create a variable called for and assign it a value 4. See what
#  happens and find out the reason behind the behavior that you
#  see. 

# for = 4  (for is a reserved keyword in Python (used for loops), so we cannot use it as a variable name.)


# 3. Store the principal amount, rate of interest, and time in
#  different variables and then calculate the Simple Interest for 3
#  years. Formula: Simple Interest = P x R x T / 100 


P = 10000   
R = 5       
T = 3       
SI = (P * R * T) / 100
print("Simple Interest:", SI)
