# create product class store product name price and display product information
class Product:

    def __init__(self,product_name,product_price):
        self.product_name=product_name
        self.product_price=product_price
     
    def DisplayDetail(self):
        print(f"Product Name is: {self.product_name} and product price is: {self.product_price}")

ProductName=input("Enter your product name:")
ProductPrice=int(input("Enter your product price:"))

obj=Product(ProductName,ProductPrice)
obj.DisplayDetail()
