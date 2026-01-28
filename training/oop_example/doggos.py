class doggos():
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(f"{self.name} is {age} years old")

    def sleep(self,sleep_time):
        print("go to bed")

    def awuf(self):
        print("awuf")

    def  calc_distance(self,time,speed):
        distance=time*speed
        if distance>10:
            print("doggo is far away :<")
        else:
            print(f"doggo is close :3")
        return distance