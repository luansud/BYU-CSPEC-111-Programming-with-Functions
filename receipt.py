from datetime import datetime

def main():
    try:
        products_dict = read_dictionary("products.csv",0)
        print("\nInkom Emporium")
        price = 0
        subtotal = 0
        total = 0
        items = 0
        tax = 0
        with open("request.csv") as request:
            next(request)
            for line in request:
                line = line.strip()
                cod, quantity = line.split(",")
                if cod in products_dict.keys():
                    full_product = products_dict[cod]
                    price = float(full_product[2])
                    quantity = int(quantity)
                    print(f"{full_product[1]}: {quantity} ${price:.2f}")
                    items += 1
                    subtotal += price*quantity
                 
                            
        tax = subtotal*0.06
        total = subtotal+tax
        current_date = datetime.now()
        day = datetime.today().strftime('%A')
        wed_discount = total-(total*0.10)
        print(f"\nNumber of Items: {items}")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Sales Tax: ${tax:.2f}")
        if day == "Friday":
            print(f"Wednesday Discount: -${(total*0.10):.2f}")
            print(f"Total: ${wed_discount:.2f}")
        else:
            print(f"Total: ${total:.2f}")
        print(f"\nThank you for shopping at the Inkom Emporium.")
        print(f"{current_date:%A %B %d %I:%M:%S %p %Y}")
    
    
    except FileNotFoundError as file_error:
        print(file_error)
    except PermissionError as perm_error:
        print(perm_error)
    except KeyError as key_error:
        print(key_error)
     

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