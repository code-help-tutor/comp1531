WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
class wholesaler():
    def __init__(self, fruit, price, quantities):
        self.__fruit = [fruit(fruit, price, quantities)]
        self.__order = [order(fruit, price, quantities)]

    def new_fruit(self, price, quantities):
        self.__fruit.append(fruit(fruit, price, quantities))

    def new_order(self, order):
        self.__order.append(order(order))

    def mostPrevOrder(self):
        return self.__order[0]

    def fulfilled(self, order):
        for i in self.__order:
            if i == order:
                for k in self.__fruit:
                    if k == order['fruit'] and k.check_remain >= order['quantities']:
                        return True
        return False

    def pending_order(self, order):
        for i in self.__order:
            if i == order:
                for k in self.__fruit:
                    if k == order['fruit'] and k.check_remain >= order['quantities']:
                        return True
        return False

class order():
    def __init__(self, fruit, price, quantities):
        self._order = [{'fruit': fruit, 'price': price, 'quantities': quantities}]

class fruit():
    def __init__(self, fruit, price, quantities):
        self.fruit = fruit
        self.price = price
        self.quantities = quantities

    def check_remain(self):
        return self.quantities

    def check_price(self):
        return self.price
    
    def update_quantity(self, new_quantities):
        self.quantities = new_quantities
        
    def update_price(self, new_price):
        self.price = new_price
