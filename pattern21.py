n=int(input("enter the number of rows"))
for i in range(n):
    for j in range(n):
        if j==0 or j==i or i==(n-1):
            print("*",end="")
        else:
            print(end=" ")
    print()           