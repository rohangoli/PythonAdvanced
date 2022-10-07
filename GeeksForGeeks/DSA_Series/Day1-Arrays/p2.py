## Convert array into Zig-Zag fashion

from cgi import test


def zigZag(arr, n):
    # code here
    i=0
    while i<len(arr)-1:
        if i%2==0:
            if not arr[i]<arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
        else:
            if not arr[i+1]<arr[i]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
                
        i+=1
    
    return arr

test_cases = [([4, 3, 7, 8, 6, 2, 1],7),([1,4,3,2],4),([1,8,5,3,2,9,4,6,7],9)]
for x,y in test_cases:
    print(zigZag(x,y))