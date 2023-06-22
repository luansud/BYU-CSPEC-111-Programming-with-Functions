with open("products.csv") as products_list:
        next(products_list)
        products_dic = {}
        for line in products_list:
            line = line.replace("\n","")
            cod,name,price = line.split(",")
            compound_list = [cod,name,price]
            products_dic[cod] = compound_list
            
print(products_dic)