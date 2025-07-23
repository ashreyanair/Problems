class v:
    def __init__(self,brand,fuel):
        self.brand=brand
        self.fuel=fuel
    def display(self):
        print(f"brand {self.brand}")
        print(f"fuel {self.fuel}")
class car(v):
    def __init__(self,brand,fuel,model):
        super().__init__(brand,fuel)
        self.model=model
    def displaydet(self):
        self.display()
        print(f"model {self.model}")
c=car("toyota","omni","wagonr")

c.displaydet()