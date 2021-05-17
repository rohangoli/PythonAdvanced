for iter in range(int(input())):
    length=int(input())
    mat=[]
    i=0
    while i<length:
        mat.append(list(map(int,input().split())))
        i+=1
    #mat=list(map(int,mat))
    # print(mat)
    count=0
    i=0
    while i<length:
        j=0
        while j<length:
            p=i
            while p<length:
                q=j
                while q<length:
                    if mat[i][j]>mat[p][q]:
                        count+=1
                    q+=1
                p+=1
            j+=1
        i+=1
    print(count)
