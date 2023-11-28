class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

# * update_price(self, percent_change, is_increased) 
# * - updates the product's price. 
# * If is_increased is True, the price should increase 
# * by the percent_change provided. 
# * If False, the price should decrease by the percent_change provided.

    def update_price(self, percent_change, is_increased):
        print(" ")
        print("update Price")
        if is_increased == True:
            print("price increase")
            x = self.price * percent_change
            self.price += x
        elif  is_increased == False:
            print("price decrease")
            x = self.price * percent_change
            self.price -= x
        else:
            print("something went wrong")
        return self

    # * print_info(self) 
    # * - print the name of the product, its category, and its price.

    def print_info(self):
        print(" ")
        print("info")
        print(f"name: {self.name}")
        print(f"price: {self.price}")
        print(f"category: {self.category}")
        return self

# sweater = Product("nike", 95.00, "winter clothing")
# sweater.print_info().update_price(0.10, True).print_info().update_price(0.55, False).print_info()