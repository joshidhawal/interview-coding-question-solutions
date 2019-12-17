"""
Have the function ThreeFiveMultiples(num) return the sum of all the multiples of 3 and 5 that are below num. For example: if num is 10, the multiples of 3 and 5 that are below 10 are 3, 5, 6, and 9, and adding them up you get 23, so your program should return 23. The integer being passed will be between 1 and 100.
Sample Test Cases

Input:6

Output:8

Input:1

Output:0


"""

num=int(input("Enter a number between 1 and 100\n"))

if (num>100 or num<0):
	print("enter a valid number")
else:

	sum=0
	for i in range(num):
		if (i%3==0 or i%5==0):
			sum=sum+i

	print(sum)
