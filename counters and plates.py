a restarent is organizing its kitchen each counter either hold a plate or be empty write a function to move all empty counters to the end of the array while maintain the order of plates, and of counters with the people
code:
lis=list(map(int,input().split()))
lis1=[]
lis2=[]
c=1
for i in lis:
    if(i==0):
         lis2.append(i)
         c=c+1
    else:
        lis1.append(i)
lis3=lis1+lis2
sum=0
for j in lis3:
    sum=sum+j
print("Number of counters:",c)
print("Number of plates:",sum)
    
