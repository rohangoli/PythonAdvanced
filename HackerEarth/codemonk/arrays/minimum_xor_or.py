for iter in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    i=0
    result = arr[0] ^ arr[1]
    while i<N-1:
        curval = arr[i] ^ arr[i+1]
        if curval < result:
            result = curval
        # j=i+1
        # while j<N:
        #     #curval = (arr[i] & arr[j]) ^ (arr[i] | arr[j])
        #     curval = arr[i] ^ arr[j]
        #     if curval < result:
        #         result = curval
        #     j+=1
        i+=1
    print(result)
