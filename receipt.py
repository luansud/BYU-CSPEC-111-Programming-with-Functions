def main():
    products_dict = read_dictionary("products.csv")
    print(f"All Products \n{products_dict}")
    print("\nRequested Items")
    price = 0
    with open("request.csv") as request:
        next(request)
        for line in request:
            line = line.strip()
            cod, quantity = line.split(",")
            full_product = products_dict[cod]
            price = float(full_product[2])
            quantity = int(quantity)
            print(f"{full_product[1]}: {quantity} ${price:.2f}")
                

def read_dictionary(filename,key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    key_column_index = 0
    with open(filename) as products_list:
        next(products_list)
        products_dic = {}
        for line in products_list:
            line = line.replace("\n","")
            cod,name,price = line.split(",")
            compound_list = [cod,name,price]
            products_dic[cod] = compound_list

    return products_dic
        

if __name__ == "__main__":
    main()