for iter in range(int(input())):
    (N,K) = list(map(int, input().strip().split()))
    arr = input()
    # print(arr)
    arr_max = int(arr,2)
    result = 0
    i=0
    while i<N:
        arr = arr[1:]+arr[0]
        # print(arr)
        temp_arr = int(arr,2)
        if temp_arr > arr_max:
            arr_max = temp_arr
            result = i+1
        i+=1
    arr = bin(arr_max)[2:]
    # print(arr)
    # print("max: {}, result: {}".format(arr_max,result))
    i=0
    kcount = 1
    while i<N and kcount<K:
        prev=0
        arr = arr[1:]+arr[0]
        if arr == bin(arr_max)[2:]:
            kcount+=1
            result += (i+1)
        i+=1
    print(result)

