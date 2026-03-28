


class Phone():
    apperance="screen"
    def __init__(self,battery,size,brand,shape,release):
        self.battery=battery
        self.size=size
        self.brand=brand
        self.shape=shape
        self.release=release
        print("the new object is created")
    
    def calling(self):
        print("lets have call together")
    




object1=Phone("4hrs","20cm","android","rectangle","2024")
object2=Phone("8hrs","25cm","apple","square","2022")
object3=Phone("10hrs","30cm","huawei","fliphone","2023")


print(object1.shape)
print(object2.battery)
object1.calling()
print(object3.apperance)