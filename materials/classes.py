from .models import Lineclass11011


class BasePrefabItem:
    def __init__(self, lineclass, diameter, name, quantity):
        self.lineclass = lineclass
        self.diameter = diameter
        self.name = name
        self.quantity = quantity

    def get_code(self, lineclass):
        if lineclass == '11011':
            self.code = Lineclass11011.objects.filter()

    def attach_to_workpack(self):
        pass

    def edit_item(self, itemid):
        pass

    def delete_item(self, itemid):
        pass


class BaseReinstateItem:
    def __init__(self, lineclass, diameter, name, quantity):
        self.lineclass = lineclass
        self.diameter = diameter
        self.name = name
        self.quantity = quantity

    def get_code(self, lineclass):
        if lineclass == '11011':
            self.code = Lineclass11011.objects.filter()

    def attach_to_workpack(self):
        pass

    def edit_item(self, itemid):
        pass

    def delete_item(self, itemid):
        pass


class BaseSpadingItem:
    def __init__(self, lineclass, diameter, name, quantity):
        self.lineclass = lineclass
        self.diameter = diameter
        self.name = name
        self.quantity = quantity

    def get_code(self, lineclass):
        if lineclass == '11011':
            self.code = Lineclass11011.objects.filter()

    def attach_to_workpack(self):
        pass

    def edit_item(self, itemid):
        pass

    def delete_item(self, itemid):
        pass