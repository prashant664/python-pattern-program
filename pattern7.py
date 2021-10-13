n=int(input("enter the number of rows"))
for i in range(n):
    for j in range(n-i):
        print(i+1,end=" ")
    print()    