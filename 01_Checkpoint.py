age = int(input("Please enter your age: "))
heart_rate = 220 - age
heart_rate_max = int(heart_rate*0.85)
heart_rate_min = int(heart_rate*0.65)

print(f"When you exercise to strengthen your heart, you should keep your heart rate between {heart_rate_min} and {heart_rate_max} beats per minute.")


