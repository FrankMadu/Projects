def quickselect(A, k):

  def lomuto(left, right):
    p = A[right]
    i = left
    for j in range(left, right):
      if A[j] < p:
        A[i], A[j] = A[j], A[i]
        i += 1
    A[i], A[right] = A[right], A[i]


    if i+1 > k:
      return lomuto(left, i-1)
    elif i+1 < k:
      return lomuto(i+1, right)
    else:
      return A[i]
  return lomuto(0, len(A)-1)


from random import randint

def main():
  # A = []
  # n = 1000
  
  # for e in range(n):
  #   r = randint(1,10000)
  #   while r in A:
  #     r = randint(1,10000)
  
  #   A.append(r)
  
  A = [31, 55, 19, 13, 42, 6, 60, 36, 48, 24]
  print(A)
  
  
  k = int(input("\nEnter the order of the smallest element you would like to find: "))
  
  while k > len(A) or k <= 0:
    k = int(input("\nInvalid input. Enter the order of the smallest element you would like to find: "))
  
  
  print("\nThe "+str(k)+"th "+"smallest value is:", quickselect(A,k))
  

main()

