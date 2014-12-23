class BaseWorkPack:
    def __init__(self, wrkpacknum):
        self.workpacknumber = wrkpacknum

    def load_workpack_from_db(self, wrkpack):
        self.workpack = wrkpack.objects.get(id=wrkpack.id)

    def edit_workpack(self):
        pass

    def delete_workpack(self):
        pass