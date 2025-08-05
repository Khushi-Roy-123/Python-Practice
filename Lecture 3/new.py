 #List (mutable)and tuple (immutable)are different things 

 #list
a =[1,2,3]
type(a)   
list.pop(1)                 #removes the data at index 1
list.remove(1)              #removes the fisrt occurence of the data
list.append(2)              #add data at the end of list
list.sort(reverse = True)   #list in descendig order
list.sort(reverse = False)  #list in ascendig order
list.insert(0,5)            #insert(index,data to insert)
print(a[0:3])               #Slicing is possible for list

#tuple
b=(x,y,z)                   #type(b)=tuple
c=(3,)                      #type(c)=tuple
print(b[0:3])               #Slicing is possible for tuple also
b.index(y)                  #gives the index of forst occurence of data
b.count(y)                  #counts the total occurence of data  


d=("hi")        # type = string 
e=(3)           # type = integer 

#Practice ques
#Ques1
a=input("Enter name of favourite movie:")
b=input("Enter name of favourite movie:")
c=input("Enter name of favourite movie:")
list=[a,b,c]
print(list)

#Ques2 
#Palindrome= jo samne se aur last se bilkul same hota hai
a= list(input("enter the list "))
b= a.copy()
b.reverse()
if (b == a):
    print("It's a Palindrome")
else:
    print("It's not a Palindrome")

#Ques3
list=["C","D","A","A","B","B","A"]
list.sort(reverse=False)
print(list)
