from training.oop_example.oop_vehicles.vehicles import vehicles_parents


class cars(vehicles_parents):
    def __init__(self, brand, types, price, tax, fuel_max, fuel_used):
        self.brand = brand
        self.types = types
        self.price = price
        self.tax = tax
        self.fuel_max = fuel_max
        self.fuel_used = fuel_used

    def current_battery_check(self):
        if self.types == "electric":
            current_battery = self.fuel_max - self.fuel_used
            print(current_battery)
            return current_battery
        else:
            return "not an electric car"

    def price_avg_calc(self,prices):
        total_price = 0
        for price in prices:
            total_price = total_price +price
        avg=total_price/len(prices)
        print(f"the average price is {avg}")
        return avg