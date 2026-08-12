
from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils import Calendar
import numpy as np
import os
import operator
import csv

class Dmgrashareincome(DataManagerMapped):
    def __init__(self, ):
        DataManagerMapped.__init__(self, )
        self.dataPath = None
        self.backfill = True
        self.report_period = NIO_MATRIX()
        self.statement_type = NIO_MATRIX()
        self.tot_oper_rev = NIO_MATRIX()
        self.oper_rev = NIO_MATRIX()
        self.int_inc = NIO_MATRIX()
        self.net_int_inc = NIO_MATRIX()
        self.insur_prem_unearned = NIO_MATRIX()
        self.handling_chrg_comm_inc = NIO_MATRIX()
        self.net_handling_chrg_comm_inc = NIO_MATRIX()
        self.net_inc_other_ops = NIO_MATRIX()
        self.plus_net_inc_other_bus = NIO_MATRIX()
        self.prem_inc = NIO_MATRIX()
        self.less_ceded_out_prem = NIO_MATRIX()
        self.chg_unearned_prem_res = NIO_MATRIX()
        self.incl_reinsurance_prem_inc = NIO_MATRIX()
        self.net_inc_sec_trading_brok_bus = NIO_MATRIX()
        self.net_inc_sec_uw_bus = NIO_MATRIX()
        self.net_inc_ec_asset_mgmt_bus = NIO_MATRIX()
        self.other_bus_inc = NIO_MATRIX()
        self.plus_net_gain_chg_fv = NIO_MATRIX()
        self.plus_net_invest_inc = NIO_MATRIX()
        self.incl_inc_invest_assoc_jv_entp = NIO_MATRIX()
        self.plus_net_gain_fx_trans = NIO_MATRIX()
        self.tot_oper_cost = NIO_MATRIX()
        self.less_oper_cost = NIO_MATRIX()
        self.less_int_exp = NIO_MATRIX()
        self.less_handling_chrg_comm_exp = NIO_MATRIX()
        self.less_taxes_surcharges_ops = NIO_MATRIX()
        self.less_selling_dist_exp = NIO_MATRIX()
        self.less_gerl_admin_exp = NIO_MATRIX()
        self.less_fin_exp = NIO_MATRIX()
        self.less_impair_loss_assets = NIO_MATRIX()
        self.prepay_surr = NIO_MATRIX()
        self.tot_claim_exp = NIO_MATRIX()
        self.chg_insur_cont_rsrv = NIO_MATRIX()
        self.dvd_exp_insured = NIO_MATRIX()
        self.reinsurance_exp = NIO_MATRIX()
        self.oper_exp = NIO_MATRIX()
        self.less_claim_recb_reinsurer = NIO_MATRIX()
        self.less_ins_rsrv_recb_reinsurer = NIO_MATRIX()
        self.less_exp_recb_reinsurer = NIO_MATRIX()
        self.other_bus_cost = NIO_MATRIX()
        self.oper_profit = NIO_MATRIX()
        self.plus_non_oper_rev = NIO_MATRIX()
        self.less_non_oper_exp = NIO_MATRIX()
        self.il_net_loss_disp_noncur_asset = NIO_MATRIX()
        self.tot_profit = NIO_MATRIX()
        self.inc_tax = NIO_MATRIX()
        self.unconfirmed_invest_loss = NIO_MATRIX()
        self.net_profit_incl_min_int_inc = NIO_MATRIX()
        self.net_profit_excl_min_int_inc = NIO_MATRIX()
        self.minority_int_inc = NIO_MATRIX()
        self.other_compreh_inc = NIO_MATRIX()
        self.tot_compreh_inc = NIO_MATRIX()
        self.tot_compreh_inc_parent_comp = NIO_MATRIX()
        self.tot_compreh_inc_min_shrhldr = NIO_MATRIX()
        self.ebit = NIO_MATRIX()
        self.ebitda = NIO_MATRIX()
        self.net_profit_after_ded_nr_lp = NIO_MATRIX()
        self.net_profit_under_intl_acc_sta = NIO_MATRIX()
        self.comp_type_code = NIO_MATRIX()
        self.s_fa_eps_basic = NIO_MATRIX()
        self.s_fa_eps_diluted = NIO_MATRIX()
        self.actual_ann_dt = NIO_MATRIX()
        self.insurance_expense = NIO_MATRIX()
        self.spe_bal_oper_profit = NIO_MATRIX()
        self.tot_bal_oper_profit = NIO_MATRIX()
        self.spe_bal_tot_profit = NIO_MATRIX()
        self.tot_bal_tot_profit = NIO_MATRIX()
        self.spe_bal_net_profit = NIO_MATRIX()
        self.tot_bal_net_profit = NIO_MATRIX()
        self.undistributed_profit = NIO_MATRIX()
        self.adjlossgain_prevyear = NIO_MATRIX()
        self.transfer_from_surplusreserve = NIO_MATRIX()
        self.transfer_from_housingimprest = NIO_MATRIX()
        self.transfer_from_others = NIO_MATRIX()
        self.distributable_profit = NIO_MATRIX()
        self.withdr_legalsurplus = NIO_MATRIX()
        self.withdr_legalpubwelfunds = NIO_MATRIX()
        self.workers_welfare = NIO_MATRIX()
        self.withdr_buzexpwelfare = NIO_MATRIX()
        self.withdr_reservefund = NIO_MATRIX()
        self.distributable_profit_shrhder = NIO_MATRIX()
        self.prfshare_dvd_payable = NIO_MATRIX()
        self.withdr_othersurpreserve = NIO_MATRIX()
        self.comshare_dvd_payable = NIO_MATRIX()
        self.capitalized_comstock_div = NIO_MATRIX()
        self.net_after_ded_nr_lp_correct = NIO_MATRIX()
        self.other_income = NIO_MATRIX()
        self.asset_disposal_income = NIO_MATRIX()
        self.continued_net_profit = NIO_MATRIX()
        self.end_net_profit = NIO_MATRIX()
        self.credit_impairment_loss = NIO_MATRIX()
        self.net_exposure_hedging_benefits = NIO_MATRIX()
        self.rd_expense = NIO_MATRIX()
        self.stmnote_finexp = NIO_MATRIX()
        self.fin_exp_int_inc = NIO_MATRIX()
        self.is_calculation = NIO_MATRIX()
        self.other_impair_loss_assets = NIO_MATRIX()
        self.tot_oper_cost2 = NIO_MATRIX()
        self.amodcost_fin_assets = NIO_MATRIX()
        self.tot_opt_inc_dif = NIO_MATRIX()
        self.tot_opt_cost_dif = NIO_MATRIX()
        return

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.dataPath = cfg.getAttributeString('dataPath')
        self.backfill = cfg.getAttributeDefault('backfill', True)
        self.addDailyData(self.report_period,self.tag + '.report_period')
        self.addDailyData(self.statement_type,self.tag + '.statement_type')
        self.addDailyData(self.tot_oper_rev,self.tag + '.tot_oper_rev')
        self.addDailyData(self.oper_rev,self.tag + '.oper_rev')
        self.addDailyData(self.int_inc,self.tag + '.int_inc')
        self.addDailyData(self.net_int_inc,self.tag + '.net_int_inc')
        self.addDailyData(self.insur_prem_unearned,self.tag + '.insur_prem_unearned')
        self.addDailyData(self.handling_chrg_comm_inc,self.tag + '.handling_chrg_comm_inc')
        self.addDailyData(self.net_handling_chrg_comm_inc,self.tag + '.net_handling_chrg_comm_inc')
        self.addDailyData(self.net_inc_other_ops,self.tag + '.net_inc_other_ops')
        self.addDailyData(self.plus_net_inc_other_bus,self.tag + '.plus_net_inc_other_bus')
        self.addDailyData(self.prem_inc,self.tag + '.prem_inc')
        self.addDailyData(self.less_ceded_out_prem,self.tag + '.less_ceded_out_prem')
        self.addDailyData(self.chg_unearned_prem_res,self.tag + '.chg_unearned_prem_res')
        self.addDailyData(self.incl_reinsurance_prem_inc,self.tag + '.incl_reinsurance_prem_inc')
        self.addDailyData(self.net_inc_sec_trading_brok_bus,self.tag + '.net_inc_sec_trading_brok_bus')
        self.addDailyData(self.net_inc_sec_uw_bus,self.tag + '.net_inc_sec_uw_bus')
        self.addDailyData(self.net_inc_ec_asset_mgmt_bus,self.tag + '.net_inc_ec_asset_mgmt_bus')
        self.addDailyData(self.other_bus_inc,self.tag + '.other_bus_inc')
        self.addDailyData(self.plus_net_gain_chg_fv,self.tag + '.plus_net_gain_chg_fv')
        self.addDailyData(self.plus_net_invest_inc,self.tag + '.plus_net_invest_inc')
        self.addDailyData(self.incl_inc_invest_assoc_jv_entp,self.tag + '.incl_inc_invest_assoc_jv_entp')
        self.addDailyData(self.plus_net_gain_fx_trans,self.tag + '.plus_net_gain_fx_trans')
        self.addDailyData(self.tot_oper_cost,self.tag + '.tot_oper_cost')
        self.addDailyData(self.less_oper_cost,self.tag + '.less_oper_cost')
        self.addDailyData(self.less_int_exp,self.tag + '.less_int_exp')
        self.addDailyData(self.less_handling_chrg_comm_exp,self.tag + '.less_handling_chrg_comm_exp')
        self.addDailyData(self.less_taxes_surcharges_ops,self.tag + '.less_taxes_surcharges_ops')
        self.addDailyData(self.less_selling_dist_exp,self.tag + '.less_selling_dist_exp')
        self.addDailyData(self.less_gerl_admin_exp,self.tag + '.less_gerl_admin_exp')
        self.addDailyData(self.less_fin_exp,self.tag + '.less_fin_exp')
        self.addDailyData(self.less_impair_loss_assets,self.tag + '.less_impair_loss_assets')
        self.addDailyData(self.prepay_surr,self.tag + '.prepay_surr')
        self.addDailyData(self.tot_claim_exp,self.tag + '.tot_claim_exp')
        self.addDailyData(self.chg_insur_cont_rsrv,self.tag + '.chg_insur_cont_rsrv')
        self.addDailyData(self.dvd_exp_insured,self.tag + '.dvd_exp_insured')
        self.addDailyData(self.reinsurance_exp,self.tag + '.reinsurance_exp')
        self.addDailyData(self.oper_exp,self.tag + '.oper_exp')
        self.addDailyData(self.less_claim_recb_reinsurer,self.tag + '.less_claim_recb_reinsurer')
        self.addDailyData(self.less_ins_rsrv_recb_reinsurer,self.tag + '.less_ins_rsrv_recb_reinsurer')
        self.addDailyData(self.less_exp_recb_reinsurer,self.tag + '.less_exp_recb_reinsurer')
        self.addDailyData(self.other_bus_cost,self.tag + '.other_bus_cost')
        self.addDailyData(self.oper_profit,self.tag + '.oper_profit')
        self.addDailyData(self.plus_non_oper_rev,self.tag + '.plus_non_oper_rev')
        self.addDailyData(self.less_non_oper_exp,self.tag + '.less_non_oper_exp')
        self.addDailyData(self.il_net_loss_disp_noncur_asset,self.tag + '.il_net_loss_disp_noncur_asset')
        self.addDailyData(self.tot_profit,self.tag + '.tot_profit')
        self.addDailyData(self.inc_tax,self.tag + '.inc_tax')
        self.addDailyData(self.unconfirmed_invest_loss,self.tag + '.unconfirmed_invest_loss')
        self.addDailyData(self.net_profit_incl_min_int_inc,self.tag + '.net_profit_incl_min_int_inc')
        self.addDailyData(self.net_profit_excl_min_int_inc,self.tag + '.net_profit_excl_min_int_inc')
        self.addDailyData(self.minority_int_inc,self.tag + '.minority_int_inc')
        self.addDailyData(self.other_compreh_inc,self.tag + '.other_compreh_inc')
        self.addDailyData(self.tot_compreh_inc,self.tag + '.tot_compreh_inc')
        self.addDailyData(self.tot_compreh_inc_parent_comp,self.tag + '.tot_compreh_inc_parent_comp')
        self.addDailyData(self.tot_compreh_inc_min_shrhldr,self.tag + '.tot_compreh_inc_min_shrhldr')
        self.addDailyData(self.ebit,self.tag + '.ebit')
        self.addDailyData(self.ebitda,self.tag + '.ebitda')
        self.addDailyData(self.net_profit_after_ded_nr_lp,self.tag + '.net_profit_after_ded_nr_lp')
        self.addDailyData(self.net_profit_under_intl_acc_sta,self.tag + '.net_profit_under_intl_acc_sta')
        self.addDailyData(self.comp_type_code,self.tag + '.comp_type_code')
        self.addDailyData(self.s_fa_eps_basic,self.tag + '.s_fa_eps_basic')
        self.addDailyData(self.s_fa_eps_diluted,self.tag + '.s_fa_eps_diluted')
        self.addDailyData(self.actual_ann_dt,self.tag + '.actual_ann_dt')
        self.addDailyData(self.insurance_expense,self.tag + '.insurance_expense')
        self.addDailyData(self.spe_bal_oper_profit,self.tag + '.spe_bal_oper_profit')
        self.addDailyData(self.tot_bal_oper_profit,self.tag + '.tot_bal_oper_profit')
        self.addDailyData(self.spe_bal_tot_profit,self.tag + '.spe_bal_tot_profit')
        self.addDailyData(self.tot_bal_tot_profit,self.tag + '.tot_bal_tot_profit')
        self.addDailyData(self.spe_bal_net_profit,self.tag + '.spe_bal_net_profit')
        self.addDailyData(self.tot_bal_net_profit,self.tag + '.tot_bal_net_profit')
        self.addDailyData(self.undistributed_profit,self.tag + '.undistributed_profit')
        self.addDailyData(self.adjlossgain_prevyear,self.tag + '.adjlossgain_prevyear')
        self.addDailyData(self.transfer_from_surplusreserve,self.tag + '.transfer_from_surplusreserve')
        self.addDailyData(self.transfer_from_housingimprest,self.tag + '.transfer_from_housingimprest')
        self.addDailyData(self.transfer_from_others,self.tag + '.transfer_from_others')
        self.addDailyData(self.distributable_profit,self.tag + '.distributable_profit')
        self.addDailyData(self.withdr_legalsurplus,self.tag + '.withdr_legalsurplus')
        self.addDailyData(self.withdr_legalpubwelfunds,self.tag + '.withdr_legalpubwelfunds')
        self.addDailyData(self.workers_welfare,self.tag + '.workers_welfare')
        self.addDailyData(self.withdr_buzexpwelfare,self.tag + '.withdr_buzexpwelfare')
        self.addDailyData(self.withdr_reservefund,self.tag + '.withdr_reservefund')
        self.addDailyData(self.distributable_profit_shrhder,self.tag + '.distributable_profit_shrhder')
        self.addDailyData(self.prfshare_dvd_payable,self.tag + '.prfshare_dvd_payable')
        self.addDailyData(self.withdr_othersurpreserve,self.tag + '.withdr_othersurpreserve')
        self.addDailyData(self.comshare_dvd_payable,self.tag + '.comshare_dvd_payable')
        self.addDailyData(self.capitalized_comstock_div,self.tag + '.capitalized_comstock_div')
        self.addDailyData(self.net_after_ded_nr_lp_correct,self.tag + '.net_after_ded_nr_lp_correct')
        self.addDailyData(self.other_income,self.tag + '.other_income')
        self.addDailyData(self.asset_disposal_income,self.tag + '.asset_disposal_income')
        self.addDailyData(self.continued_net_profit,self.tag + '.continued_net_profit')
        self.addDailyData(self.end_net_profit,self.tag + '.end_net_profit')
        self.addDailyData(self.credit_impairment_loss,self.tag + '.credit_impairment_loss')
        self.addDailyData(self.net_exposure_hedging_benefits,self.tag + '.net_exposure_hedging_benefits')
        self.addDailyData(self.rd_expense,self.tag + '.rd_expense')
        self.addDailyData(self.stmnote_finexp,self.tag + '.stmnote_finexp')
        self.addDailyData(self.fin_exp_int_inc,self.tag + '.fin_exp_int_inc')
        self.addDailyData(self.is_calculation,self.tag + '.is_calculation')
        self.addDailyData(self.other_impair_loss_assets,self.tag + '.other_impair_loss_assets')
        self.addDailyData(self.tot_oper_cost2,self.tag + '.tot_oper_cost2')
        self.addDailyData(self.amodcost_fin_assets,self.tag + '.amodcost_fin_assets')
        self.addDailyData(self.tot_opt_inc_dif,self.tag + '.tot_opt_inc_dif')
        self.addDailyData(self.tot_opt_cost_dif,self.tag + '.tot_opt_cost_dif')
        return

    def loadDay(self, di):
        self.fillnan(di)  # set default value
        if di == len(uv.Dates) - 1:
            return
        if di > 1 and self.backfill:  # backfill
            self.doBackfill(di)
        filepath = os.path.join(self.dataPath, '%d' % uv.Dates[di])
        if not os.path.isfile(filepath):
            print('[ %s ] %s missing on day %d' %  (self.tag, filepath, uv.Dates[di]))
            return
        infile = open(filepath, 'r')
        infile.readline() # skip title line
        updated = 0
        for line in infile:
            linespt = line.strip('\n').split(',')
            # a field could be blank if its value is missing
            linespt = [np.nan if x == '' else x for x in linespt]
            ticker = linespt[1][0:6]
            ii = uv.Instruments.lookup(ticker)
            if ii < 0:
                continue
            self.report_period[di, ii]  = float(linespt[4])
            self.statement_type[di, ii]  = float(linespt[5])
            self.tot_oper_rev[di, ii]  = float(linespt[6])
            self.oper_rev[di, ii]  = float(linespt[7])
            self.int_inc[di, ii]  = float(linespt[8])
            self.net_int_inc[di, ii]  = float(linespt[9])
            self.insur_prem_unearned[di, ii]  = float(linespt[10])
            self.handling_chrg_comm_inc[di, ii]  = float(linespt[11])
            self.net_handling_chrg_comm_inc[di, ii]  = float(linespt[12])
            self.net_inc_other_ops[di, ii]  = float(linespt[13])
            self.plus_net_inc_other_bus[di, ii]  = float(linespt[14])
            self.prem_inc[di, ii]  = float(linespt[15])
            self.less_ceded_out_prem[di, ii]  = float(linespt[16])
            self.chg_unearned_prem_res[di, ii]  = float(linespt[17])
            self.incl_reinsurance_prem_inc[di, ii]  = float(linespt[18])
            self.net_inc_sec_trading_brok_bus[di, ii]  = float(linespt[19])
            self.net_inc_sec_uw_bus[di, ii]  = float(linespt[20])
            self.net_inc_ec_asset_mgmt_bus[di, ii]  = float(linespt[21])
            self.other_bus_inc[di, ii]  = float(linespt[22])
            self.plus_net_gain_chg_fv[di, ii]  = float(linespt[23])
            self.plus_net_invest_inc[di, ii]  = float(linespt[24])
            self.incl_inc_invest_assoc_jv_entp[di, ii]  = float(linespt[25])
            self.plus_net_gain_fx_trans[di, ii]  = float(linespt[26])
            self.tot_oper_cost[di, ii]  = float(linespt[27])
            self.less_oper_cost[di, ii]  = float(linespt[28])
            self.less_int_exp[di, ii]  = float(linespt[29])
            self.less_handling_chrg_comm_exp[di, ii]  = float(linespt[30])
            self.less_taxes_surcharges_ops[di, ii]  = float(linespt[31])
            self.less_selling_dist_exp[di, ii]  = float(linespt[32])
            self.less_gerl_admin_exp[di, ii]  = float(linespt[33])
            self.less_fin_exp[di, ii]  = float(linespt[34])
            self.less_impair_loss_assets[di, ii]  = float(linespt[35])
            self.prepay_surr[di, ii]  = float(linespt[36])
            self.tot_claim_exp[di, ii]  = float(linespt[37])
            self.chg_insur_cont_rsrv[di, ii]  = float(linespt[38])
            self.dvd_exp_insured[di, ii]  = float(linespt[39])
            self.reinsurance_exp[di, ii]  = float(linespt[40])
            self.oper_exp[di, ii]  = float(linespt[41])
            self.less_claim_recb_reinsurer[di, ii]  = float(linespt[42])
            self.less_ins_rsrv_recb_reinsurer[di, ii]  = float(linespt[43])
            self.less_exp_recb_reinsurer[di, ii]  = float(linespt[44])
            self.other_bus_cost[di, ii]  = float(linespt[45])
            self.oper_profit[di, ii]  = float(linespt[46])
            self.plus_non_oper_rev[di, ii]  = float(linespt[47])
            self.less_non_oper_exp[di, ii]  = float(linespt[48])
            self.il_net_loss_disp_noncur_asset[di, ii]  = float(linespt[49])
            self.tot_profit[di, ii]  = float(linespt[50])
            self.inc_tax[di, ii]  = float(linespt[51])
            self.unconfirmed_invest_loss[di, ii]  = float(linespt[52])
            self.net_profit_incl_min_int_inc[di, ii]  = float(linespt[53])
            self.net_profit_excl_min_int_inc[di, ii]  = float(linespt[54])
            self.minority_int_inc[di, ii]  = float(linespt[55])
            self.other_compreh_inc[di, ii]  = float(linespt[56])
            self.tot_compreh_inc[di, ii]  = float(linespt[57])
            self.tot_compreh_inc_parent_comp[di, ii]  = float(linespt[58])
            self.tot_compreh_inc_min_shrhldr[di, ii]  = float(linespt[59])
            self.ebit[di, ii]  = float(linespt[60])
            self.ebitda[di, ii]  = float(linespt[61])
            self.net_profit_after_ded_nr_lp[di, ii]  = float(linespt[62])
            self.net_profit_under_intl_acc_sta[di, ii]  = float(linespt[63])
            self.comp_type_code[di, ii]  = float(linespt[64])
            self.s_fa_eps_basic[di, ii]  = float(linespt[65])
            self.s_fa_eps_diluted[di, ii]  = float(linespt[66])
            self.actual_ann_dt[di, ii]  = float(linespt[67])
            self.insurance_expense[di, ii]  = float(linespt[68])
            self.spe_bal_oper_profit[di, ii]  = float(linespt[69])
            self.tot_bal_oper_profit[di, ii]  = float(linespt[70])
            self.spe_bal_tot_profit[di, ii]  = float(linespt[71])
            self.tot_bal_tot_profit[di, ii]  = float(linespt[72])
            self.spe_bal_net_profit[di, ii]  = float(linespt[73])
            self.tot_bal_net_profit[di, ii]  = float(linespt[74])
            self.undistributed_profit[di, ii]  = float(linespt[75])
            self.adjlossgain_prevyear[di, ii]  = float(linespt[76])
            self.transfer_from_surplusreserve[di, ii]  = float(linespt[77])
            self.transfer_from_housingimprest[di, ii]  = float(linespt[78])
            self.transfer_from_others[di, ii]  = float(linespt[79])
            self.distributable_profit[di, ii]  = float(linespt[80])
            self.withdr_legalsurplus[di, ii]  = float(linespt[81])
            self.withdr_legalpubwelfunds[di, ii]  = float(linespt[82])
            self.workers_welfare[di, ii]  = float(linespt[83])
            self.withdr_buzexpwelfare[di, ii]  = float(linespt[84])
            self.withdr_reservefund[di, ii]  = float(linespt[85])
            self.distributable_profit_shrhder[di, ii]  = float(linespt[86])
            self.prfshare_dvd_payable[di, ii]  = float(linespt[87])
            self.withdr_othersurpreserve[di, ii]  = float(linespt[88])
            self.comshare_dvd_payable[di, ii]  = float(linespt[89])
            self.capitalized_comstock_div[di, ii]  = float(linespt[90])
            self.net_after_ded_nr_lp_correct[di, ii]  = float(linespt[91])
            self.other_income[di, ii]  = float(linespt[92])
            self.asset_disposal_income[di, ii]  = float(linespt[93])
            self.continued_net_profit[di, ii]  = float(linespt[94])
            self.end_net_profit[di, ii]  = float(linespt[95])
            self.credit_impairment_loss[di, ii]  = float(linespt[96])
            self.net_exposure_hedging_benefits[di, ii]  = float(linespt[97])
            self.rd_expense[di, ii]  = float(linespt[98])
            self.stmnote_finexp[di, ii]  = float(linespt[99])
            self.fin_exp_int_inc[di, ii]  = float(linespt[100])
            self.is_calculation[di, ii]  = float(linespt[101])
            self.other_impair_loss_assets[di, ii]  = float(linespt[102])
            self.tot_oper_cost2[di, ii]  = float(linespt[103])
            self.amodcost_fin_assets[di, ii]  = float(linespt[104])
            self.tot_opt_inc_dif[di, ii]  = float(linespt[105])
            self.tot_opt_cost_dif[di, ii]  = float(linespt[106])
            updated += 1
        infile.close()
        print('[ %s ] Updated %d stocks on day %d' %  (self.tag, updated, uv.Dates[di]))
        return

    def doBackfill(self, di):

        self.report_period[di] = self.report_period[di - 1]
        self.statement_type[di] = self.statement_type[di - 1]
        self.tot_oper_rev[di] = self.tot_oper_rev[di - 1]
        self.oper_rev[di] = self.oper_rev[di - 1]
        self.int_inc[di] = self.int_inc[di - 1]
        self.net_int_inc[di] = self.net_int_inc[di - 1]
        self.insur_prem_unearned[di] = self.insur_prem_unearned[di - 1]
        self.handling_chrg_comm_inc[di] = self.handling_chrg_comm_inc[di - 1]
        self.net_handling_chrg_comm_inc[di] = self.net_handling_chrg_comm_inc[di - 1]
        self.net_inc_other_ops[di] = self.net_inc_other_ops[di - 1]
        self.plus_net_inc_other_bus[di] = self.plus_net_inc_other_bus[di - 1]
        self.prem_inc[di] = self.prem_inc[di - 1]
        self.less_ceded_out_prem[di] = self.less_ceded_out_prem[di - 1]
        self.chg_unearned_prem_res[di] = self.chg_unearned_prem_res[di - 1]
        self.incl_reinsurance_prem_inc[di] = self.incl_reinsurance_prem_inc[di - 1]
        self.net_inc_sec_trading_brok_bus[di] = self.net_inc_sec_trading_brok_bus[di - 1]
        self.net_inc_sec_uw_bus[di] = self.net_inc_sec_uw_bus[di - 1]
        self.net_inc_ec_asset_mgmt_bus[di] = self.net_inc_ec_asset_mgmt_bus[di - 1]
        self.other_bus_inc[di] = self.other_bus_inc[di - 1]
        self.plus_net_gain_chg_fv[di] = self.plus_net_gain_chg_fv[di - 1]
        self.plus_net_invest_inc[di] = self.plus_net_invest_inc[di - 1]
        self.incl_inc_invest_assoc_jv_entp[di] = self.incl_inc_invest_assoc_jv_entp[di - 1]
        self.plus_net_gain_fx_trans[di] = self.plus_net_gain_fx_trans[di - 1]
        self.tot_oper_cost[di] = self.tot_oper_cost[di - 1]
        self.less_oper_cost[di] = self.less_oper_cost[di - 1]
        self.less_int_exp[di] = self.less_int_exp[di - 1]
        self.less_handling_chrg_comm_exp[di] = self.less_handling_chrg_comm_exp[di - 1]
        self.less_taxes_surcharges_ops[di] = self.less_taxes_surcharges_ops[di - 1]
        self.less_selling_dist_exp[di] = self.less_selling_dist_exp[di - 1]
        self.less_gerl_admin_exp[di] = self.less_gerl_admin_exp[di - 1]
        self.less_fin_exp[di] = self.less_fin_exp[di - 1]
        self.less_impair_loss_assets[di] = self.less_impair_loss_assets[di - 1]
        self.prepay_surr[di] = self.prepay_surr[di - 1]
        self.tot_claim_exp[di] = self.tot_claim_exp[di - 1]
        self.chg_insur_cont_rsrv[di] = self.chg_insur_cont_rsrv[di - 1]
        self.dvd_exp_insured[di] = self.dvd_exp_insured[di - 1]
        self.reinsurance_exp[di] = self.reinsurance_exp[di - 1]
        self.oper_exp[di] = self.oper_exp[di - 1]
        self.less_claim_recb_reinsurer[di] = self.less_claim_recb_reinsurer[di - 1]
        self.less_ins_rsrv_recb_reinsurer[di] = self.less_ins_rsrv_recb_reinsurer[di - 1]
        self.less_exp_recb_reinsurer[di] = self.less_exp_recb_reinsurer[di - 1]
        self.other_bus_cost[di] = self.other_bus_cost[di - 1]
        self.oper_profit[di] = self.oper_profit[di - 1]
        self.plus_non_oper_rev[di] = self.plus_non_oper_rev[di - 1]
        self.less_non_oper_exp[di] = self.less_non_oper_exp[di - 1]
        self.il_net_loss_disp_noncur_asset[di] = self.il_net_loss_disp_noncur_asset[di - 1]
        self.tot_profit[di] = self.tot_profit[di - 1]
        self.inc_tax[di] = self.inc_tax[di - 1]
        self.unconfirmed_invest_loss[di] = self.unconfirmed_invest_loss[di - 1]
        self.net_profit_incl_min_int_inc[di] = self.net_profit_incl_min_int_inc[di - 1]
        self.net_profit_excl_min_int_inc[di] = self.net_profit_excl_min_int_inc[di - 1]
        self.minority_int_inc[di] = self.minority_int_inc[di - 1]
        self.other_compreh_inc[di] = self.other_compreh_inc[di - 1]
        self.tot_compreh_inc[di] = self.tot_compreh_inc[di - 1]
        self.tot_compreh_inc_parent_comp[di] = self.tot_compreh_inc_parent_comp[di - 1]
        self.tot_compreh_inc_min_shrhldr[di] = self.tot_compreh_inc_min_shrhldr[di - 1]
        self.ebit[di] = self.ebit[di - 1]
        self.ebitda[di] = self.ebitda[di - 1]
        self.net_profit_after_ded_nr_lp[di] = self.net_profit_after_ded_nr_lp[di - 1]
        self.net_profit_under_intl_acc_sta[di] = self.net_profit_under_intl_acc_sta[di - 1]
        self.comp_type_code[di] = self.comp_type_code[di - 1]
        self.s_fa_eps_basic[di] = self.s_fa_eps_basic[di - 1]
        self.s_fa_eps_diluted[di] = self.s_fa_eps_diluted[di - 1]
        self.actual_ann_dt[di] = self.actual_ann_dt[di - 1]
        self.insurance_expense[di] = self.insurance_expense[di - 1]
        self.spe_bal_oper_profit[di] = self.spe_bal_oper_profit[di - 1]
        self.tot_bal_oper_profit[di] = self.tot_bal_oper_profit[di - 1]
        self.spe_bal_tot_profit[di] = self.spe_bal_tot_profit[di - 1]
        self.tot_bal_tot_profit[di] = self.tot_bal_tot_profit[di - 1]
        self.spe_bal_net_profit[di] = self.spe_bal_net_profit[di - 1]
        self.tot_bal_net_profit[di] = self.tot_bal_net_profit[di - 1]
        self.undistributed_profit[di] = self.undistributed_profit[di - 1]
        self.adjlossgain_prevyear[di] = self.adjlossgain_prevyear[di - 1]
        self.transfer_from_surplusreserve[di] = self.transfer_from_surplusreserve[di - 1]
        self.transfer_from_housingimprest[di] = self.transfer_from_housingimprest[di - 1]
        self.transfer_from_others[di] = self.transfer_from_others[di - 1]
        self.distributable_profit[di] = self.distributable_profit[di - 1]
        self.withdr_legalsurplus[di] = self.withdr_legalsurplus[di - 1]
        self.withdr_legalpubwelfunds[di] = self.withdr_legalpubwelfunds[di - 1]
        self.workers_welfare[di] = self.workers_welfare[di - 1]
        self.withdr_buzexpwelfare[di] = self.withdr_buzexpwelfare[di - 1]
        self.withdr_reservefund[di] = self.withdr_reservefund[di - 1]
        self.distributable_profit_shrhder[di] = self.distributable_profit_shrhder[di - 1]
        self.prfshare_dvd_payable[di] = self.prfshare_dvd_payable[di - 1]
        self.withdr_othersurpreserve[di] = self.withdr_othersurpreserve[di - 1]
        self.comshare_dvd_payable[di] = self.comshare_dvd_payable[di - 1]
        self.capitalized_comstock_div[di] = self.capitalized_comstock_div[di - 1]
        self.net_after_ded_nr_lp_correct[di] = self.net_after_ded_nr_lp_correct[di - 1]
        self.other_income[di] = self.other_income[di - 1]
        self.asset_disposal_income[di] = self.asset_disposal_income[di - 1]
        self.continued_net_profit[di] = self.continued_net_profit[di - 1]
        self.end_net_profit[di] = self.end_net_profit[di - 1]
        self.credit_impairment_loss[di] = self.credit_impairment_loss[di - 1]
        self.net_exposure_hedging_benefits[di] = self.net_exposure_hedging_benefits[di - 1]
        self.rd_expense[di] = self.rd_expense[di - 1]
        self.stmnote_finexp[di] = self.stmnote_finexp[di - 1]
        self.fin_exp_int_inc[di] = self.fin_exp_int_inc[di - 1]
        self.is_calculation[di] = self.is_calculation[di - 1]
        self.other_impair_loss_assets[di] = self.other_impair_loss_assets[di - 1]
        self.tot_oper_cost2[di] = self.tot_oper_cost2[di - 1]
        self.amodcost_fin_assets[di] = self.amodcost_fin_assets[di - 1]
        self.tot_opt_inc_dif[di] = self.tot_opt_inc_dif[di - 1]
        self.tot_opt_cost_dif[di] = self.tot_opt_cost_dif[di - 1]