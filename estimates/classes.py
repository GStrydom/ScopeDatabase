
class EstimateTable:
    master_list = []

    def __init__(self):
        pass

    def filter_values_into_table(self, fws, dmls, inls, hcs, ccs):
        column_1101120 = ['11011', '3/4"', 0, 0, 0, 0, 0]
        column_1101125 = ['11011', '1"', 0, 0, 0, 0, 0]
        column_1101140 = ['11011', '1 1/2"', 0, 0, 0, 0, 0]
        column_1101150 = ['11011', '2"', 0, 0, 0, 0, 0]
        column_1101180 = ['11011', '3"', 0, 0, 0, 0, 0]
        column_11011100 = ['11011', '4"', 0, 0, 0, 0, 0]

        for fw in fws:
            if fw.lineclasses == '11011':
                if fw.diameter == '20':
                    column_1101120[2] += fw.numberoffieldwelds
                if fw.diameter == '25':
                    column_1101125[2] += fw.numberoffieldwelds
                if fw.diameter == '40':
                    column_1101140[2] += fw.numberoffieldwelds
                if fw.diameter == '50':
                    column_1101150[2] += fw.numberoffieldwelds
                if fw.diameter == '80':
                    column_1101180[2] += fw.numberoffieldwelds
                if fw.diameter == '100':
                    column_11011100[2] += fw.numberoffieldwelds

        for dml in dmls:
            if dml.lineclasses == '11011':
                if dml.diameter == '20':
                    column_1101120[3] += dml.demolength
                if dml.diameter == '25':
                    column_1101125[3] += dml.demolength
                if dml.diameter == '40"':
                    column_1101140[3] += dml.demolength
                if dml.diameter == '50':
                    column_1101150[3] += dml.demolength
                if dml.diameter == '80':
                    column_1101180[3] += dml.demolength
                if dml.diameter == '100':
                    column_11011100[3] += dml.demolength

        for inl in inls:
            if inl.lineclasses == '11011':
                if inl.diameter == '20':
                    column_1101120[4] += inl.installlength
                if inl.diameter == '25':
                    column_1101125[4] += inl.installlength
                if inl.diameter == '40':
                    column_1101140[4] += inl.installlength
                if inl.diameter == '50':
                    column_1101150[4] += inl.installlength
                if inl.diameter == '80':
                    column_1101180[4] += inl.installlength
                if inl.diameter == '100':
                    column_11011100[4] += inl.installlength

        for hc in hcs:
            if hc.lineclasses == '11011':
                if hc.diameter == '20':
                    column_1101120[5] += hc.numhotcuts
                if hc.diameter == '25':
                    column_1101125[5] += hc.numhotcuts
                if hc.diameter == '40':
                    column_1101140[5] += hc.numhotcuts
                if hc.diameter == '50':
                    column_1101150[5] += hc.numhotcuts
                if hc.diameter == '80':
                    column_1101180[5] += hc.numhotcuts
                if hc.diameter == '100':
                    column_11011100[5] += hc.numhotcuts

        for cc in ccs:
            if cc.lineclasses == '11011':
                if cc.diameter == '20':
                    column_1101120[6] += cc.numcoldcuts
                if cc.diameter == '25':
                    column_1101125[6] += cc.numcoldcuts
                if cc.diameter == '40':
                    column_1101140[6] += cc.numcoldcuts
                if cc.diameter == '50':
                    column_1101150[6] += cc.numcoldcuts
                if cc.diameter == '80':
                    column_1101180[6] += cc.numcoldcuts
                if cc.diameter == '100':
                    column_11011100[6] += cc.numcoldcuts

        EstimateTable.master_list.append(column_1101120)
        EstimateTable.master_list.append(column_1101125)
        EstimateTable.master_list.append(column_1101140)
        EstimateTable.master_list.append(column_1101150)
        EstimateTable.master_list.append(column_1101180)
        EstimateTable.master_list.append(column_11011100)
        return EstimateTable.master_list


class BaseEstimate(object):
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

    def edit_item(self):
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