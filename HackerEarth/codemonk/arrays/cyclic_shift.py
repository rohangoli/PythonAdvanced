for iter in range(int(input())):
    (N,K) = list(map(int, input().strip().split()))
    arr = input()
    arr_max = arr
    result = 0
    i=0
    kcount=0
    while i<N:
        arr = arr[1:]+arr[0]
        # print(arr)
        if arr > arr_max:
            arr_max = arr
            result = (i+1)
            kcount = 1
        i+=1
    arr = arr_max
    itercount = 0
    while kcount<K:
        arr = arr[1:]+arr[0]
        itercount +=1
        #print(arr,itercount,sep=' ')
        if arr == arr_max:
            result += itercount
            kcount +=1
            print(result,kcount,sep=' ')
            itercount=0
    print(result)
