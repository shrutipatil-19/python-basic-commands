day_of_week = input("enter day of week :").lower()
print(day_of_week)

if day_of_week == "saturday" or day_of_week == "sunday": 
    print("i will learn live")
else:
    print("i will practice")  

num1= int(input("Enter first number:"))
num2=int(input("Enter second number:"))
choice = input("enterthe oprator (option + ,-,*, /) :")

if choice == "+":
    sum_of_num=num1+num2
    print("addition", sum_of_num)

elif choice == "-":
    diff_of_num = num1-num2
    print("addition", diff_of_num)
else:
    print("invalid")