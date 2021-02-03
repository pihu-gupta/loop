i= int(input("enter number to check for armstrong number"))
og=i
sum=0
while i>0:
        sum=sum+(i%10)*(i%10)*(i%10)
        i=i//10
if og==sum:
    print("nuber is aemstrong")
else:
    print("number is not armstrong")
    