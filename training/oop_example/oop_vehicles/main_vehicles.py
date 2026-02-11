from training.oop_example.oop_vehicles.vehicles import vehicles_parents
from training.oop_example.oop_vehicles.cars import cars
from training.oop_example.oop_vehicles.trucks import trucks


class vehicles:
    car1 = cars("tesla", "electric", 170000, 1.18, 30, 15)
    car2 = cars("toyota", "gas", 110000, 1.18, 40, 12)
    truck1 = trucks("honda", 8, 150000, 1.18, 100, 20)

    car1.current_battery_check()
    car1_price=car1.price_calculator()
    truck_price=truck1.price_calculator()

    # if car1.price_calculator() > truck1.price_calculator():
    #     difference = car1.price_calculator() - truck1.price_calculator()
    #     print(f"the car is more expensive by {difference} nis")
    # elif car1.price_calculator() < truck1.price_calculator():
    #     difference = truck1.price_calculator() - car1.price_calculator()
    #     print(f"the truck is more expensive by {difference} nis")
    # else:
    #     print("both vehicles cost the same amount")
    if car1_price > truck_price:
        difference =car1_price - truck_price
        print(f"the car is more expensive by {difference} nis")
    elif car1_price <truck_price:
        difference = truck_price - car1_price
        print(f"the truck is more expensive by {difference} nis")
    else:
        print("both vehicles cost the same amount")

    prices=[80,90,110]
    car1.price_avg_calc(prices)