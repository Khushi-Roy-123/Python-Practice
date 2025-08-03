#Basics
print("hello world") 
name="khushi"
age =24
price=25.99

print("my name is", name)

#Arithmatic Operators
a=5
b=2.45
print(a+b)
print(a*b)
print(a-b)
print(a/b)
print(a%b)
print(a**b)

#Relational Operators
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)
print(a<b)

#Assignment Operators
num= 10
num += 10
print(num)

#Logical Operators
print(not False) #True
print(not (a>b)) #True

val1 = True
val2 = False
print(val1 and val2) #False
print(val1 or val2) #True
print(a==b or val2) #False

#Type Conversion
a=5        # if a="5" then error will occur since a= string. and string can not be added with float
b=2.45
sum = a+b # 5.0 + 4.25 = 6.25
print(sum)


#Type Caste 
c,d= 1,"2"  #only works when initial type can be fitted in final type
e= int(b)
add = c + e
print(add)

x= 3.14
x= str(x)
print(type(x))

#input()
name = input("Enter Your Name")
print("Welcome", name)  

number = input("Enter a number")  # input always change its data to string type
print(type(number), number)

marks = float(input("Enter marks"))  # we need to mention the type of data priorly
print(type(marks), marks)

#practice ques
#ques1
p= int(input("Enter a number"))
q= int(input("Enter other number"))
print("Sum of numbers is:", p+q)

#ques2
side = int(input("Enter side of Square"))
print("Area of square is:", side**2)

#ques3
m= float(input("Enter a number"))
n= float(input("Enter other number"))
print("average of numbers is", (m+n)/2)

#ques4
r= int(input("Enter a number"))
s= int(input("Enter other number"))
print(r >= s) 



