## Bob at the Bank
# cook your dish here
t = int(input())
for _ in range(t):
    (w,x,y,z) = map(int, input().split())
    print(w+(x-y)*z)