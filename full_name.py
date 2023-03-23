full_name = input("What is your Full name?\n")
print(len(full_name))
if len(full_name) == 0:
        print("You haven't entered anything. please enter your Full name")
elif len(full_name) <= 3:
        print("You have entered less than 4 characters. Please make sure that you enter your name and surname")
elif len(full_name) >= 25:
        print("You have entererd more than 25 characters. Please make sure that you have only entered your full name.")
else:
        print("Thank you for entering your name.")