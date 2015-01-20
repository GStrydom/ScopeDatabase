
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
        column_11011150 = ['11011', '6"', 0, 0, 0, 0, 0]
        column_11011200 = ['11011', '8"', 0, 0, 0, 0, 0]
        column_11011250 = ['11011', '10"', 0, 0, 0, 0, 0]
        column_11011300 = ['11011', '12"', 0, 0, 0, 0, 0]
        column_11011350 = ['11011', '14"', 0, 0, 0, 0, 0]
        column_11011400 = ['11011', '16"', 0, 0, 0, 0, 0]

        column_1107120 = ['11071', '3/4"', 0, 0, 0, 0, 0]
        column_1107125 = ['11071', '1"', 0, 0, 0, 0, 0]
        column_1107140 = ['11071', '1 1/2"', 0, 0, 0, 0, 0]
        column_1107150 = ['11071', '2"', 0, 0, 0, 0, 0]
        column_1107180 = ['11071', '3"', 0, 0, 0, 0, 0]
        column_11071100 = ['11071', '4"', 0, 0, 0, 0, 0]
        column_11071150 = ['11071', '6"', 0, 0, 0, 0, 0]
        column_11071200 = ['11071', '8"', 0, 0, 0, 0, 0]
        column_11071250 = ['11071', '10"', 0, 0, 0, 0, 0]
        column_11071300 = ['11071', '12"', 0, 0, 0, 0, 0]
        column_11071350 = ['11071', '14"', 0, 0, 0, 0, 0]
        column_11071400 = ['11071', '16"', 0, 0, 0, 0, 0]

        column_1126120 = ['11261', '3/4"', 0, 0, 0, 0, 0]
        column_1126125 = ['11261', '1"', 0, 0, 0, 0, 0]
        column_1126140 = ['11261', '1 1/2"', 0, 0, 0, 0, 0]
        column_1126150 = ['11261', '2"', 0, 0, 0, 0, 0]
        column_1126180 = ['11261', '3"', 0, 0, 0, 0, 0]
        column_11261100 = ['11261', '4"', 0, 0, 0, 0, 0]
        column_11261150 = ['11261', '6"', 0, 0, 0, 0, 0]
        column_11261200 = ['11261', '8"', 0, 0, 0, 0, 0]
        column_11261250 = ['11261', '10"', 0, 0, 0, 0, 0]
        column_11261300 = ['11261', '12"', 0, 0, 0, 0, 0]
        column_11261350 = ['11261', '14"', 0, 0, 0, 0, 0]
        column_11261400 = ['11261', '16"', 0, 0, 0, 0, 0]

        column_3101120 = ['31011', '3/4"', 0, 0, 0, 0, 0]
        column_3101125 = ['31011', '1"', 0, 0, 0, 0, 0]
        column_3101140 = ['31011', '1 1/2"', 0, 0, 0, 0, 0]
        column_3101150 = ['31011', '2"', 0, 0, 0, 0, 0]
        column_3101180 = ['31011', '3"', 0, 0, 0, 0, 0]
        column_31011100 = ['31011', '4"', 0, 0, 0, 0, 0]
        column_31011150 = ['31011', '6"', 0, 0, 0, 0, 0]
        column_31011200 = ['31011', '8"', 0, 0, 0, 0, 0]
        column_31011250 = ['31011', '10"', 0, 0, 0, 0, 0]
        column_31011300 = ['31011', '12"', 0, 0, 0, 0, 0]
        column_31011350 = ['31011', '14"', 0, 0, 0, 0, 0]
        column_31011400 = ['31011', '16"', 0, 0, 0, 0, 0]

        column_3107120 = ['31071', '3/4"', 0, 0, 0, 0, 0]
        column_3107125 = ['31071', '1"', 0, 0, 0, 0, 0]
        column_3107140 = ['31071', '1 1/2"', 0, 0, 0, 0, 0]
        column_3107150 = ['31071', '2"', 0, 0, 0, 0, 0]
        column_3107180 = ['31071', '3"', 0, 0, 0, 0, 0]
        column_31071100 = ['31071', '4"', 0, 0, 0, 0, 0]
        column_31071150 = ['31071', '6"', 0, 0, 0, 0, 0]
        column_31071200 = ['31071', '8"', 0, 0, 0, 0, 0]
        column_31071250 = ['31071', '10"', 0, 0, 0, 0, 0]
        column_31071300 = ['31071', '12"', 0, 0, 0, 0, 0]
        column_31071350 = ['31071', '14"', 0, 0, 0, 0, 0]
        column_31071400 = ['31071', '16"', 0, 0, 0, 0, 0]

        column_3126120 = ['31261', '3/4"', 0, 0, 0, 0, 0]
        column_3126125 = ['31261', '1"', 0, 0, 0, 0, 0]
        column_3126140 = ['31261', '1 1/2"', 0, 0, 0, 0, 0]
        column_3126150 = ['31261', '2"', 0, 0, 0, 0, 0]
        column_3126180 = ['31261', '3"', 0, 0, 0, 0, 0]
        column_31261100 = ['31261', '4"', 0, 0, 0, 0, 0]
        column_31261150 = ['31261', '6"', 0, 0, 0, 0, 0]
        column_31261200 = ['31261', '8"', 0, 0, 0, 0, 0]
        column_31261250 = ['31261', '10"', 0, 0, 0, 0, 0]
        column_31261300 = ['31261', '12"', 0, 0, 0, 0, 0]
        column_31261350 = ['31261', '14"', 0, 0, 0, 0, 0]
        column_31261400 = ['31261', '16"', 0, 0, 0, 0, 0]

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

        for fw in fws:
            if fw.lineclasses == '11071':
                if fw.diameter == '20':
                    column_1107120[2] += fw.numberoffieldwelds
                if fw.diameter == '25':
                    column_1107125[2] += fw.numberoffieldwelds
                if fw.diameter == '40':
                    column_1107140[2] += fw.numberoffieldwelds
                if fw.diameter == '50':
                    column_1107150[2] += fw.numberoffieldwelds
                if fw.diameter == '80':
                    column_1107180[2] += fw.numberoffieldwelds
                if fw.diameter == '100':
                    column_11071100[2] += fw.numberoffieldwelds

        for dml in dmls:
            if dml.lineclasses == '11071':
                if dml.diameter == '20':
                    column_1107120[3] += dml.demolength
                if dml.diameter == '25':
                    column_1107125[3] += dml.demolength
                if dml.diameter == '40"':
                    column_1107140[3] += dml.demolength
                if dml.diameter == '50':
                    column_1107150[3] += dml.demolength
                if dml.diameter == '80':
                    column_1107180[3] += dml.demolength
                if dml.diameter == '100':
                    column_11071100[3] += dml.demolength

        for inl in inls:
            if inl.lineclasses == '11071':
                if inl.diameter == '20':
                    column_1107120[4] += inl.installlength
                if inl.diameter == '25':
                    column_1107125[4] += inl.installlength
                if inl.diameter == '40':
                    column_1107140[4] += inl.installlength
                if inl.diameter == '50':
                    column_1107150[4] += inl.installlength
                if inl.diameter == '80':
                    column_1107180[4] += inl.installlength
                if inl.diameter == '100':
                    column_11071100[4] += inl.installlength

        for hc in hcs:
            if hc.lineclasses == '11071':
                if hc.diameter == '20':
                    column_1107120[5] += hc.numhotcuts
                if hc.diameter == '25':
                    column_1107125[5] += hc.numhotcuts
                if hc.diameter == '40':
                    column_1107140[5] += hc.numhotcuts
                if hc.diameter == '50':
                    column_1107150[5] += hc.numhotcuts
                if hc.diameter == '80':
                    column_1107180[5] += hc.numhotcuts
                if hc.diameter == '100':
                    column_11071100[5] += hc.numhotcuts

        for cc in ccs:
            if cc.lineclasses == '11071':
                if cc.diameter == '20':
                    column_1107120[6] += cc.numcoldcuts
                if cc.diameter == '25':
                    column_1107125[6] += cc.numcoldcuts
                if cc.diameter == '40':
                    column_1107140[6] += cc.numcoldcuts
                if cc.diameter == '50':
                    column_1107150[6] += cc.numcoldcuts
                if cc.diameter == '80':
                    column_1107180[6] += cc.numcoldcuts
                if cc.diameter == '100':
                    column_11071100[6] += cc.numcoldcuts

        for fw in fws:
            if fw.lineclasses == '11261':
                if fw.diameter == '20':
                    column_1126120[2] += fw.numberoffieldwelds
                if fw.diameter == '25':
                    column_1126125[2] += fw.numberoffieldwelds
                if fw.diameter == '40':
                    column_1126140[2] += fw.numberoffieldwelds
                if fw.diameter == '50':
                    column_1126150[2] += fw.numberoffieldwelds
                if fw.diameter == '80':
                    column_1126180[2] += fw.numberoffieldwelds
                if fw.diameter == '100':
                    column_11261100[2] += fw.numberoffieldwelds

        for dml in dmls:
            if dml.lineclasses == '11261':
                if dml.diameter == '20':
                    column_1126120[3] += dml.demolength
                if dml.diameter == '25':
                    column_1126125[3] += dml.demolength
                if dml.diameter == '40"':
                    column_1126140[3] += dml.demolength
                if dml.diameter == '50':
                    column_1126150[3] += dml.demolength
                if dml.diameter == '80':
                    column_1126180[3] += dml.demolength
                if dml.diameter == '100':
                    column_11261100[3] += dml.demolength

        for inl in inls:
            if inl.lineclasses == '11261':
                if inl.diameter == '20':
                    column_1126120[4] += inl.installlength
                if inl.diameter == '25':
                    column_1126125[4] += inl.installlength
                if inl.diameter == '40':
                    column_1126140[4] += inl.installlength
                if inl.diameter == '50':
                    column_1126150[4] += inl.installlength
                if inl.diameter == '80':
                    column_1126180[4] += inl.installlength
                if inl.diameter == '100':
                    column_11261100[4] += inl.installlength

        for hc in hcs:
            if hc.lineclasses == '11261':
                if hc.diameter == '20':
                    column_1126120[5] += hc.numhotcuts
                if hc.diameter == '25':
                    column_1126125[5] += hc.numhotcuts
                if hc.diameter == '40':
                    column_1126140[5] += hc.numhotcuts
                if hc.diameter == '50':
                    column_1126150[5] += hc.numhotcuts
                if hc.diameter == '80':
                    column_1126180[5] += hc.numhotcuts
                if hc.diameter == '100':
                    column_11261100[5] += hc.numhotcuts

        for cc in ccs:
            if cc.lineclasses == '11261':
                if cc.diameter == '20':
                    column_1126120[6] += cc.numcoldcuts
                if cc.diameter == '25':
                    column_1126125[6] += cc.numcoldcuts
                if cc.diameter == '40':
                    column_1126140[6] += cc.numcoldcuts
                if cc.diameter == '50':
                    column_1126150[6] += cc.numcoldcuts
                if cc.diameter == '80':
                    column_1126180[6] += cc.numcoldcuts
                if cc.diameter == '100':
                    column_11261100[6] += cc.numcoldcuts

        EstimateTable.master_list.append(column_1101120)
        EstimateTable.master_list.append(column_1101125)
        EstimateTable.master_list.append(column_1101140)
        EstimateTable.master_list.append(column_1101150)
        EstimateTable.master_list.append(column_1101180)
        EstimateTable.master_list.append(column_11011100)
        EstimateTable.master_list.append(column_11011150)
        EstimateTable.master_list.append(column_11011200)
        EstimateTable.master_list.append(column_11011250)
        EstimateTable.master_list.append(column_11011300)
        EstimateTable.master_list.append(column_11011350)
        EstimateTable.master_list.append(column_11011400)
        EstimateTable.master_list.append(column_1107120)
        EstimateTable.master_list.append(column_1107125)
        EstimateTable.master_list.append(column_1107140)
        EstimateTable.master_list.append(column_1107150)
        EstimateTable.master_list.append(column_1107180)
        EstimateTable.master_list.append(column_11071100)
        EstimateTable.master_list.append(column_11071150)
        EstimateTable.master_list.append(column_11071200)
        EstimateTable.master_list.append(column_11071250)
        EstimateTable.master_list.append(column_11071300)
        EstimateTable.master_list.append(column_11071350)
        EstimateTable.master_list.append(column_11071400)
        return EstimateTable.master_list


class BaseEstimate(object):
    def __init__(self, lineclass, diameter, quantity):
        self.lineclass = lineclass
        self.diameter = diameter
        self.quantity = quantity


class FieldWeld(BaseEstimate):

    totalgrindprep = 0
    totalweldweld = 0
    totalweldfit = 0
    totalqcfitup = 0

    def calculate_manhours(self, norm):
        cut_norm = norm.objects.filter(dn__exact=self.diameter)[0].cut
        prep_norm = norm.objects.filter(dn__exact=self.diameter)[0].prep
        number_of_fieldwelds = self.quantity
        welder_norm = norm.objects.filter(dn__exact=self.diameter)[0].tackweldlesseighty
        self.grindprep_manhours = (cut_norm + prep_norm)
        self.grindprep_manhours *= 2
        self.grindprep_manhours *= welder_norm
        self.weldweld_manhours = welder_norm
        self.weldweld_manhours *= number_of_fieldwelds
        self.qc_fitupcheck = 1 * welder_norm
        if self.diameter < 4:
            self.weldfit_manhours = self.weldweld_manhours * 0.15
        else:
            self.weldfit_manhours = self.weldweld_manhours * 0.30
        FieldWeld.totalgrindprep += self.grindprep_manhours
        FieldWeld.totalweldweld += self.weldweld_manhours
        FieldWeld.totalweldfit += self.weldfit_manhours
        FieldWeld.totalqcfitup += self.qc_fitupcheck


class DemoLength(BaseEstimate):
    total_rig_out_line_rigger = 0
    total_rig_out_line_fitter = 0
    total_rig_in_line_rigger = 0
    total_rig_in_line_fitter = 0

    def calculate_manhours(self, norm):
        rigger_norm1 = norm.objects.filter(dn__exact=self.diameter)[0].handlemeternormshours
        rigger_norm2 = self.quantity
        self.rig_out_line_rigger_hours = rigger_norm1 * rigger_norm2
        self.rig_out_line_fitter_hours = self.rig_out_line_rigger_hours
        self.rig_in_line_rigger = self.rig_out_line_rigger_hours
        self.rig_in_line_fitter = self.rig_out_line_rigger_hours

        DemoLength.total_rig_out_line_rigger += self.total_rig_out_line_rigger
        DemoLength.total_rig_out_line_fitter += self.total_rig_out_line_fitter
        DemoLength.total_rig_in_line_rigger += self.rig_in_line_rigger
        DemoLength.total_rig_in_line_fitter += self.rig_in_line_fitter


class InstallLength(BaseEstimate):
    total_rig_in_line_rigger = 0
    total_rig_in_line_fitter = 0

    def calculate_manhours(self, norm):
        rigger_norm1 = norm.objects.filter(dn__exact=self.diameter)[0].handlemeternormshours
        rigger_norm2 = self.quantity
        self.rig_in_line_riggers = rigger_norm1 * rigger_norm2
        self.rig_in_line_fitter = self.rig_in_line_riggers

        InstallLength.total_rig_in_line_fitter += self.total_rig_in_line_fitter
        InstallLength.total_rig_in_line_rigger += self.total_rig_in_line_rigger


class ColdCut(BaseEstimate):
    total_cold_cut_line = 0
    total_riggers_for_cold_cut = 0

    def calculate_manhours(self, norm):
        pass


class HotCut(BaseEstimate):
    total_hot_cut_line = 0
    total_riggers_for_hot_cut = 0

    def calculate_manhours(self, norm):
        pass


class FlangePT(BaseEstimate):

    def calculate_manhours(self, norm):
        pass