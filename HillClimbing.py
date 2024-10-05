from random import *
from math import *
import matplotlib.pyplot as plt
import numpy as np


# Function 1
def myFunction(x):
  if (x == 0):
    return 0
  elif ((log2(x) * 7) % 17) < (x % 13):
    return (x + log2(x))**3
  elif ((log2(x) * 5) % 23) < (x % 19):
    return (log2(x)*3)**3
  else:
    return (log2(x)**2) - x

# Function 2
# def myFunction(x):
#   return -1*x**2 + 5000*x + 10000




x_values = []

for i in range(10000):
  x_values.append(i)


spoint = randint(1,len(x_values)-2)
# print(spoint)


y_values = []

for x in x_values:
  y_values.append(myFunction(x))

# print(x_values)
# print(y_values)


def hillClimb(arr, start_index):
  lmax_index = start_index
  search_route = "none"
  
  if arr[lmax_index] < arr[lmax_index+1]: # Conditional statement that chooses the direction the search point moves
    if arr[lmax_index] < arr[lmax_index-1]: # Conditional statement used for choosing between left and right increasing directions
      search_route = "right" if arr[lmax_index + 1] >= arr[lmax_index - 1] else "left"
    else:
      search_route = 'right'
  elif arr[lmax_index] < arr[lmax_index-1]:
    search_route = 'left'
  else:
    return lmax_index, arr[lmax_index] # returns local max index and local max if function value of search point is greater than left and right points
  
  # print(search_route)
  while lmax_index > 0 and lmax_index < len(arr)-1: # Conditional loop for checking if search point does not meet either left or right x bounds
    # print(lmax_index)
    if search_route == 'right': # Conditional statement that moves the search point based on specified direction until local max is determined
      if arr[lmax_index] <= arr[lmax_index+1]:
        lmax_index += 1
      else:
        break # Exits out of loop if local max is found
    else:
      if arr[lmax_index] <= arr[lmax_index-1]:
        lmax_index -= 1
      else:
        break
  return lmax_index, arr[lmax_index] # returns local max index and local max






# Main Test Case
results = hillClimb(y_values, spoint)
print(f"Starting at a search value when x = {spoint}, the local maximum occurs at x = {results[0]} and the value of the function at that point is {results[1]}.")


# Alternate Test Cases
# print(hillClimb(y_values, 1701))
# print(hillClimb([6,5,5,5,4,3,2],5))
# print(hillClimb([2,5,5,5,4,3,2],5))



plt.plot(np.array(x_values), np.array(y_values))
plt.show()








