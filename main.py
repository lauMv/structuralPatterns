from Shoes import Shoes
from Socks import Socks
from fabric import Component
from composite import Composite

def client_code(component: Component) -> None:
    print(f"Compras: {component.operation()}", end="\n")
    print (f"Costo total: {component.getCost()}", end="\n")

def admin(component1: Component, component2: Component) -> None:
    if component1.is_composite():
        component1.add(component2)

    print(f"Compras: {component1.operation()}", end="")
    print(f"Costo total: {component1.getCost()}", end="")

if __name__ == "__main__":

    simple = Shoes()
    print("Cliente: Quiero un par de zapatos:")
    client_code(simple)
    print("\n")

    tree = Composite()

    branch1 = Composite()
    branch1.add(Shoes())
    branch1.add(Socks())

    branch2 = Composite()
    branch2.add(Socks())

    tree.add(branch1)
    tree.add(branch2)

    print("Cliente: Tengo una lista de pedidos para dos personas:")
    client_code(tree)
    print("\n")

    print("Admin: Quiero ver todas las compras:")
    admin(tree, simple)

   