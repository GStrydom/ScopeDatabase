
class BaseEstimate:
    def __init__(self, lineclass, diameter, quantity):
        self.lineclass = lineclass
        self.diameter = diameter
        self.quantity = quantity


class FieldWeld(BaseEstimate):
    total_grind_prep = 0
    total_weld_weld = 0
    total_weld_fit = 0
    total_qc_checkup = 0

    def calculate_manhours(self, norm):
        cut_norm = norm.objects.filter(pipediameter__exact=self.diameter)[0].cut
        prep_norm = norm.objects.filter(pipediameter__exact=self.diameter)[0].prep
        number_of_fieldwelds = self.quantity
        welder_norm = norm.objects.filter(pipediameter__exact=self.diameter)[0].tackweldlesseighty
        self.grindprep_manhours = (cut_norm + prep_norm) * 2 * welder_norm * 1,
        self.weldweld_manhours = welder_norm * number_of_fieldwelds * 1,
        self.qc_fitupcheck = 1 * welder_norm
        if self.diameter < 4:
            self.weldfit_manhours = self.weldweld_manhours * 0.15
        else:
            self.weldfit_manhours = self.weldweld_manhours * 0.30

    def edit_fieldweld(self):
        pass

    def delete_fieldweld(self):
        pass

    def combine_if_same(self):
        pass


class DemoLength(BaseEstimate):
    total_rig_out_line_rigger = 0
    total_rig_out_line_fitter = 0
    total_rig_in_line_rigger = 0
    total_rig_in_line_fitter = 0

    def calculate_manhours(self, norm):
        rigger_norm1 = norm.objects.filter(pipediameter__exact=self.diameter)[0].handlemeternormshours
        rigger_norm2 = self.quantity
        self.rig_out_line_rigger_hours = rigger_norm1 * rigger_norm2
        self.rig_out_line_fitter_hours = self.rig_out_line_rigger_hours
        self.rig_in_line_rigger = self.rig_out_line_rigger_hours
        self.rig_in_line_fitter = self.rig_out_line_rigger_hours

    def edit_demolength(self):
        pass

    def delete_demolength(self):
        pass

    def combine_if_same(self):
        pass


class InstallLength(BaseEstimate):
    total_rig_in_line_rigger = 0
    total_rig_in_line_fitter = 0

    def calculate_manhours(self, norm):
        rigger_norm1 = norm.objects.filter(pipediameter__exact=self.diameter)[0].handlemeternormshours
        rigger_norm2 = self.quantity
        self.rig_in_line_riggers = rigger_norm1 * rigger_norm2
        self.rig_in_line_fitter = self.rig_in_line_riggers

    def edit_installlength(self):
        pass

    def delete_installlength(self):
        pass

    def combine_if_same(self):
        pass


class ColdCut(BaseEstimate):
    total_cold_cut_line = 0
    total_riggers_for_cold_cut = 0

    def calculate_manhours(self, norm):
        pass

    def edit_coldcut(self):
        pass

    def delete_coldcut(self):
        pass

    def combine_if_same(self):
        pass


class HotCut(BaseEstimate):
    total_hot_cut_line = 0
    total_riggers_for_hot_cut = 0

    def calculate_manhours(self, norm):
        pass

    def edit_hotcut(self):
        pass

    def delete_hotcut(self):
        pass

    def combine_if_same(self):
        pass