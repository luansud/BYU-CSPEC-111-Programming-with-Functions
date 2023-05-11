import math
from datetime import date

pi = math.pi

w = float(input("Enter the width of the tire in mm (ex 205):"))
a = float(input("Enter the aspect ratio of the tire (ex 60):"))
d = float(input("Enter the diameter of the wheel in inches (ex 15):"))
telefone = ""

current_time = date.today()

v = pi*w**2*a*(w*a+2540*d)/10000000000

print(f"The approximate volume is {v:.2f} liters")

costumer_buy = input("Do you want to buy this tire? (YES / NO)")

if costumer_buy.upper() == "YES":
    telefone = input("Please type your number: ")
else: print("It's ok, Thank you for talk with us.")
    
with open("volumes.txt","at") as volume_file:
    print(f"{current_time}, {w:.0f}, {a:.0f}, {d:.0f}, {v:.2f}  {telefone}", file=volume_file)
