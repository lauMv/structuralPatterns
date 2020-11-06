from fabric import Component

class Socks (Component):
    
    def getCost(self):
        return 30

    def operation(self) -> str:
        return "Sock"