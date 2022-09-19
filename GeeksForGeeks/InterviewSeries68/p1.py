## Geeks hates too many 1s

def noConseBits(query : int) -> int:
    # code here
    bin_str = []
    while query:
        bin_str.append(query%2)
        query = query//2

    print(bin_str)    
    # i=0
    # while i<len(bin_str)-2:
    #     if bin_str[i:i+3]==[1,1,1]:
    #         bin_str[i]=0
    #     i+=1
    i=len(bin_str)-1
    while i>1:
        if bin_str[i-2:i+1]==[1,1,1]:
            bin_str[i-2]=0
        i-=1

    print(bin_str)

    decimal = 0
    i=0
    while i<len(bin_str):
        decimal += bin_str[i]*(2**i)
        i+=1
        
    return decimal

tc = [2,7,65,110,127,246]
for idx,val in enumerate(tc):
    print('Case{}: Original={}'.format(idx,val))
    print(noConseBits(val))