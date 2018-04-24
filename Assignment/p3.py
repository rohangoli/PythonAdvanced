'''Read from a text file and print highest occurances of words (Only Top 5).'''
x=open("p3sample.txt","r")
y=x.read()
z=y.split(' ')
d={}
for i in z:
    if i not in d:
        d[i]=0
    d[i]+=1
q=sorted(d,key=d.__getitem__)
print("Words with High occurence are")
for i in q[-5:][::-1]:
    print(i,"-",d[i])
x.close()
