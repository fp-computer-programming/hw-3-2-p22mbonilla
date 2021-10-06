# Author MB 10/04/2021

w = int(input("what is your weight: "))

if w >= 40:
    print("you are Extremely Obese")
elif w >= 30:
    print("you are Obese")
elif w >= 25:
    print("you are Overweight")
elif w >= 19:
    print("you are Healthy")
else:
    print("you are Underweight")
