## B. Basketball Together

# Input:
# 6 180
# 90 80 70 60 50 100
# Output:
# 2

(N,D) = map(int, input().split())
powers = list(map(int, input().split()))
powers.sort()

i=0
j=N-1
count=0
while i<j:
    #print('-'*20,'\n',powers[i],powers[j])
    teamP = powers[j]
    while D>=teamP:
        #print(teamP,powers[i],powers[j])
        teamP+=powers[j]
        #print(teamP)
        i+=1
    count+=1
    j-=1
print(count)