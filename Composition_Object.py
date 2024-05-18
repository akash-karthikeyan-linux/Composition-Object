class Products:
    def __init__(self, name, price, dis_price):
        self.name = name
        self.price = price
        self.dis_price = dis_price
        self.saved_price = price - dis_price

    def get_product_details(self):
        print("Product: {}".format(self.name))
        print("Price: {}".format(self.price))
        print("Discount Price: {}".format(self.dis_price))
        print("You Saved: {}".format(self.saved_price))

    def get_deal_price(self):
        return self.dis_price


class ElectronicItem(Products):
    def __init__(self, name, price, dis_price, warranty_in_months):
        super().__init__(name, price, dis_price)
        self.warranty_in_months = warranty_in_months

    def get_product_details(self):
        super().get_product_details()
        print("Warranty in months: {}".format(self.warranty_in_months))


class GroceryItem(Products):
    def __init__(self, name, price, dis_price, expiry_date):
        super().__init__(name, price, dis_price)
        self.expiry_date = expiry_date

    def get_product_details(self):
        super().get_product_details()
        print("Expiry Date: {}".format(self.expiry_date))


class Order:
    def __init__(self):
        self.cart = []

    def add_item(self, product, quantity):
        self.cart.append((product, quantity))

    def display_order_details(self):
        for product, quantity in self.cart:
            product.get_product_details()
            print("Quantity: {} \n".format(quantity))

    def display_total_bill(self):
        total_bill = 0
        for name, quant in self.cart:
            price = name.get_deal_price() * quant
            total_bill += price
        return total_bill


tv = ElectronicItem("TV", 40000, 31000, 24)
milk = GroceryItem("Milk", 30, 28, "30/11/2021")

order = Order()
order.add_item(milk, 2)
order.add_item(tv, 5)
order.display_order_details()
print(order.display_total_bill())
