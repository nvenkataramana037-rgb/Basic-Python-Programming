
#1.Python program to print the name 
n="N.Venkata Ramana"
print(n)

#2.get the input from the user and print it 
name=input("Enter Your Name")
print(name)

#3.get input from the user and priont it (integer)
a=int(input("Enter the number1"))
b=int(input("enter the number2"))
print(a)
print(b)

#4.get input input from the user and add two numbers
num1=int(input("enter  first number"))
num2=int(input("enter  second number"))
sum=num1+num2
print(sum)

#5.get input from the useer and swap thge numjber by using 3rd variable
x=int(input("enter x value"))
y=int(input("enter y value "))
print("before swapping:",x)
print("before swapping:",y)
temp=x
x=y
y=temp
print("after swapping:",x)
print("after swapping:",y)

#6.concatenate first name and last name 
n1=input("enter first name")
n2=input("enter 2nd name")
n=n1+n2
print("after concatination:",n)

#7.python program to print premitive data types
a=10
b=1.2
c="Ramana"
d='A'
print("integer:",a)
print("Float:",b)
print("string:",c)
print("char:",d)
#8.python program to print non premitive datatypes
my_list=[1,2,3,4,5]
my_tup=(6,7,8,9)
my_set={2,4,6,8}
my_dic={"one":1,"two":2}
print(my_list)
print(my_tup)
print(my_set)
print(my_dic)
#9.pythonb program to print square of the number 
n=int(input("enter a number"))
z=n**2
print("square of a number:",z) 

#10.Average of the 3 numbers
num1=int(input("enter num1"))
num2=int(input("enter num2"))
num3=int(input("enter num3"))
a=(num1+num2+num3)/3
print(a)  


#11.python program to get user input and multiply it by 10
a=int(input("enter a value"))
b=a*10
print("Result:",b) 

#12.python program to convert minute into seconds
m=int(input("enter value in minutes:"))
sec=m*60
print(sec) 

#python proghram to floating point
a=float(input("enter a value:"))
b=float(input("enter b value"))
mul=a*b
print(mul) 

#13.python program to find largest of 3 numbers
num1=int(input("enter num1"))
num2=int(input("enter num2"))
num3=int(input("enter num3"))
largest=max(num1,num2,num3)
print(largest)

#14.sum of first n natural numbers
n = int(input("Enter a number: "))
sum = n * (n + 1) // 2
print("Sum of the first", n, "natural numbers is:", sum) 

#15.person appylying loan
pancard=input("enter pan number")
aadhar=int(input("enter aadhar num"))
cibil=int(input("enter cibil score"))
if cibil>=700:
    print("loan approved")
else:
    print("rejected") 
#16.arthimetic operators
a = int(input("enter a value"))
b = int(input("enter b value"))
print("addition of two number:", a + b)
print("sub of two number:", a - b)
print("mul of two number:", a * b)
print("div of two numbers:", a // b) 

#17.logical operators
a=16
b=12
print(a>0 and b>15)
print(a>15 or b<15)
print(not(a==10)) 

#18.python program to print positive and negative numbers
a=int(input("enter the num"))
if a>0:
    print("positive number")
elif a<0:
    print("negative number")
else:
    print("zero") 

#19.even or oidd number
a=int(input("enter the num"))
if a%2==0:
    print("even number")
else:
    print("odd number") 

#20.python program to check number divisdible by 5 and 11 
a=int(input("enter the num"))
if (a%5==0 and a%11==0):
    print("given number is div by both")
else:
    print("gievn number not divisible")
