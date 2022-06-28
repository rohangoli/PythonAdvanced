# Maximum XOR of Two Numbers in an Array

# Example 1:
# Input: nums = [3,10,5,25,2,8]
# Output: 28
# Explanation: The maximum result is 5 XOR 25 = 28.

# Example 2:
# Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
# Output: 127
 
# Function to return the
# maximum xor
def max_xor( arr , n):
     
    maxx = 0
    mask = 0;
 
    se = set()
     
    for i in range(30, -1, -1):
         
        # set the i'th bit in mask
        # like 100000, 110000, 111000..
        mask |= (1 << i)
        newMaxx = maxx | (1 << i)
        print(i,mask, newMaxx, maxx)
     
        for i in range(n):
             
            # Just keep the prefix till
            # i'th bit neglecting all
            # the bit's after i'th bit
            se.add(arr[i] & mask)
        print(se)
 
        for prefix in se:
             
            # find two pair in set
            # such that a^b = newMaxx
            # which is the highest
            # possible bit can be obtained
            if (newMaxx ^ prefix) in se:
                maxx = newMaxx
                break
                 
        # clear the set for next
        # iteration
        se.clear()
        print('-'*5)
    return maxx
 
# Driver Code
arr = [ 25, 10, 2, 8, 5, 3 ]
n = len(arr)
print(max_xor(arr, n))