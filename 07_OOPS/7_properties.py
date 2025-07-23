# class Product:
#     def __init__(self,price):
#         self.set_price(price)

#     def get_price(self):
#         return self.__price

#     def set_price(self,val):
#         if val<0:
#             raise ValueError("Price can't be negative")
#         self.__price = val
# this is what java devs do (unpythonic)

class Product:
    def __init__(self,price):
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter    # if we comment this property out we will get a read only property
    def price(self,val):
        if val<0:
            raise ValueError("Price can't be negative")
        self.__price = val

    # price = property(get_price,set_price)  # better is to use decorators


product = Product(10)
print(product.price)
# product.price = -1