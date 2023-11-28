from products import Product

class Store():
    def __init__(self, name):
        self.name = name
        self.product_list = []

# * add_product(self, new_product) 
# * - takes a product and adds it to the store
    def add_product(self, new_product):
        self.product_list.append(new_product)
        print(new_product.name)
        return self
# * sell_product(self, id) 
# * - remove the product from the store's list of products given the id 
# *  (assume id is the index of the product in the list) and print its info.
# * inflation(self, percent_increase) 
    def sell_pruduct(self, id):
        for i in range(len(self.product_list)):
            if self.product_list[i] == self.product_list[id]:
                self.product_list.pop(id)
                print(self.product_list)
                return self
            else:
                print("something went wrong")
                return self

# * - increases the price of each product by the percent_increase given 
# * (use the method you wrote in the Product class!)
    def price_increase(self, percent_change, is_increased):
        print(" ")
        print("price increase")
        for product in self.product_list:
            print(product.name)
            print(product.price)
        for product in self.product_list:
            product.update_price(percent_change, is_increased)
            print(product.name)
            print(f"after price change: {product.price}")
        return self
# * set_clearance(self, category, percent_discount) 
# * - updates all the products matching the given category
    def set_clearance(self, category, percent_discount):
        for product in self.product_list:
            if category == product.category:
                print(" ")
                x = product.price * percent_discount
                product.price -= x
                print(product.category)
                print(f"{product.name}")
                print(product.price)
            elif category != product.category:
                print(" ")
                print(product.category)
                print("no discount for you!")
            else:
                print("something went wrong")
# * by reducing the price by the percent_discount given 
# * (use the method you wrote in the Product class!)

shoes_outlet = Store("Nike Outlet")
nike_shoes = Product("nike running shoes",95, "running")
nike_hoodie = Product("nike hoodie", 125, "running")
nike_shirt =  Product("nike shirt", 25, "outwear")
shoes_outlet.add_product(nike_shoes).add_product(nike_hoodie).add_product(nike_shirt).set_clearance("running", 0.25)
