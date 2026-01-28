class cattos():
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(f"{self.name} is {age} years old")

    def sleep(self,sleep_time):
        print("go to bed")

    def meow(self):
        print("meow")

    def  calc_distance(self,time,speed):
        distance=time*speed
        if distance<10:
            print("catto is far away :<")
        else:
            print(f"catto is close :3")
        return distance