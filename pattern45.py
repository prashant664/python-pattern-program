n=int(input("enter the number of rows"))
for i in range(n):
    for j in range(i+1):
        k=ord("A")+i
        print(chr(k),end=" ")
    print()    