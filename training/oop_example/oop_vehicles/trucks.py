from training.oop_example.oop_vehicles.vehicles import vehicles_parents

class trucks(vehicles_parents):
    def __init__(self,brand,wheels_count,price,tax,speed,time):
        self.brand=brand
        self.wheels_count=wheels_count
        self.price=price
        self.tax=tax
        self.speed=speed
        self.time=time
    def calculate_distance(self):
        distance=self.speed * self.time
        return distance