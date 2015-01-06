
class BaseEstimate:
    def __init__(self, lineclass, diameter, quantity):
        self.lineclass = lineclass
        self.diameter = diameter
        self.quantity = quantity


class FieldWeldManhours(BaseEstimate):
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
