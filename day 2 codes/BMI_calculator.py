#Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
h=float(height)
w=float(weight)
BMI=int(w/(h**2))
print(BMI)

