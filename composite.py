from typing import List
from fabric import Component

class Composite(Component):
    
    def __init__(self) -> None:
        self._children: List[Component] = []

    
    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Branch({'+'.join(results)})"

    def getCost(self) -> int:
        result = 0
        for child in self._children:
            result =  result + child.getCost()
        return (result)