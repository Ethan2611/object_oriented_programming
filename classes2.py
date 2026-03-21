


class Family():
    last_name="Ibhanesebhor"
    def __init__(self,name,age,gender,height,relation):
        self.name=name
        self.age=age
        self.gender=gender
        self.height=height
        self.relation=relation
        print("the new object is created")
    
    def eating(self):
        print("lets have dinner together")
    




object1=Family("Ethan",14,"male",5.9,"son")
object2=Family("Amelia",11,"female",5.4,"daughter")
object3=Family("Maya",11,"female",5.4,"daughter")


print(object1.height)
print(object2.name)
object1.eating()
print(object3.last_name)