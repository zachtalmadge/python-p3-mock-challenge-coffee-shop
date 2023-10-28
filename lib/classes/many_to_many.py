class Coffee:
    def __init__(self, name):
        self.name = name
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if not hasattr(self, 'name'):
            if isinstance(new_name, str) and len(new_name) >= 3:
                self._name = new_name
            else:
                raise Exception('Name must be at least 3 characters!')
        else:
            raise Exception('Cannot change the name after initialization!')
    
    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        return list(set([order.customer for order in self.orders()]))
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        
        prices = [order.price for order in Order.all]
        
        return sum(prices) / len(prices)
    

class Customer:
    def __init__(self, name):
        self.name = name
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and (len(new_name) >= 1 and len(new_name) <= 15):
            self._name = new_name
        else:
            raise Exception("Name must be a string and between 1 and 15 characters!")
        
    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        return list(set([order.coffee for order in self.orders()]))
    
    def create_order(self, coffee, price):
        order = Order(self, coffee, price)
        return order
    
    
class Order:
    
    all = []
    
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        type(self).all.append(self)
        
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        if hasattr(self, 'price'):
            raise Exception('Cannot change price')
        else:
            if isinstance(new_price, float) and (new_price >= 1.0 and new_price < 10.0):
                self._price = new_price
                
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, new_customer):
        if isinstance(new_customer, Customer):
            self._customer = new_customer
        else:
            raise Exception('You are wrong!')
        
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, new_coffee):
        if isinstance(new_coffee, Coffee):
            self._coffee = new_coffee
        else:
            raise Exception('You are wrong!')