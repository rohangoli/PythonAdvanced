for i in range(int(input())):
    (length,shift)=map(int,input().split())
    arr=list(map(int,input().split()))

    while shift>=length:
        shift=shift-length

    arr=arr[length-shift:]+arr[0:length-shift]
    i=0
    while i<length:
        print(arr[i],end =" ")
        i+=1
    print()
