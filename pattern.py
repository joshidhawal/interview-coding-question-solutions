n= int(input("Enter the number of rows : "))
for i in range(n,0,-1):
    for j in range(n,0,-1):
        if i>j:
            print(i, end="")
        else:
            print(j, end="")
    print("")
        