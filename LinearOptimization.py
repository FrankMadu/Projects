import numpy as np
from tabulate import tabulate

# Number of Variables
while True:
  try:
    n = int(input("Enter the number of variables for this problem: "))
    while n <= 0:
      n = int(input("Input must be a positive integer. Enter the number of variables for this problem: "))
    break
  except:
    print("Invalid input. Please try again.")

# Coefficient array of objective function
while True:
  try:
    c = list(map(float, input("Enter the coefficients for each variable of the objective function. Separate each value by a space: ").split()))
    # print(c)
    # print(len(c))
    
    while len(c) != n:
      print("The number of coefficients in the array does not match the number of variables. Please try again.")
      c = list(map(float, input("Enter the coefficients for each variable of the objective function. Separate each value by a space: ").split()))
    
    
    # print(c)
    break
  except:
    print("Invalid input. Please try again.")

# Square matrix for stating the constraints
while True:
  try:
    A_v = list(map(str, input("Enter the data for the square matrix stating the constraints. Separate each row with a semicolon: ").split(';')))
    
    # print(A_v)
    # print(len(A_v))
    
    A = []
    for v in A_v:
      row = list(map(float, v.split()))
      A.append(row)
      
    # print(A)
    row_count = len(A)
    column_count = len(A[0])
    # print("Rows: ", row_count)
    # print("Columns: ", column_count)
    
    row_equivalency = "yes"
    for i in range(row_count):
      if len(A[i]) != column_count:
        row_equivalency = "no"
        break
    
    while row_count != column_count or row_count != n or row_equivalency == "no":
      print("The matrix entered is not a square matrix or the dimensions don't match the number of variable. Please try again.")
      A_v = list(map(str, input("Enter the data for the square matrix stating the constraints. Separate each row with a semicolon: ").split(';')))
    
      # print(A_v)
      # print(len(A_v))
    
      A = []
      for v in A_v:
        row = list(map(float, v.split()))
        A.append(row)
    
      # print(A)
      row_count = len(A)
      column_count = len(A[0])
      # print("Rows: ", row_count)
      # print("Columns: ", column_count)
    
      row_equivalency = "yes"
      for i in range(row_count):
        if len(A[i]) != column_count:
          row_equivalency = "no"
          break
    break
  except:
    print("Invalid input. Please try again.")
    
    
# Coefficient array for constraint limits
while True:
  try:
    b = list(map(float, input("Enter the coefficients for the constraint limits. Separate each value by a space: ").split()))
    # print(b)
    # print(len(b))
    
    while len(b) != n:
      print("The number of coefficients in the array does not match the number of variables. Please try again.")
      b = list(map(float, input("Enter the coefficients for the constraint limits. Separate each value by a space: ").split()))
    
    # print(b)
    break
  except:
    print("Invalid input. Please try again.")
    

table_data = [] # Initiates table for the LP problem

# Creates the first row for the table
starting_row = ["Supply"]
for i in range(n):
  starting_row.append("Constraint {}".format(i+1))
starting_row.append("Profit")
table_data.append(starting_row)

# Creates the middle rows for the table
for i in range(n):
  middle_row = []
  middle_row.append("Variable {}".format(i+1))
  for e in A[i]:
    middle_row.append(e)
  middle_row.append(c[i])
  table_data.append(middle_row)

# Creates the last row for the table
ending_row = ["Availability"]
for e in b:
  ending_row.append(e)
table_data.append(ending_row)


# print(table_data)
# for arr in table_data:
#   for e in arr:
#     print(e, end = "  ")
#   print()


print("\nTable:")
print(tabulate(table_data, headers = 'firstrow', tablefmt = 'fancy_grid')) #Prints the table for the LP problem
print()
  

# Solo Options Calculations
solo_matrix = []
solo_profit = []

for i in range(n): # Loop for determining the optimum Solo solution based on the constraints
  min_val = 10**99 # Initializes minimum value of the variable for any given constraint
  for j in range(n): # Loops through each contraint for a variable and finds the smallest value
    try: # Used to check for errors in calculations (ex: Prevents error when dividing by 0)
      current_val = b[j]/A[i][j]
      if current_val < min_val: # Conditional statement for finding a new minimum variable value
        min_val = current_val
    except:
      print("Variable {} has no effect on Constrain {}. Calculations can't be made.".format(i+1,j+1))
  if min_val != 10**10: # Appends value of variable for any given solo option
    solo_matrix.append(min_val)
  else:
    min_val == 0
    solo_matrix.append(min_val)
  solo_profit.append(min_val*c[i]) # Appends the profit made for any given solo option


# print(solo_matrix)
# print(solo_profit)

for s in range(len(solo_matrix)): # Outputs the result of the solo calculations
  print("If only Variable {} is made, then there will be a profit of ${:.2f}. The number of units produced from Variable {} is {}.".format(s+1, solo_profit[s], s+1, solo_matrix[s]))


A_n = [] # Initializes properly formed square matrix
for j in range(n): # Loop for properly formatting (changing each row into a column) the matrix A to solve for optinum balance solution.
  A_row = []
  for i in range(n):
    A_row.append(A[i][j])
  A_n.append(A_row)

# print(A_n)

# Balanced Option Calculations
A = np.array(A_n)
inv_A = np.linalg.inv(A)
b = np.array(b)
c = np.array(c)
x = inv_A.dot(b)
balanced_profit = c.dot(x)

# print()
# print(x)
# print(balanced_profit)

print("The Balanced profit amount will be ${:.2f}. The optimal solution for the variable matrix is: {}".format(balanced_profit,x))

profit_matrix = []
profit_name = []
for l in range(len(solo_profit)):
  profit_matrix.append(solo_profit[l])
  profit_name.append("Solo Variable {}".format(l+1))
profit_matrix.append(balanced_profit)
profit_name.append("Balanced")

# print(profit_matrix)
# print(profit_name)

max_profit = 0
max_index = 0
for m in range(len(profit_matrix)):
  if profit_matrix[m] > max_profit:
    max_profit = profit_matrix[m]
    max_index = m

if max_profit > 0:
  print("\nThe best possible option for maximizing the profit is the {} option with a profit amount of ${:.2f}.".format(profit_name[max_index], max_profit))
else:
  print("There was no profit made from this LP problem.")



# Case 1

# Enter the number of variables for this problem: 2
# Enter the coefficients for each variable of the objective function. Separate each value by a space: 50 40
# Enter the data for the square matrix stating the constraints. Separate each row with a semicolon: 1 2;1.5 1
# Enter the coefficients for the constraint limits. Separate each value by a space: 750 1000

# Table:
# ╒══════════════╤════════════════╤════════════════╤══════════╕
# │ Supply       │   Constraint 1 │   Constraint 2 │   Profit │
# ╞══════════════╪════════════════╪════════════════╪══════════╡
# │ Variable 1   │            1   │              2 │       50 │
# ├──────────────┼────────────────┼────────────────┼──────────┤
# │ Variable 2   │            1.5 │              1 │       40 │
# ├──────────────┼────────────────┼────────────────┼──────────┤
# │ Availability │          750   │           1000 │          │
# ╘══════════════╧════════════════╧════════════════╧══════════╛

# If only Variable 1 is made, then there will be a profit of $25000.00. The number of units produced from Variable 1 is 500.0.
# If only Variable 2 is made, then there will be a profit of $20000.00. The number of units produced from Variable 2 is 500.0.
# The Balanced profit amount will be $28750.00. The optimal solution for the variable matrix is: [375. 250.]

# The best possible option for maximizing the profit is the Balanced option with a profit amount of $28750.00.



# Case 2

# Enter the number of variables for this problem: 3
# Enter the coefficients for each variable of the objective function. Separate each value by a space: 3000 2000 2000
# Enter the data for the square matrix stating the constraints. Separate each row with a semicolon: 2 1 8;4 2 0;5 4 3
# Enter the coefficients for the constraint limits. Separate each value by a space: 300 200 300

# Table:
# ╒══════════════╤════════════════╤════════════════╤════════════════╤══════════╕
# │ Supply       │   Constraint 1 │   Constraint 2 │   Constraint 3 │   Profit │
# ╞══════════════╪════════════════╪════════════════╪════════════════╪══════════╡
# │ Variable 1   │              2 │              1 │              8 │     3000 │
# ├──────────────┼────────────────┼────────────────┼────────────────┼──────────┤
# │ Variable 2   │              4 │              2 │              0 │     2000 │
# ├──────────────┼────────────────┼────────────────┼────────────────┼──────────┤
# │ Variable 3   │              5 │              4 │              3 │     2000 │
# ├──────────────┼────────────────┼────────────────┼────────────────┼──────────┤
# │ Availability │            300 │            200 │            300 │          │
# ╘══════════════╧════════════════╧════════════════╧════════════════╧══════════╛

# Variable 2 has no effect on Constrain 3. Calculations can't be made.
# If only Variable 1 is made, then there will be a profit of $112500.00. The number of units produced from Variable 1 is 37.5.
# If only Variable 2 is made, then there will be a profit of $150000.00. The number of units produced from Variable 2 is 75.0.
# If only Variable 3 is made, then there will be a profit of $100000.00. The number of units produced from Variable 3 is 50.0.
# The Balanced profit amount will be $183333.33. The optimal solution for the variable matrix is: [25.         20.83333333 33.33333333]

# The best possible option for maximizing the profit is the Balanced option with a profit amount of $183333.33.






