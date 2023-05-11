import math
number_itens = int(input("Enter the number of items: "))
itens_per_box =  int(input("Enter the number of items per box:"))

total_boxes = math.ceil(number_itens / itens_per_box)

print(f"For {number_itens}, packing {itens_per_box} items in each box, you will need {total_boxes} boxes.")