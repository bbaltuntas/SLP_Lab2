print("Welcome in Micheal's store")

try:
    product_name = input("Product name:")
    product_price = float(input("Product price:"))
    client_mail = input("Client mail:")
    client_phone = float(input("Client phone:"))
    gross_price = product_price * (23 / 100) + product_price
    print("Your basket:")
    print("name", "net price", "gross price", "email", "phone", sep="; ")
    print(product_name, product_price, gross_price, client_mail, client_phone,
          sep="; ")
except:
    print("Process interrupted. Bad data type. ")
