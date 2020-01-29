"""
This program will print the Pattern taking the number of rows (n) as input from the user.
if the n=5
55555
54444
54333
54322
54321

"""
n= int(input("Enter the number of rows : "))
for i in range(n,0,-1):
    for j in range(n,0,-1):
        if i>j:
            print(i, end="")
        else:
            print(j, end="")
    print("")
        