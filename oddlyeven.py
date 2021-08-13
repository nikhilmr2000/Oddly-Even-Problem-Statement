# Given a maximum of 100 digit numbers as input, find the difference between the sum of odd and even position digits


n=int(input())
b=str(n)
l=[]
p=0
m=0
for i in b:
    l.append(i)


for i,val in enumerate(l):
    if(i%2==0):
        p+=int(val)
    else:
        m+=int(val)


if(p>m):
    z=p-m
    print(z)
else:
    z=m-p
    print(z)
