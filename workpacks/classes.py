class BaseWorkPack:
    def __init__(self, wrkpacknum, wrkpacklinenum, wrkpacklineclass, wrkpackproject, wrkpacklead, wrkpackzone):
        self.workpacknumber = wrkpacknum
        self.workpacklinenumber = wrkpacklinenum
        self.workpacklineclass = wrkpacklineclass
        self.workpackproject = wrkpackproject
        self.workpacklead = wrkpacklead
        self.workpackzone = wrkpackzone

    def load_workpack_from_db(self, wrkpack):
        self.workpack = wrkpack.objects.get(id=wrkpack.id)

    def edit_workpack(self):
        pass

    def delete_workpack(self):
        pass