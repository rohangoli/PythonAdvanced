# cook your dish here
t = int(input())
for _ in range(t):
    (a,b,x,y) = map(float,input().split())
    speedA = a/x
    speedB = b/y
    if speedB>speedA:
        print("Bob")
    elif speedA>speedB:
        print("Alice")
    else:
        print("Equal")
    