#Escape Sequence Character like \n
str1= "First line \n second line"
str2= "First line \t second line"
print(str1)
print(str2)  
a= "ques and"
b=" "
c=str("ans")
str ="apple"
print(a+b+c) 
print(len(a))
print(a[1])

#Slicing
print(a[:2])
print(a[0:len(a)])  
#print(str(-3:-1))  

str3="hi this is khushi"
print(str3.endswith("ushi"))
print(str3.capitalize)
print(str3.replace("hi","hello"))
print(str3.find("this"))
print(str3.count("is"))
print(str3.find("o"))

# if-elif-else statement
p= 33
q=int(input("Enter marks"))
if(p< q):
    print("pass")
elif(p>q):
     print("fail")
else:
     print("re-try")


x=["yes", "no"]
y=["yes", "no"]
z=x

print( x is z)
print( x is y)
print(x==y)
print( x is not z)
print( x is not y)
print( x != y)

for i in range(10):
	if i%2!=0:
		print("******")
	else:
		print("**")

#Nesting = if in if 
age= int(input("enter a numer"))
if (age>=18):
    if(age<=80):
        print ("can drive")
    else:
        print ("can not drive")
else:
    print ("can not drive")

#Practice Ques
#Ques1
a=int(input("enter a number"))
if (a%2 == 0):
    print("number is even")
else:
    print("number is odd")
    
#Ques2
a=int(input("enter a number"))
b=int(input("enter a number"))
c=int(input("enter a number"))
if (a>b and a>c):
    print(a, "is the greates number")
elif (b>c and b>a):
    print(b, "is the greatest number")
elif (c>b and c>a):
    print(c, "is the greatest number")
else:
    print("all are equal")

#Ques3
m=int(input("enter a number"))
if (m%7 == 0):
    print(m," is divisible by 7")
else:
    print(m,"is not divisible by 7")

 
    
          

   




