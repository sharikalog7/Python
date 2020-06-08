inp=int(input("enter a number"))
print(inp)
sum1=0
n=len(str(inp))

temp=inp
print("n",n)
for i in range(len(str(inp))):

        num=temp//10
        num=temp%10
        print(num)
        cube=num**n
        print(cube)
    
        temp=temp//10
        print(num)

        sum1=sum1+cube
        print(sum1)




if inp==sum1:
        print("yes its an armstrong")

else:
    print("not an armstrong")
