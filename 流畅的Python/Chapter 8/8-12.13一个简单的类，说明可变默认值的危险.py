class HauntedBus(object):
    def __init__(self, passengers=[]):
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


bus1 = HauntedBus(["Alice", "Bill"])
print(bus1.passengers)
bus1.pick("Charlie")
bus1.drop("Alice")
print(bus1.passengers)

bus2 = HauntedBus()
bus2.pick("Carrie")
print(bus2.passengers)
bus3 = HauntedBus()
print(bus3.passengers)
bus3.pick("Dave")
print(bus2.passengers)
