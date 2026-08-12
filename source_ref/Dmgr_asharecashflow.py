
from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils import Calendar
import numpy as np
import os
import operator
import csv

class Dmgrasharecashflow(DataManagerMapped):
    def __init__(self, ):
        DataManagerMapped.__init__(self, )
        self.dataPath = None
        self.backfill = True
        self.report_period = NIO_MATRIX()
        self.statement_type = NIO_MATRIX()
        self.cash_recp_sg_and_rs = NIO_MATRIX()
        self.recp_tax_rends = NIO_MATRIX()
        self.net_incr_dep_cob = NIO_MATRIX()
        self.net_incr_loans_central_bank = NIO_MATRIX()
        self.net_incr_fund_borr_ofi = NIO_MATRIX()
        self.cash_recp_prem_orig_inco = NIO_MATRIX()
        self.net_incr_insured_dep = NIO_MATRIX()
        self.net_cash_received_reinsu_bus = NIO_MATRIX()
        self.net_incr_disp_tfa = NIO_MATRIX()
        self.net_incr_int_handling_chrg = NIO_MATRIX()
        self.net_incr_disp_faas = NIO_MATRIX()
        self.net_incr_loans_other_bank = NIO_MATRIX()
        self.net_incr_repurch_bus_fund = NIO_MATRIX()
        self.other_cash_recp_ral_oper_act = NIO_MATRIX()
        self.stot_cash_inflows_oper_act = NIO_MATRIX()
        self.cash_pay_goods_purch_serv_rec = NIO_MATRIX()
        self.cash_pay_beh_empl = NIO_MATRIX()
        self.pay_all_typ_tax = NIO_MATRIX()
        self.net_incr_clients_loan_adv = NIO_MATRIX()
        self.net_incr_dep_cbob = NIO_MATRIX()
        self.cash_pay_claims_orig_inco = NIO_MATRIX()
        self.handling_chrg_paid = NIO_MATRIX()
        self.comm_insur_plcy_paid = NIO_MATRIX()
        self.other_cash_pay_ral_oper_act = NIO_MATRIX()
        self.stot_cash_outflows_oper_act = NIO_MATRIX()
        self.net_cash_flows_oper_act = NIO_MATRIX()
        self.cash_recp_disp_withdrwl_invest = NIO_MATRIX()
        self.cash_recp_return_invest = NIO_MATRIX()
        self.net_cash_recp_disp_fiolta = NIO_MATRIX()
        self.net_cash_recp_disp_sobu = NIO_MATRIX()
        self.other_cash_recp_ral_inv_act = NIO_MATRIX()
        self.stot_cash_inflows_inv_act = NIO_MATRIX()
        self.cash_pay_acq_const_fiolta = NIO_MATRIX()
        self.cash_paid_invest = NIO_MATRIX()
        self.net_cash_pay_aquis_sobu = NIO_MATRIX()
        self.other_cash_pay_ral_inv_act = NIO_MATRIX()
        self.net_incr_pledge_loan = NIO_MATRIX()
        self.stot_cash_outflows_inv_act = NIO_MATRIX()
        self.net_cash_flows_inv_act = NIO_MATRIX()
        self.cash_recp_cap_contrib = NIO_MATRIX()
        self.incl_cash_rec_saims = NIO_MATRIX()
        self.cash_recp_borrow = NIO_MATRIX()
        self.proc_issue_bonds = NIO_MATRIX()
        self.other_cash_recp_ral_fnc_act = NIO_MATRIX()
        self.stot_cash_inflows_fnc_act = NIO_MATRIX()
        self.cash_prepay_amt_borr = NIO_MATRIX()
        self.cash_pay_dist_dpcp_int_exp = NIO_MATRIX()
        self.incl_dvd_profit_paid_sc_ms = NIO_MATRIX()
        self.other_cash_pay_ral_fnc_act = NIO_MATRIX()
        self.stot_cash_outflows_fnc_act = NIO_MATRIX()
        self.net_cash_flows_fnc_act = NIO_MATRIX()
        self.eff_fx_flu_cash = NIO_MATRIX()
        self.net_incr_cash_cash_equ = NIO_MATRIX()
        self.cash_cash_equ_beg_period = NIO_MATRIX()
        self.cash_cash_equ_end_period = NIO_MATRIX()
        self.net_profit = NIO_MATRIX()
        self.unconfirmed_invest_loss = NIO_MATRIX()
        self.plus_prov_depr_assets = NIO_MATRIX()
        self.depr_fa_coga_dpba = NIO_MATRIX()
        self.amort_intang_assets = NIO_MATRIX()
        self.amort_lt_deferred_exp = NIO_MATRIX()
        self.decr_deferred_exp = NIO_MATRIX()
        self.incr_acc_exp = NIO_MATRIX()
        self.loss_disp_fiolta = NIO_MATRIX()
        self.loss_scr_fa = NIO_MATRIX()
        self.loss_fv_chg = NIO_MATRIX()
        self.fin_exp = NIO_MATRIX()
        self.invest_loss = NIO_MATRIX()
        self.decr_deferred_inc_tax_assets = NIO_MATRIX()
        self.incr_deferred_inc_tax_liab = NIO_MATRIX()
        self.decr_inventories = NIO_MATRIX()
        self.decr_oper_payable = NIO_MATRIX()
        self.incr_oper_payable = NIO_MATRIX()
        self.im_net_cash_flows_oper_act = NIO_MATRIX()
        self.conv_debt_into_cap = NIO_MATRIX()
        self.conv_corp_bonds_due_within_1y = NIO_MATRIX()
        self.fa_fnc_leases = NIO_MATRIX()
        self.end_bal_cash = NIO_MATRIX()
        self.less_beg_bal_cash = NIO_MATRIX()
        self.plus_end_bal_cash_equ = NIO_MATRIX()
        self.less_beg_bal_cash_equ = NIO_MATRIX()
        self.im_net_incr_cash_cash_equ = NIO_MATRIX()
        self.free_cash_flow = NIO_MATRIX()
        self.comp_type_code = NIO_MATRIX()
        self.actual_ann_dt = NIO_MATRIX()
        self.spe_bal_cash_inflows_oper = NIO_MATRIX()
        self.tot_bal_cash_inflows_oper = NIO_MATRIX()
        self.spe_bal_cash_outflows_oper = NIO_MATRIX()
        self.tot_bal_cash_outflows_oper = NIO_MATRIX()
        self.tot_bal_netcash_outflows_oper = NIO_MATRIX()
        self.spe_bal_cash_inflows_inv = NIO_MATRIX()
        self.tot_bal_cash_inflows_inv = NIO_MATRIX()
        self.spe_bal_cash_outflows_inv = NIO_MATRIX()
        self.tot_bal_cash_outflows_inv = NIO_MATRIX()
        self.tot_bal_netcash_outflows_inv = NIO_MATRIX()
        self.spe_bal_cash_inflows_fnc = NIO_MATRIX()
        self.tot_bal_cash_inflows_fnc = NIO_MATRIX()
        self.spe_bal_cash_outflows_fnc = NIO_MATRIX()
        self.tot_bal_cash_outflows_fnc = NIO_MATRIX()
        self.tot_bal_netcash_outflows_fnc = NIO_MATRIX()
        self.spe_bal_netcash_inc = NIO_MATRIX()
        self.tot_bal_netcash_inc = NIO_MATRIX()
        self.spe_bal_netcash_equ_undir = NIO_MATRIX()
        self.tot_bal_netcash_equ_undir = NIO_MATRIX()
        self.spe_bal_netcash_inc_undir = NIO_MATRIX()
        self.tot_bal_netcash_inc_undir = NIO_MATRIX()
        self.s_dismantle_capital_add_net = NIO_MATRIX()
        self.is_calculation = NIO_MATRIX()
        self.securitie_netcash_received = NIO_MATRIX()
        self.other_impair_loss_assets = NIO_MATRIX()
        self.credit_impairment_loss = NIO_MATRIX()
        self.right_use_assets_dep = NIO_MATRIX()
        self.other_accounts = NIO_MATRIX()
        self.others = NIO_MATRIX()
        self.melt_money_net_increase = NIO_MATRIX()
        self.sec_fa_net_fina_instruments = NIO_MATRIX()
        return

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.dataPath = cfg.getAttributeString('dataPath')
        self.backfill = cfg.getAttributeDefault('backfill', True)
        self.addDailyData(self.report_period,self.tag + '.report_period')
        self.addDailyData(self.statement_type,self.tag + '.statement_type')
        self.addDailyData(self.cash_recp_sg_and_rs,self.tag + '.cash_recp_sg_and_rs')
        self.addDailyData(self.recp_tax_rends,self.tag + '.recp_tax_rends')
        self.addDailyData(self.net_incr_dep_cob,self.tag + '.net_incr_dep_cob')
        self.addDailyData(self.net_incr_loans_central_bank,self.tag + '.net_incr_loans_central_bank')
        self.addDailyData(self.net_incr_fund_borr_ofi,self.tag + '.net_incr_fund_borr_ofi')
        self.addDailyData(self.cash_recp_prem_orig_inco,self.tag + '.cash_recp_prem_orig_inco')
        self.addDailyData(self.net_incr_insured_dep,self.tag + '.net_incr_insured_dep')
        self.addDailyData(self.net_cash_received_reinsu_bus,self.tag + '.net_cash_received_reinsu_bus')
        self.addDailyData(self.net_incr_disp_tfa,self.tag + '.net_incr_disp_tfa')
        self.addDailyData(self.net_incr_int_handling_chrg,self.tag + '.net_incr_int_handling_chrg')
        self.addDailyData(self.net_incr_disp_faas,self.tag + '.net_incr_disp_faas')
        self.addDailyData(self.net_incr_loans_other_bank,self.tag + '.net_incr_loans_other_bank')
        self.addDailyData(self.net_incr_repurch_bus_fund,self.tag + '.net_incr_repurch_bus_fund')
        self.addDailyData(self.other_cash_recp_ral_oper_act,self.tag + '.other_cash_recp_ral_oper_act')
        self.addDailyData(self.stot_cash_inflows_oper_act,self.tag + '.stot_cash_inflows_oper_act')
        self.addDailyData(self.cash_pay_goods_purch_serv_rec,self.tag + '.cash_pay_goods_purch_serv_rec')
        self.addDailyData(self.cash_pay_beh_empl,self.tag + '.cash_pay_beh_empl')
        self.addDailyData(self.pay_all_typ_tax,self.tag + '.pay_all_typ_tax')
        self.addDailyData(self.net_incr_clients_loan_adv,self.tag + '.net_incr_clients_loan_adv')
        self.addDailyData(self.net_incr_dep_cbob,self.tag + '.net_incr_dep_cbob')
        self.addDailyData(self.cash_pay_claims_orig_inco,self.tag + '.cash_pay_claims_orig_inco')
        self.addDailyData(self.handling_chrg_paid,self.tag + '.handling_chrg_paid')
        self.addDailyData(self.comm_insur_plcy_paid,self.tag + '.comm_insur_plcy_paid')
        self.addDailyData(self.other_cash_pay_ral_oper_act,self.tag + '.other_cash_pay_ral_oper_act')
        self.addDailyData(self.stot_cash_outflows_oper_act,self.tag + '.stot_cash_outflows_oper_act')
        self.addDailyData(self.net_cash_flows_oper_act,self.tag + '.net_cash_flows_oper_act')
        self.addDailyData(self.cash_recp_disp_withdrwl_invest,self.tag + '.cash_recp_disp_withdrwl_invest')
        self.addDailyData(self.cash_recp_return_invest,self.tag + '.cash_recp_return_invest')
        self.addDailyData(self.net_cash_recp_disp_fiolta,self.tag + '.net_cash_recp_disp_fiolta')
        self.addDailyData(self.net_cash_recp_disp_sobu,self.tag + '.net_cash_recp_disp_sobu')
        self.addDailyData(self.other_cash_recp_ral_inv_act,self.tag + '.other_cash_recp_ral_inv_act')
        self.addDailyData(self.stot_cash_inflows_inv_act,self.tag + '.stot_cash_inflows_inv_act')
        self.addDailyData(self.cash_pay_acq_const_fiolta,self.tag + '.cash_pay_acq_const_fiolta')
        self.addDailyData(self.cash_paid_invest,self.tag + '.cash_paid_invest')
        self.addDailyData(self.net_cash_pay_aquis_sobu,self.tag + '.net_cash_pay_aquis_sobu')
        self.addDailyData(self.other_cash_pay_ral_inv_act,self.tag + '.other_cash_pay_ral_inv_act')
        self.addDailyData(self.net_incr_pledge_loan,self.tag + '.net_incr_pledge_loan')
        self.addDailyData(self.stot_cash_outflows_inv_act,self.tag + '.stot_cash_outflows_inv_act')
        self.addDailyData(self.net_cash_flows_inv_act,self.tag + '.net_cash_flows_inv_act')
        self.addDailyData(self.cash_recp_cap_contrib,self.tag + '.cash_recp_cap_contrib')
        self.addDailyData(self.incl_cash_rec_saims,self.tag + '.incl_cash_rec_saims')
        self.addDailyData(self.cash_recp_borrow,self.tag + '.cash_recp_borrow')
        self.addDailyData(self.proc_issue_bonds,self.tag + '.proc_issue_bonds')
        self.addDailyData(self.other_cash_recp_ral_fnc_act,self.tag + '.other_cash_recp_ral_fnc_act')
        self.addDailyData(self.stot_cash_inflows_fnc_act,self.tag + '.stot_cash_inflows_fnc_act')
        self.addDailyData(self.cash_prepay_amt_borr,self.tag + '.cash_prepay_amt_borr')
        self.addDailyData(self.cash_pay_dist_dpcp_int_exp,self.tag + '.cash_pay_dist_dpcp_int_exp')
        self.addDailyData(self.incl_dvd_profit_paid_sc_ms,self.tag + '.incl_dvd_profit_paid_sc_ms')
        self.addDailyData(self.other_cash_pay_ral_fnc_act,self.tag + '.other_cash_pay_ral_fnc_act')
        self.addDailyData(self.stot_cash_outflows_fnc_act,self.tag + '.stot_cash_outflows_fnc_act')
        self.addDailyData(self.net_cash_flows_fnc_act,self.tag + '.net_cash_flows_fnc_act')
        self.addDailyData(self.eff_fx_flu_cash,self.tag + '.eff_fx_flu_cash')
        self.addDailyData(self.net_incr_cash_cash_equ,self.tag + '.net_incr_cash_cash_equ')
        self.addDailyData(self.cash_cash_equ_beg_period,self.tag + '.cash_cash_equ_beg_period')
        self.addDailyData(self.cash_cash_equ_end_period,self.tag + '.cash_cash_equ_end_period')
        self.addDailyData(self.net_profit,self.tag + '.net_profit')
        self.addDailyData(self.unconfirmed_invest_loss,self.tag + '.unconfirmed_invest_loss')
        self.addDailyData(self.plus_prov_depr_assets,self.tag + '.plus_prov_depr_assets')
        self.addDailyData(self.depr_fa_coga_dpba,self.tag + '.depr_fa_coga_dpba')
        self.addDailyData(self.amort_intang_assets,self.tag + '.amort_intang_assets')
        self.addDailyData(self.amort_lt_deferred_exp,self.tag + '.amort_lt_deferred_exp')
        self.addDailyData(self.decr_deferred_exp,self.tag + '.decr_deferred_exp')
        self.addDailyData(self.incr_acc_exp,self.tag + '.incr_acc_exp')
        self.addDailyData(self.loss_disp_fiolta,self.tag + '.loss_disp_fiolta')
        self.addDailyData(self.loss_scr_fa,self.tag + '.loss_scr_fa')
        self.addDailyData(self.loss_fv_chg,self.tag + '.loss_fv_chg')
        self.addDailyData(self.fin_exp,self.tag + '.fin_exp')
        self.addDailyData(self.invest_loss,self.tag + '.invest_loss')
        self.addDailyData(self.decr_deferred_inc_tax_assets,self.tag + '.decr_deferred_inc_tax_assets')
        self.addDailyData(self.incr_deferred_inc_tax_liab,self.tag + '.incr_deferred_inc_tax_liab')
        self.addDailyData(self.decr_inventories,self.tag + '.decr_inventories')
        self.addDailyData(self.decr_oper_payable,self.tag + '.decr_oper_payable')
        self.addDailyData(self.incr_oper_payable,self.tag + '.incr_oper_payable')
        self.addDailyData(self.im_net_cash_flows_oper_act,self.tag + '.im_net_cash_flows_oper_act')
        self.addDailyData(self.conv_debt_into_cap,self.tag + '.conv_debt_into_cap')
        self.addDailyData(self.conv_corp_bonds_due_within_1y,self.tag + '.conv_corp_bonds_due_within_1y')
        self.addDailyData(self.fa_fnc_leases,self.tag + '.fa_fnc_leases')
        self.addDailyData(self.end_bal_cash,self.tag + '.end_bal_cash')
        self.addDailyData(self.less_beg_bal_cash,self.tag + '.less_beg_bal_cash')
        self.addDailyData(self.plus_end_bal_cash_equ,self.tag + '.plus_end_bal_cash_equ')
        self.addDailyData(self.less_beg_bal_cash_equ,self.tag + '.less_beg_bal_cash_equ')
        self.addDailyData(self.im_net_incr_cash_cash_equ,self.tag + '.im_net_incr_cash_cash_equ')
        self.addDailyData(self.free_cash_flow,self.tag + '.free_cash_flow')
        self.addDailyData(self.comp_type_code,self.tag + '.comp_type_code')
        self.addDailyData(self.actual_ann_dt,self.tag + '.actual_ann_dt')
        self.addDailyData(self.spe_bal_cash_inflows_oper,self.tag + '.spe_bal_cash_inflows_oper')
        self.addDailyData(self.tot_bal_cash_inflows_oper,self.tag + '.tot_bal_cash_inflows_oper')
        self.addDailyData(self.spe_bal_cash_outflows_oper,self.tag + '.spe_bal_cash_outflows_oper')
        self.addDailyData(self.tot_bal_cash_outflows_oper,self.tag + '.tot_bal_cash_outflows_oper')
        self.addDailyData(self.tot_bal_netcash_outflows_oper,self.tag + '.tot_bal_netcash_outflows_oper')
        self.addDailyData(self.spe_bal_cash_inflows_inv,self.tag + '.spe_bal_cash_inflows_inv')
        self.addDailyData(self.tot_bal_cash_inflows_inv,self.tag + '.tot_bal_cash_inflows_inv')
        self.addDailyData(self.spe_bal_cash_outflows_inv,self.tag + '.spe_bal_cash_outflows_inv')
        self.addDailyData(self.tot_bal_cash_outflows_inv,self.tag + '.tot_bal_cash_outflows_inv')
        self.addDailyData(self.tot_bal_netcash_outflows_inv,self.tag + '.tot_bal_netcash_outflows_inv')
        self.addDailyData(self.spe_bal_cash_inflows_fnc,self.tag + '.spe_bal_cash_inflows_fnc')
        self.addDailyData(self.tot_bal_cash_inflows_fnc,self.tag + '.tot_bal_cash_inflows_fnc')
        self.addDailyData(self.spe_bal_cash_outflows_fnc,self.tag + '.spe_bal_cash_outflows_fnc')
        self.addDailyData(self.tot_bal_cash_outflows_fnc,self.tag + '.tot_bal_cash_outflows_fnc')
        self.addDailyData(self.tot_bal_netcash_outflows_fnc,self.tag + '.tot_bal_netcash_outflows_fnc')
        self.addDailyData(self.spe_bal_netcash_inc,self.tag + '.spe_bal_netcash_inc')
        self.addDailyData(self.tot_bal_netcash_inc,self.tag + '.tot_bal_netcash_inc')
        self.addDailyData(self.spe_bal_netcash_equ_undir,self.tag + '.spe_bal_netcash_equ_undir')
        self.addDailyData(self.tot_bal_netcash_equ_undir,self.tag + '.tot_bal_netcash_equ_undir')
        self.addDailyData(self.spe_bal_netcash_inc_undir,self.tag + '.spe_bal_netcash_inc_undir')
        self.addDailyData(self.tot_bal_netcash_inc_undir,self.tag + '.tot_bal_netcash_inc_undir')
        self.addDailyData(self.s_dismantle_capital_add_net,self.tag + '.s_dismantle_capital_add_net')
        self.addDailyData(self.is_calculation,self.tag + '.is_calculation')
        self.addDailyData(self.securitie_netcash_received,self.tag + '.securitie_netcash_received')
        self.addDailyData(self.other_impair_loss_assets,self.tag + '.other_impair_loss_assets')
        self.addDailyData(self.credit_impairment_loss,self.tag + '.credit_impairment_loss')
        self.addDailyData(self.right_use_assets_dep,self.tag + '.right_use_assets_dep')
        self.addDailyData(self.other_accounts,self.tag + '.other_accounts')
        self.addDailyData(self.others,self.tag + '.others')
        self.addDailyData(self.melt_money_net_increase,self.tag + '.melt_money_net_increase')
        self.addDailyData(self.sec_fa_net_fina_instruments,self.tag + '.sec_fa_net_fina_instruments')
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
            self.cash_recp_sg_and_rs[di, ii]  = float(linespt[7])
            self.recp_tax_rends[di, ii]  = float(linespt[8])
            self.net_incr_dep_cob[di, ii]  = float(linespt[9])
            self.net_incr_loans_central_bank[di, ii]  = float(linespt[10])
            self.net_incr_fund_borr_ofi[di, ii]  = float(linespt[11])
            self.cash_recp_prem_orig_inco[di, ii]  = float(linespt[12])
            self.net_incr_insured_dep[di, ii]  = float(linespt[13])
            self.net_cash_received_reinsu_bus[di, ii]  = float(linespt[14])
            self.net_incr_disp_tfa[di, ii]  = float(linespt[15])
            self.net_incr_int_handling_chrg[di, ii]  = float(linespt[16])
            self.net_incr_disp_faas[di, ii]  = float(linespt[17])
            self.net_incr_loans_other_bank[di, ii]  = float(linespt[18])
            self.net_incr_repurch_bus_fund[di, ii]  = float(linespt[19])
            self.other_cash_recp_ral_oper_act[di, ii]  = float(linespt[20])
            self.stot_cash_inflows_oper_act[di, ii]  = float(linespt[21])
            self.cash_pay_goods_purch_serv_rec[di, ii]  = float(linespt[22])
            self.cash_pay_beh_empl[di, ii]  = float(linespt[23])
            self.pay_all_typ_tax[di, ii]  = float(linespt[24])
            self.net_incr_clients_loan_adv[di, ii]  = float(linespt[25])
            self.net_incr_dep_cbob[di, ii]  = float(linespt[26])
            self.cash_pay_claims_orig_inco[di, ii]  = float(linespt[27])
            self.handling_chrg_paid[di, ii]  = float(linespt[28])
            self.comm_insur_plcy_paid[di, ii]  = float(linespt[29])
            self.other_cash_pay_ral_oper_act[di, ii]  = float(linespt[30])
            self.stot_cash_outflows_oper_act[di, ii]  = float(linespt[31])
            self.net_cash_flows_oper_act[di, ii]  = float(linespt[32])
            self.cash_recp_disp_withdrwl_invest[di, ii]  = float(linespt[33])
            self.cash_recp_return_invest[di, ii]  = float(linespt[34])
            self.net_cash_recp_disp_fiolta[di, ii]  = float(linespt[35])
            self.net_cash_recp_disp_sobu[di, ii]  = float(linespt[36])
            self.other_cash_recp_ral_inv_act[di, ii]  = float(linespt[37])
            self.stot_cash_inflows_inv_act[di, ii]  = float(linespt[38])
            self.cash_pay_acq_const_fiolta[di, ii]  = float(linespt[39])
            self.cash_paid_invest[di, ii]  = float(linespt[40])
            self.net_cash_pay_aquis_sobu[di, ii]  = float(linespt[41])
            self.other_cash_pay_ral_inv_act[di, ii]  = float(linespt[42])
            self.net_incr_pledge_loan[di, ii]  = float(linespt[43])
            self.stot_cash_outflows_inv_act[di, ii]  = float(linespt[44])
            self.net_cash_flows_inv_act[di, ii]  = float(linespt[45])
            self.cash_recp_cap_contrib[di, ii]  = float(linespt[46])
            self.incl_cash_rec_saims[di, ii]  = float(linespt[47])
            self.cash_recp_borrow[di, ii]  = float(linespt[48])
            self.proc_issue_bonds[di, ii]  = float(linespt[49])
            self.other_cash_recp_ral_fnc_act[di, ii]  = float(linespt[50])
            self.stot_cash_inflows_fnc_act[di, ii]  = float(linespt[51])
            self.cash_prepay_amt_borr[di, ii]  = float(linespt[52])
            self.cash_pay_dist_dpcp_int_exp[di, ii]  = float(linespt[53])
            self.incl_dvd_profit_paid_sc_ms[di, ii]  = float(linespt[54])
            self.other_cash_pay_ral_fnc_act[di, ii]  = float(linespt[55])
            self.stot_cash_outflows_fnc_act[di, ii]  = float(linespt[56])
            self.net_cash_flows_fnc_act[di, ii]  = float(linespt[57])
            self.eff_fx_flu_cash[di, ii]  = float(linespt[58])
            self.net_incr_cash_cash_equ[di, ii]  = float(linespt[59])
            self.cash_cash_equ_beg_period[di, ii]  = float(linespt[60])
            self.cash_cash_equ_end_period[di, ii]  = float(linespt[61])
            self.net_profit[di, ii]  = float(linespt[62])
            self.unconfirmed_invest_loss[di, ii]  = float(linespt[63])
            self.plus_prov_depr_assets[di, ii]  = float(linespt[64])
            self.depr_fa_coga_dpba[di, ii]  = float(linespt[65])
            self.amort_intang_assets[di, ii]  = float(linespt[66])
            self.amort_lt_deferred_exp[di, ii]  = float(linespt[67])
            self.decr_deferred_exp[di, ii]  = float(linespt[68])
            self.incr_acc_exp[di, ii]  = float(linespt[69])
            self.loss_disp_fiolta[di, ii]  = float(linespt[70])
            self.loss_scr_fa[di, ii]  = float(linespt[71])
            self.loss_fv_chg[di, ii]  = float(linespt[72])
            self.fin_exp[di, ii]  = float(linespt[73])
            self.invest_loss[di, ii]  = float(linespt[74])
            self.decr_deferred_inc_tax_assets[di, ii]  = float(linespt[75])
            self.incr_deferred_inc_tax_liab[di, ii]  = float(linespt[76])
            self.decr_inventories[di, ii]  = float(linespt[77])
            self.decr_oper_payable[di, ii]  = float(linespt[78])
            self.incr_oper_payable[di, ii]  = float(linespt[79])
            self.im_net_cash_flows_oper_act[di, ii]  = float(linespt[80])
            self.conv_debt_into_cap[di, ii]  = float(linespt[81])
            self.conv_corp_bonds_due_within_1y[di, ii]  = float(linespt[82])
            self.fa_fnc_leases[di, ii]  = float(linespt[83])
            self.end_bal_cash[di, ii]  = float(linespt[84])
            self.less_beg_bal_cash[di, ii]  = float(linespt[85])
            self.plus_end_bal_cash_equ[di, ii]  = float(linespt[86])
            self.less_beg_bal_cash_equ[di, ii]  = float(linespt[87])
            self.im_net_incr_cash_cash_equ[di, ii]  = float(linespt[88])
            self.free_cash_flow[di, ii]  = float(linespt[89])
            self.comp_type_code[di, ii]  = float(linespt[90])
            self.actual_ann_dt[di, ii]  = float(linespt[91])
            self.spe_bal_cash_inflows_oper[di, ii]  = float(linespt[92])
            self.tot_bal_cash_inflows_oper[di, ii]  = float(linespt[93])
            self.spe_bal_cash_outflows_oper[di, ii]  = float(linespt[94])
            self.tot_bal_cash_outflows_oper[di, ii]  = float(linespt[95])
            self.tot_bal_netcash_outflows_oper[di, ii]  = float(linespt[96])
            self.spe_bal_cash_inflows_inv[di, ii]  = float(linespt[97])
            self.tot_bal_cash_inflows_inv[di, ii]  = float(linespt[98])
            self.spe_bal_cash_outflows_inv[di, ii]  = float(linespt[99])
            self.tot_bal_cash_outflows_inv[di, ii]  = float(linespt[100])
            self.tot_bal_netcash_outflows_inv[di, ii]  = float(linespt[101])
            self.spe_bal_cash_inflows_fnc[di, ii]  = float(linespt[102])
            self.tot_bal_cash_inflows_fnc[di, ii]  = float(linespt[103])
            self.spe_bal_cash_outflows_fnc[di, ii]  = float(linespt[104])
            self.tot_bal_cash_outflows_fnc[di, ii]  = float(linespt[105])
            self.tot_bal_netcash_outflows_fnc[di, ii]  = float(linespt[106])
            self.spe_bal_netcash_inc[di, ii]  = float(linespt[107])
            self.tot_bal_netcash_inc[di, ii]  = float(linespt[108])
            self.spe_bal_netcash_equ_undir[di, ii]  = float(linespt[109])
            self.tot_bal_netcash_equ_undir[di, ii]  = float(linespt[110])
            self.spe_bal_netcash_inc_undir[di, ii]  = float(linespt[111])
            self.tot_bal_netcash_inc_undir[di, ii]  = float(linespt[112])
            self.s_dismantle_capital_add_net[di, ii]  = float(linespt[114])
            self.is_calculation[di, ii]  = float(linespt[115])
            self.securitie_netcash_received[di, ii]  = float(linespt[116])
            self.other_impair_loss_assets[di, ii]  = float(linespt[117])
            self.credit_impairment_loss[di, ii]  = float(linespt[118])
            self.right_use_assets_dep[di, ii]  = float(linespt[119])
            self.other_accounts[di, ii]  = float(linespt[120])
            self.others[di, ii]  = float(linespt[121])
            self.melt_money_net_increase[di, ii]  = float(linespt[124])
            self.sec_fa_net_fina_instruments[di, ii]  = float(linespt[125])
            updated += 1
        infile.close()
        print('[ %s ] Updated %d stocks on day %d' %  (self.tag, updated, uv.Dates[di]))
        return

    def doBackfill(self, di):

        self.report_period[di] = self.report_period[di - 1]
        self.statement_type[di] = self.statement_type[di - 1]
        self.cash_recp_sg_and_rs[di] = self.cash_recp_sg_and_rs[di - 1]
        self.recp_tax_rends[di] = self.recp_tax_rends[di - 1]
        self.net_incr_dep_cob[di] = self.net_incr_dep_cob[di - 1]
        self.net_incr_loans_central_bank[di] = self.net_incr_loans_central_bank[di - 1]
        self.net_incr_fund_borr_ofi[di] = self.net_incr_fund_borr_ofi[di - 1]
        self.cash_recp_prem_orig_inco[di] = self.cash_recp_prem_orig_inco[di - 1]
        self.net_incr_insured_dep[di] = self.net_incr_insured_dep[di - 1]
        self.net_cash_received_reinsu_bus[di] = self.net_cash_received_reinsu_bus[di - 1]
        self.net_incr_disp_tfa[di] = self.net_incr_disp_tfa[di - 1]
        self.net_incr_int_handling_chrg[di] = self.net_incr_int_handling_chrg[di - 1]
        self.net_incr_disp_faas[di] = self.net_incr_disp_faas[di - 1]
        self.net_incr_loans_other_bank[di] = self.net_incr_loans_other_bank[di - 1]
        self.net_incr_repurch_bus_fund[di] = self.net_incr_repurch_bus_fund[di - 1]
        self.other_cash_recp_ral_oper_act[di] = self.other_cash_recp_ral_oper_act[di - 1]
        self.stot_cash_inflows_oper_act[di] = self.stot_cash_inflows_oper_act[di - 1]
        self.cash_pay_goods_purch_serv_rec[di] = self.cash_pay_goods_purch_serv_rec[di - 1]
        self.cash_pay_beh_empl[di] = self.cash_pay_beh_empl[di - 1]
        self.pay_all_typ_tax[di] = self.pay_all_typ_tax[di - 1]
        self.net_incr_clients_loan_adv[di] = self.net_incr_clients_loan_adv[di - 1]
        self.net_incr_dep_cbob[di] = self.net_incr_dep_cbob[di - 1]
        self.cash_pay_claims_orig_inco[di] = self.cash_pay_claims_orig_inco[di - 1]
        self.handling_chrg_paid[di] = self.handling_chrg_paid[di - 1]
        self.comm_insur_plcy_paid[di] = self.comm_insur_plcy_paid[di - 1]
        self.other_cash_pay_ral_oper_act[di] = self.other_cash_pay_ral_oper_act[di - 1]
        self.stot_cash_outflows_oper_act[di] = self.stot_cash_outflows_oper_act[di - 1]
        self.net_cash_flows_oper_act[di] = self.net_cash_flows_oper_act[di - 1]
        self.cash_recp_disp_withdrwl_invest[di] = self.cash_recp_disp_withdrwl_invest[di - 1]
        self.cash_recp_return_invest[di] = self.cash_recp_return_invest[di - 1]
        self.net_cash_recp_disp_fiolta[di] = self.net_cash_recp_disp_fiolta[di - 1]
        self.net_cash_recp_disp_sobu[di] = self.net_cash_recp_disp_sobu[di - 1]
        self.other_cash_recp_ral_inv_act[di] = self.other_cash_recp_ral_inv_act[di - 1]
        self.stot_cash_inflows_inv_act[di] = self.stot_cash_inflows_inv_act[di - 1]
        self.cash_pay_acq_const_fiolta[di] = self.cash_pay_acq_const_fiolta[di - 1]
        self.cash_paid_invest[di] = self.cash_paid_invest[di - 1]
        self.net_cash_pay_aquis_sobu[di] = self.net_cash_pay_aquis_sobu[di - 1]
        self.other_cash_pay_ral_inv_act[di] = self.other_cash_pay_ral_inv_act[di - 1]
        self.net_incr_pledge_loan[di] = self.net_incr_pledge_loan[di - 1]
        self.stot_cash_outflows_inv_act[di] = self.stot_cash_outflows_inv_act[di - 1]
        self.net_cash_flows_inv_act[di] = self.net_cash_flows_inv_act[di - 1]
        self.cash_recp_cap_contrib[di] = self.cash_recp_cap_contrib[di - 1]
        self.incl_cash_rec_saims[di] = self.incl_cash_rec_saims[di - 1]
        self.cash_recp_borrow[di] = self.cash_recp_borrow[di - 1]
        self.proc_issue_bonds[di] = self.proc_issue_bonds[di - 1]
        self.other_cash_recp_ral_fnc_act[di] = self.other_cash_recp_ral_fnc_act[di - 1]
        self.stot_cash_inflows_fnc_act[di] = self.stot_cash_inflows_fnc_act[di - 1]
        self.cash_prepay_amt_borr[di] = self.cash_prepay_amt_borr[di - 1]
        self.cash_pay_dist_dpcp_int_exp[di] = self.cash_pay_dist_dpcp_int_exp[di - 1]
        self.incl_dvd_profit_paid_sc_ms[di] = self.incl_dvd_profit_paid_sc_ms[di - 1]
        self.other_cash_pay_ral_fnc_act[di] = self.other_cash_pay_ral_fnc_act[di - 1]
        self.stot_cash_outflows_fnc_act[di] = self.stot_cash_outflows_fnc_act[di - 1]
        self.net_cash_flows_fnc_act[di] = self.net_cash_flows_fnc_act[di - 1]
        self.eff_fx_flu_cash[di] = self.eff_fx_flu_cash[di - 1]
        self.net_incr_cash_cash_equ[di] = self.net_incr_cash_cash_equ[di - 1]
        self.cash_cash_equ_beg_period[di] = self.cash_cash_equ_beg_period[di - 1]
        self.cash_cash_equ_end_period[di] = self.cash_cash_equ_end_period[di - 1]
        self.net_profit[di] = self.net_profit[di - 1]
        self.unconfirmed_invest_loss[di] = self.unconfirmed_invest_loss[di - 1]
        self.plus_prov_depr_assets[di] = self.plus_prov_depr_assets[di - 1]
        self.depr_fa_coga_dpba[di] = self.depr_fa_coga_dpba[di - 1]
        self.amort_intang_assets[di] = self.amort_intang_assets[di - 1]
        self.amort_lt_deferred_exp[di] = self.amort_lt_deferred_exp[di - 1]
        self.decr_deferred_exp[di] = self.decr_deferred_exp[di - 1]
        self.incr_acc_exp[di] = self.incr_acc_exp[di - 1]
        self.loss_disp_fiolta[di] = self.loss_disp_fiolta[di - 1]
        self.loss_scr_fa[di] = self.loss_scr_fa[di - 1]
        self.loss_fv_chg[di] = self.loss_fv_chg[di - 1]
        self.fin_exp[di] = self.fin_exp[di - 1]
        self.invest_loss[di] = self.invest_loss[di - 1]
        self.decr_deferred_inc_tax_assets[di] = self.decr_deferred_inc_tax_assets[di - 1]
        self.incr_deferred_inc_tax_liab[di] = self.incr_deferred_inc_tax_liab[di - 1]
        self.decr_inventories[di] = self.decr_inventories[di - 1]
        self.decr_oper_payable[di] = self.decr_oper_payable[di - 1]
        self.incr_oper_payable[di] = self.incr_oper_payable[di - 1]
        self.im_net_cash_flows_oper_act[di] = self.im_net_cash_flows_oper_act[di - 1]
        self.conv_debt_into_cap[di] = self.conv_debt_into_cap[di - 1]
        self.conv_corp_bonds_due_within_1y[di] = self.conv_corp_bonds_due_within_1y[di - 1]
        self.fa_fnc_leases[di] = self.fa_fnc_leases[di - 1]
        self.end_bal_cash[di] = self.end_bal_cash[di - 1]
        self.less_beg_bal_cash[di] = self.less_beg_bal_cash[di - 1]
        self.plus_end_bal_cash_equ[di] = self.plus_end_bal_cash_equ[di - 1]
        self.less_beg_bal_cash_equ[di] = self.less_beg_bal_cash_equ[di - 1]
        self.im_net_incr_cash_cash_equ[di] = self.im_net_incr_cash_cash_equ[di - 1]
        self.free_cash_flow[di] = self.free_cash_flow[di - 1]
        self.comp_type_code[di] = self.comp_type_code[di - 1]
        self.actual_ann_dt[di] = self.actual_ann_dt[di - 1]
        self.spe_bal_cash_inflows_oper[di] = self.spe_bal_cash_inflows_oper[di - 1]
        self.tot_bal_cash_inflows_oper[di] = self.tot_bal_cash_inflows_oper[di - 1]
        self.spe_bal_cash_outflows_oper[di] = self.spe_bal_cash_outflows_oper[di - 1]
        self.tot_bal_cash_outflows_oper[di] = self.tot_bal_cash_outflows_oper[di - 1]
        self.tot_bal_netcash_outflows_oper[di] = self.tot_bal_netcash_outflows_oper[di - 1]
        self.spe_bal_cash_inflows_inv[di] = self.spe_bal_cash_inflows_inv[di - 1]
        self.tot_bal_cash_inflows_inv[di] = self.tot_bal_cash_inflows_inv[di - 1]
        self.spe_bal_cash_outflows_inv[di] = self.spe_bal_cash_outflows_inv[di - 1]
        self.tot_bal_cash_outflows_inv[di] = self.tot_bal_cash_outflows_inv[di - 1]
        self.tot_bal_netcash_outflows_inv[di] = self.tot_bal_netcash_outflows_inv[di - 1]
        self.spe_bal_cash_inflows_fnc[di] = self.spe_bal_cash_inflows_fnc[di - 1]
        self.tot_bal_cash_inflows_fnc[di] = self.tot_bal_cash_inflows_fnc[di - 1]
        self.spe_bal_cash_outflows_fnc[di] = self.spe_bal_cash_outflows_fnc[di - 1]
        self.tot_bal_cash_outflows_fnc[di] = self.tot_bal_cash_outflows_fnc[di - 1]
        self.tot_bal_netcash_outflows_fnc[di] = self.tot_bal_netcash_outflows_fnc[di - 1]
        self.spe_bal_netcash_inc[di] = self.spe_bal_netcash_inc[di - 1]
        self.tot_bal_netcash_inc[di] = self.tot_bal_netcash_inc[di - 1]
        self.spe_bal_netcash_equ_undir[di] = self.spe_bal_netcash_equ_undir[di - 1]
        self.tot_bal_netcash_equ_undir[di] = self.tot_bal_netcash_equ_undir[di - 1]
        self.spe_bal_netcash_inc_undir[di] = self.spe_bal_netcash_inc_undir[di - 1]
        self.tot_bal_netcash_inc_undir[di] = self.tot_bal_netcash_inc_undir[di - 1]
        self.s_dismantle_capital_add_net[di] = self.s_dismantle_capital_add_net[di - 1]
        self.is_calculation[di] = self.is_calculation[di - 1]
        self.securitie_netcash_received[di] = self.securitie_netcash_received[di - 1]
        self.other_impair_loss_assets[di] = self.other_impair_loss_assets[di - 1]
        self.credit_impairment_loss[di] = self.credit_impairment_loss[di - 1]
        self.right_use_assets_dep[di] = self.right_use_assets_dep[di - 1]
        self.other_accounts[di] = self.other_accounts[di - 1]
        self.others[di] = self.others[di - 1]
        self.melt_money_net_increase[di] = self.melt_money_net_increase[di - 1]
        self.sec_fa_net_fina_instruments[di] = self.sec_fa_net_fina_instruments[di - 1]