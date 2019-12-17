""" 
Have the function ABCheck(str) take the str parameter being passed and return the string true if the characters a and b are separated by exactly 3 places anywhere in the string at least once (ie. "lane borrowed" would result in true because there is exactly three characters between a and b). Otherwise return the string false.
Sample Test Cases

Input:"after badly"

Output:false

Input:"Laura sobs"

Output:true
"""

str=input()
str=str.replace(" ","")
print (str)

a=[]
b=[]
counter=0

for i in range(len(str)):
	if(str[i]=='a'):
		a.append(i)
	if(str[i]=='b'):
		b.append(i)


print "a is",a
print "b is",b

for i in a:
	for j in b:
		if(abs(i-j)==3):
			counter=counter+1

if (counter==0):
	print("false");
else:
	print("true");
