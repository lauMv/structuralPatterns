from fabric import Component

class Shoes (Component):
    
    def getCost(self):
        return 50

    def operation(self) -> str:
        return "Shoe"