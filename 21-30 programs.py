 

#21.python program to ghet bthe age details
n=int(input("enter the age "))
if n<10:
    print("Child")
elif (n>=10 and n<=21):
    print("Teenage")
else:
    print("Adult") 

#22.grade using marks
marks=int(input("enter the marks"))
if (marks>90): 
  print("Grade A")
  print("Excellent")
elif (marks>=70 and marks<=70):
  print("Grade B")
  print("Good")
elif (marks>=50 and marks<=70):
  print("Grade c")
  print("Average")
elif (marks>=40 and marks<=50):
  print("Grade D")
  print("Below Average")
else:
  print("Fail") 


#23.python program to check the day of the week
day=int(input("enter the day"))
if day==1:
    print("Monday")
elif(day==2):
    print("Tuesday")
elif(day==3):
    print("Wednesday")
elif(day==4):
    print("Thursday")
elif(day==5):
    print("Friday")
elif (day==6):
    print("Saturday")
elif (day==7):
    print("Sunday")
else:
    print("Invalid Option") 


#24.user name and password
user="Ramana"
password_1=1234
user_name=input("enter user name ")
if (user!=user_name):
    print("Enter correct user name")
    user_name=input("enter user name again ")
password=int(input("enter the password"))
if (password_1==password):
    print("Login Success")
else:
    print("login Failed")


#25.Pyhton programto devolope a calculator
a=int(input("enter a value"))
b=int(input("enter b value"))
print(" choice:    1.addition  2.subtraction 3.multiplicaion 4.division")
choice=int(input("enter your choice"))
if choice==1:
    print("Addition of two numbers")
    print(a+b)
if choice==2:
    print("Subtraction of two numbers")
    print(a-b)
if choice==3:
    print("Multiplication of two numbers")
    print(a*b)
if choice==4:
    print("Dvision of two numbers")
    print(a//b)

#26.no.of days in a month
month = int(input("Enter your month: "))
if month in (1, 3, 5, 7, 8, 10, 12):
    print("31 Days")
elif month in (4, 6, 9, 11):
    print("30 Days")
else:
    print("28/29 Days")


#27.pyhton program to check body temparature
temp=int(input("enter temp in celcius:"))
if temp==36:
    print("Body temp is normal")
elif temp>36:
    print("Fever")
elif temp<36:
    print("cold")
else:
    print("enter a valid temparature")


#28. sum of cubes of numbers
m = int(input("enter starting value"))
n = int(input("enter endimng value"))

if m > n:
    print(0)
else:
    total_sum = 0
    for i in range(m, n + 1):
        total_sum += i ** 3
    print(total_sum)

#29.voting eligibility
n=int(input("enter the age"))
if n>18:
    print("eligible for vote")
else:
    print("ineligible")

