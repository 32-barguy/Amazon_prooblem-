print("Welcome to Price comparing machine \n Developed by theetam inc")

userin = int(input("Please enter the price you found out on Flipkart\n>>>"))
userin_2 = int(input("Please enter the price you found out on Amazon\n>>>"))

if userin>userin_2:
    print("The product you found on Amazon is cheaper Sir!")
elif userin_2>userin:
    print("The product you found on Flipkart is cheaper sir ")