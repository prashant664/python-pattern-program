n=int(input("enter the number of rows"))
for i in range(n):
    for j in range(n):
        if  i==0 or i==j or j==(n-1):
            print("*",end="")
        else:
            print(end=" ")
    print()             