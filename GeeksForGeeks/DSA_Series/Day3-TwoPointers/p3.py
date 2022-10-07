## Dam of Candies

def maxCandy(height, n): 
    # Your code goes here
    i=0
    j=n-1
    maxArea = 0
    while i<j:
        width = j-i-1
        length = min(height[i],height[j])
        maxArea = max(maxArea, width*length)
        
        if height[i]<height[j]:
            i+=1
        else:
            j-=1
            
    return maxArea

test_cases = [
    ([1,3,4],3),
    ([2, 1, 3, 4, 6, 5],6),
    ([2, 1, 3, 4, 6, 5, 3],7,)
    ]
for x,y in test_cases:
    print(maxCandy(x,y))