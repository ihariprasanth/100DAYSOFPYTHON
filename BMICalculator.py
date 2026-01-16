#using f-string and a mathematical operations we build a bmi calculator

print("Welcome to the BMI Calculator!")
height=float(input("Enter your height in cm: "))
weight=float(input("Enter your weight in kg: "))
result=round(height/weight**2,2)
print(f"BMI : {result}")
#new method
