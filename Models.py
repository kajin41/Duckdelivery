import random
import Config



class Location:
    def __init__(self, name):
        self.name = name
        self.lat = random.uniform(40.738178, 40.754353)
        self.lon = random.uniform(-74.042851, -74.024468)

class User:
    def __init__(self, name):
        self.id = Config.newUserIndex + 1
        Config.newUserIndex = self.id
        self.name = name


class Order:
    def __init__(self, start, end, orderer, deliverer, item, store, cost, fee, paymentmethod):
        import random
        import string
        self.id = Config.newOrderIndex + 1
        Config.newOrderIndex = self.id
        self.start = start
        self.end = end
        self.orderer = orderer
        self.deliverer = deliverer
        self.item = item
        self.store = store
        self.cost = cost
        self.fee = fee
        self.paymentmethod = paymentmethod
        self.confirmationId = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6)) # creates a random 6 char confirmation code
        self.complete = False


def init_data():
    nullUser = User('null')
    u2 = User('Greg Mercado')
    u3 = User('Orange Joe')
    Config.users = {str(nullUser.id): nullUser, str(u2.id): u2, str(u3.id): u3}

    o1 = Order(Location('Pizza Planet'), Location('Apartment A'), u2.id, nullUser.id, 'Pizza', 'Pizza Planet', 16, 2, 1)
    o2 = Order(Location('The Wash'), Location('Apartment B'), u2.id, nullUser.id, 'Dry Cleaning #5437', 'The Wash', 0, 2, 1)
    o3 = Order(Location('Jack Hardware'), Location('Apartment C'), u2.id, nullUser.id, 'Nails', 'Jack Hardware', 4, 2, 1)
    Config.orders = {str(o1.id): o1, str(o2.id): o2, str(o3.id): o3}
    print('01', o1.confirmationId)
    print('02', o2.confirmationId)
    print('03', o3.confirmationId)
