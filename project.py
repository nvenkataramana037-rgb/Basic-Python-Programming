mob_num=int(input("Enter Your Mobile Number:"))
smpl_otp=123
otp=int(input("Enter Your OTP:"))
if otp==smpl_otp:
    password=int(input("Enter Your Password:"))
    print("Login Successful Enjoy Your Orders😋...")
else:
    print("Wrong otp entered..!\nResend OTP")
    otp=int(input("Enter Your OTP Again:"))
    print("Login Failed.!")

print("Welcome to Food Delivery System🥘")
print("Choose Your Menu")
print("1. Tiffins  \n2. Meals  \n3. Juice Items  \n4. Snacks  \n5. Tea and Drinks")
choice = int(input("Enter your choice from menu: "))

if choice == 1:
    print("1. Dosa   2. Idli")
    item = int(input("Enter your item: "))
    if item == 1:
        print("Selected Dosa")
        print("Price: 100")
        q=int(input("Enter Quantity Req:"))
        print("Total Price: ",q*100)

    else:
        print("Selected Idli")
        print("Price: 50/-")
        q=int(input("enter quantity req:"))
        print("Total Price: ",q*50 )

elif choice == 2:
    print("1. Veg Meals  2. Non-Veg Meals")
    item = int(input("Select your item: "))
    if item == 1:
        print("Selected Veg Meals")
        print("Price: 220")
        q=int(input("Enter Quantity Req:"))
        print("Total Price: ",q*220)
    else:
        print("Selected Non-Veg Meals")
        print("Price: 320")
        q=int(input("Enter Quantity Req:"))
        print("Total Price: ",q*320)

elif choice == 3:
    print("1. Banana Juice  2. Grape Juice")
    choice_ = int(input("Enter your juice choice: "))
    if choice_ == 1:
        print("Selected Banana Juice")
        print("Price: 60")
        q=int(input("Enter Quantity Req:"))
        print("Total Price: ",q*60)
    else:
        print("Selected Grape Juice")
        print("Price: 80")
        q=int(input("Enter Quantity Req:"))
        print("Total Price: ",q*80)

elif choice == 4:
    print("Snacks  coming soon...")

elif choice == 5:
    print("Tea and Drinks  coming soon...")

else:
    print("Invalid choice! Please select from the menu.")
