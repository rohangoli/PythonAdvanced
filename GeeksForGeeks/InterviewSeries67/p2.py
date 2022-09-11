## Common String

def commonString(s, t):
    #code here
    results = []
    
    m,n = len(s), len(t)
    
    # left match
    i=m-n
    j=n
    while i<m and j>-1:
        if s[i:]==t[:j]:
            results.append(s[:i]+s[i:]+t[j:])
        i+=1
        j-=1
        
    # right match
    i=n
    j=0
    while i>-1 and j<n:
        if t[j:]==s[:i]:
            results.append(t[:j]+t[j:]+s[i:])
        i-=1
        j+=1
        
    if len(results)==0:
        results.append(s+t)
        results.append(t+s)
    
    #print(results)
    # results.sort()
    results = sorted(results, key = lambda i: (len(i), i))
    print(results)

    return results[0]

print(commonString('asdfg','fghj'))
print(commonString('bacbab','aba'))
print(commonString('nylpas','lollypop'))
print(commonString('nylolly','lollynyl'))
print(commonString('doyjaatukloy','loydoy'))
print(commonString('yjaatukloy','loydoy'))
