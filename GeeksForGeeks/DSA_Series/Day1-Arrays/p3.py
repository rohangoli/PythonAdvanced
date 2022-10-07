## Minimum number of jumps

def minJumps_NOT(arr, n):
    #code here
    i=0
    jumps = 0
    while i<n-1 and arr[i]!=0:
        #print('jump ',i)
        j=1
        jumpMax = arr[i]
        while j<arr[i] and (i+j)<n:
            jumpMax = max(jumpMax,arr[i+j])
            j+=1
        i+=jumpMax
        jumps+=1
        
    if i>=n-1:
        return jumps
    else:
        return -1

def minJumps(arr, n):
  # The number of jumps needed to reach the starting index is 0
  if (n <= 1):
    return 0
  
  # Return -1 if not possible to jump
  if (arr[0] == 0):
    return -1
  
  # initialization
  # stores all time the maximal reachable index in the array
  maxReach = arr[0] 
  # stores the amount of steps we can still take
  step = arr[0]
  # stores the amount of jumps necessary to reach that maximal reachable position
  jump = 1
  
  # Start traversing array
  
  for i in range(1, n):
    # Check if we have reached the end of the array
    if (i == n-1):
      return jump
  
    # updating maxReach
    maxReach = max(maxReach, i + arr[i])
  
    # we use a step to get to the current index
    step -= 1;
  
    # If no further steps left
    if (step == 0):
      # we must have used a jump
      jump += 1
       
      # Check if the current index / position or lesser index
      # is the maximum reach point from the previous indexes
      if(i >= maxReach):
        return -1
  
      # re-initialize the steps to the amount
      # of steps to reach maxReach from position i.
      step = maxReach - i;
  return -1

test_cases = [
    ([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9],11),
    ([1, 4, 3, 2, 6, 7],6),
    ([1,1,0,3,4],5),
    ([1,3,2,3,4],5),
    ([2,3,1,1,2,4,2,0,1,1],10),
    ([1,4,1,0,1,3,2,1,1,1,4], 11),
    ([0,1,1,1,1],5)
    ]
for x,y in test_cases:
    print(minJumps(x,y))