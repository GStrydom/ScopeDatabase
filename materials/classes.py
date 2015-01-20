from .models import Lineclass, Workpack
from materials.models import MaterialItem


class BasePrefabItem:
    def __init__(self, lineclass, diameter, name, quantity):
        self.lineclass = lineclass
        self.diameter = diameter
        self.name = name
        self.quantity = quantity


class BaseReinstateItem:
    def __init__(self, lineclass, diameter, name, quantity):
        self.lineclass = lineclass
        self.diameter = diameter
        self.name = name
        self.quantity = quantity


class BaseSpadingItem:
    def __init__(self, lineclass, diameter, name, quantity):
        self.lineclass = lineclass
        self.diameter = diameter
        self.name = name
        self.quantity = quantity