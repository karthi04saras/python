the function to accept two positive integers r and unit and a positive integer array "arr" of the sixe "n" as its argument or represents number of rat present in the area. "unit" is the amount of the food each rat consumes each ith element of array "arr" represents amount of ood presents in i+1 house number where 0 is <=i
code:
r=int(input("Enter the count the rat:"))
unit=2
mul=r*unit
lists=list(map(int,input().split()))
print(lists)
sum=0
c=0
for i in lists:
    sum=sum+i
    c+=1
    if(sum>=mul):
        print(sum)
        break
print(c)
