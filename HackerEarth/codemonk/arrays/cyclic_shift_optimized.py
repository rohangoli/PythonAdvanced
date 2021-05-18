for iter in range(int(input())):
    (N,K) = list(map(int, input().strip().split()))
    arr = input()
    arr_max = arr
    result = 0
    i=0
    kcount=0
    mult_arr = [0] * N
    while i<N:
        arr = arr[1:]+arr[0]
        # print(arr)
        if arr > arr_max:
            arr_max = arr
            result = (i+1)
            #kcount = 1
        i+=1
    # print("max: {}, result: {}".format(arr_max,result))
    # bmax = bin(arr_max)[2:]
    # print(bmax)
    mult_arr[result-1] = 1
    
    arr = arr_max
    itercount = 0
    mult_iter = result
    while mult_iter<N:
        arr = arr[1:]+arr[0]
        if arr == arr_max:
            mult_arr[mult_iter]=1
        mult_iter+=1
    # print(mult_arr)
    result += (N/mult_arr.count(1)) * (K-1)
    print(int(result))
    
    # while kcount<K :
    #     arr = arr[1:]+arr[0]
    #     itercount +=1
    #     print(arr,itercount,sep=' ')
    #     if arr == arr_max:
    #         result += itercount
    #         kcount +=1
    #         print(result,kcount,sep=' ')
    #         itercount=0
    # print(result)
