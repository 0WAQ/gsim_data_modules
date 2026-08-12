from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import Universe as uv
from gsim.data import DataRegistry as dr
import pandas as pd
import glob
import logging


class DmgrAShareIncome3d12q(DataManagerMapped):
    def __init__(self):
        DataManagerMapped.__init__(self)
        self.dataPath = ''
        self.nquarters = 12

        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s - %(levelname)s - %(message)s',
            filename='cashflow.log'
        )

        ########################################################################################################################################
        # 字符串类型字段(varchar/timestamp)
        self.report_period = NIO_CUBE()
        self.actual_ann_dt = NIO_CUBE()

        # 数值类型字段(numeric)
        self.statement_type = NIO_CUBE()
        self.cash_recp_sg_and_rs = NIO_CUBE()
        self.recp_tax_rends = NIO_CUBE()
        self.net_incr_dep_cob = NIO_CUBE()
        self.net_incr_loans_central_bank = NIO_CUBE()
        self.net_incr_fund_borr_ofi = NIO_CUBE()
        self.cash_recp_prem_orig_inco = NIO_CUBE()
        self.net_incr_insured_dep = NIO_CUBE()
        self.net_cash_received_reinsu_bus = NIO_CUBE()
        self.net_incr_disp_tfa = NIO_CUBE()
        self.net_incr_int_handling_chrg = NIO_CUBE()
        self.net_incr_disp_faas = NIO_CUBE()
        self.net_incr_loans_other_bank = NIO_CUBE()
        self.net_incr_repurch_bus_fund = NIO_CUBE()
        self.other_cash_recp_ral_oper_act = NIO_CUBE()
        self.stot_cash_inflows_oper_act = NIO_CUBE()
        self.cash_pay_goods_purch_serv_rec = NIO_CUBE()
        self.cash_pay_beh_empl = NIO_CUBE()
        self.pay_all_typ_tax = NIO_CUBE()
        self.net_incr_clients_loan_adv = NIO_CUBE()
        self.net_incr_dep_cbob = NIO_CUBE()
        self.cash_pay_claims_orig_inco = NIO_CUBE()
        self.handling_chrg_paid = NIO_CUBE()
        self.comm_insur_plcy_paid = NIO_CUBE()
        self.other_cash_pay_ral_oper_act = NIO_CUBE()
        self.stot_cash_outflows_oper_act = NIO_CUBE()
        self.net_cash_flows_oper_act = NIO_CUBE()
        self.cash_recp_disp_withdrwl_invest = NIO_CUBE()
        self.cash_recp_return_invest = NIO_CUBE()
        self.net_cash_recp_disp_fiolta = NIO_CUBE()
        self.net_cash_recp_disp_sobu = NIO_CUBE()
        self.other_cash_recp_ral_inv_act = NIO_CUBE()
        self.stot_cash_inflows_inv_act = NIO_CUBE()
        self.cash_pay_acq_const_fiolta = NIO_CUBE()
        self.cash_paid_invest = NIO_CUBE()
        self.net_cash_pay_aquis_sobu = NIO_CUBE()
        self.other_cash_pay_ral_inv_act = NIO_CUBE()
        self.net_incr_pledge_loan = NIO_CUBE()
        self.stot_cash_outflows_inv_act = NIO_CUBE()
        self.net_cash_flows_inv_act = NIO_CUBE()
        self.cash_recp_cap_contrib = NIO_CUBE()
        self.incl_cash_rec_saims = NIO_CUBE()
        self.cash_recp_borrow = NIO_CUBE()
        self.proc_issue_bonds = NIO_CUBE()
        self.other_cash_recp_ral_fnc_act = NIO_CUBE()
        self.stot_cash_inflows_fnc_act = NIO_CUBE()
        self.cash_prepay_amt_borr = NIO_CUBE()
        self.cash_pay_dist_dpcp_int_exp = NIO_CUBE()
        self.incl_dvd_profit_paid_sc_ms = NIO_CUBE()
        self.other_cash_pay_ral_fnc_act = NIO_CUBE()
        self.stot_cash_outflows_fnc_act = NIO_CUBE()
        self.net_cash_flows_fnc_act = NIO_CUBE()
        self.eff_fx_flu_cash = NIO_CUBE()
        self.net_incr_cash_cash_equ = NIO_CUBE()
        self.cash_cash_equ_beg_period = NIO_CUBE()
        self.cash_cash_equ_end_period = NIO_CUBE()
        self.net_profit = NIO_CUBE()
        self.unconfirmed_invest_loss = NIO_CUBE()
        self.plus_prov_depr_assets = NIO_CUBE()
        self.depr_fa_coga_dpba = NIO_CUBE()
        self.amort_intang_assets = NIO_CUBE()
        self.amort_lt_deferred_exp = NIO_CUBE()
        self.decr_deferred_exp = NIO_CUBE()
        self.incr_acc_exp = NIO_CUBE()
        self.loss_disp_fiolta = NIO_CUBE()
        self.loss_scr_fa = NIO_CUBE()
        self.loss_fv_chg = NIO_CUBE()
        self.fin_exp = NIO_CUBE()
        self.invest_loss = NIO_CUBE()
        self.decr_deferred_inc_tax_assets = NIO_CUBE()
        self.incr_deferred_inc_tax_liab = NIO_CUBE()
        self.decr_inventories = NIO_CUBE()
        self.decr_oper_payable = NIO_CUBE()
        self.incr_oper_payable = NIO_CUBE()
        self.im_net_cash_flows_oper_act = NIO_CUBE()
        self.conv_debt_into_cap = NIO_CUBE()
        self.conv_corp_bonds_due_within_1y = NIO_CUBE()
        self.fa_fnc_leases = NIO_CUBE()
        self.end_bal_cash = NIO_CUBE()
        self.less_beg_bal_cash = NIO_CUBE()
        self.plus_end_bal_cash_equ = NIO_CUBE()
        self.less_beg_bal_cash_equ = NIO_CUBE()
        self.im_net_incr_cash_cash_equ = NIO_CUBE()
        self.free_cash_flow = NIO_CUBE()
        self.spe_bal_cash_inflows_oper = NIO_CUBE()
        self.tot_bal_cash_inflows_oper = NIO_CUBE()
        self.spe_bal_cash_outflows_oper = NIO_CUBE()
        self.tot_bal_cash_outflows_oper = NIO_CUBE()
        self.tot_bal_netcash_outflows_oper = NIO_CUBE()
        self.spe_bal_cash_inflows_inv = NIO_CUBE()
        self.tot_bal_cash_inflows_inv = NIO_CUBE()
        self.spe_bal_cash_outflows_inv = NIO_CUBE()
        self.tot_bal_cash_outflows_inv = NIO_CUBE()
        self.tot_bal_netcash_outflows_inv = NIO_CUBE()
        self.spe_bal_cash_inflows_fnc = NIO_CUBE()
        self.tot_bal_cash_inflows_fnc = NIO_CUBE()
        self.spe_bal_cash_outflows_fnc = NIO_CUBE()
        self.tot_bal_cash_outflows_fnc = NIO_CUBE()
        self.tot_bal_netcash_outflows_fnc = NIO_CUBE()
        self.spe_bal_netcash_inc = NIO_CUBE()
        self.tot_bal_netcash_inc = NIO_CUBE()
        self.spe_bal_netcash_equ_undir = NIO_CUBE()
        self.tot_bal_netcash_equ_undir = NIO_CUBE()
        self.spe_bal_netcash_inc_undir = NIO_CUBE()
        self.tot_bal_netcash_inc_undir = NIO_CUBE()
        self.s_dismantle_capital_add_net = NIO_CUBE()
        self.is_calculation = NIO_CUBE()
        self.securitie_netcash_received = NIO_CUBE()
        self.other_impair_loss_assets = NIO_CUBE()
        self.credit_impairment_loss = NIO_CUBE()
        self.right_use_assets_dep = NIO_CUBE()
        self.other_accounts = NIO_CUBE()
        self.others = NIO_CUBE()
        self.melt_money_net_increase = NIO_CUBE()
        self.sec_fa_net_fina_instruments = NIO_CUBE()
        ########################################################################################################################################


    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.dataPath: str = cfg.getAttributeString('dataPath')
        self.nquarters: int = cfg.getAttributeDefault('nquarters', 12)


        ########################################################################################################################################
        # 字符串类型字段(varchar/timestamp)
        self.addData(self.report_period, self.tag + '.report_period', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.actual_ann_dt, self.tag + '.actual_ann_dt', len(uv.Dates), len(uv.Instruments), self.nquarters)

        # 数值类型字段(numeric)
        self.addData(self.statement_type, self.tag + '.statement_type', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.cash_recp_sg_and_rs, self.tag + '.cash_recp_sg_and_rs', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.recp_tax_rends, self.tag + '.recp_tax_rends', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.net_incr_dep_cob, self.tag + '.net_incr_dep_cob', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.net_incr_loans_central_bank, self.tag + '.net_incr_loans_central_bank', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.net_incr_fund_borr_ofi, self.tag + '.net_incr_fund_borr_ofi', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.cash_recp_prem_orig_inco, self.tag + '.cash_recp_prem_orig_inco', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.net_incr_insured_dep, self.tag + '.net_incr_insured_dep', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.net_cash_received_reinsu_bus, self.tag + '.net_cash_received_reinsu_bus', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.net_incr_disp_tfa, self.tag + '.net_incr_disp_tfa', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.net_incr_int_handling_chrg, self.tag + '.net_incr_int_handling_chrg', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.net_incr_disp_faas, self.tag + '.net_incr_disp_faas', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.net_incr_loans_other_bank, self.tag + '.net_incr_loans_other_bank', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.net_incr_repurch_bus_fund, self.tag + '.net_incr_repurch_bus_fund', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.other_cash_recp_ral_oper_act, self.tag + '.other_cash_recp_ral_oper_act', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.stot_cash_inflows_oper_act, self.tag + '.stot_cash_inflows_oper_act', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.cash_pay_goods_purch_serv_rec, self.tag + '.cash_pay_goods_purch_serv_rec', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.cash_pay_beh_empl, self.tag + '.cash_pay_beh_empl', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.pay_all_typ_tax, self.tag + '.pay_all_typ_tax', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.net_incr_clients_loan_adv, self.tag + '.net_incr_clients_loan_adv', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.net_incr_dep_cbob, self.tag + '.net_incr_dep_cbob', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.cash_pay_claims_orig_inco, self.tag + '.cash_pay_claims_orig_inco', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.handling_chrg_paid, self.tag + '.handling_chrg_paid', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.comm_insur_plcy_paid, self.tag + '.comm_insur_plcy_paid', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.other_cash_pay_ral_oper_act, self.tag + '.other_cash_pay_ral_oper_act', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.stot_cash_outflows_oper_act, self.tag + '.stot_cash_outflows_oper_act', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.net_cash_flows_oper_act, self.tag + '.net_cash_flows_oper_act', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.cash_recp_disp_withdrwl_invest, self.tag + '.cash_recp_disp_withdrwl_invest', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.cash_recp_return_invest, self.tag + '.cash_recp_return_invest', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.net_cash_recp_disp_fiolta, self.tag + '.net_cash_recp_disp_fiolta', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.net_cash_recp_disp_sobu, self.tag + '.net_cash_recp_disp_sobu', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.other_cash_recp_ral_inv_act, self.tag + '.other_cash_recp_ral_inv_act', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.stot_cash_inflows_inv_act, self.tag + '.stot_cash_inflows_inv_act', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.cash_pay_acq_const_fiolta, self.tag + '.cash_pay_acq_const_fiolta', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.cash_paid_invest, self.tag + '.cash_paid_invest', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.net_cash_pay_aquis_sobu, self.tag + '.net_cash_pay_aquis_sobu', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.other_cash_pay_ral_inv_act, self.tag + '.other_cash_pay_ral_inv_act', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.net_incr_pledge_loan, self.tag + '.net_incr_pledge_loan', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.stot_cash_outflows_inv_act, self.tag + '.stot_cash_outflows_inv_act', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.net_cash_flows_inv_act, self.tag + '.net_cash_flows_inv_act', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.cash_recp_cap_contrib, self.tag + '.cash_recp_cap_contrib', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.incl_cash_rec_saims, self.tag + '.incl_cash_rec_saims', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.cash_recp_borrow, self.tag + '.cash_recp_borrow', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.proc_issue_bonds, self.tag + '.proc_issue_bonds', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.other_cash_recp_ral_fnc_act, self.tag + '.other_cash_recp_ral_fnc_act', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.stot_cash_inflows_fnc_act, self.tag + '.stot_cash_inflows_fnc_act', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.cash_prepay_amt_borr, self.tag + '.cash_prepay_amt_borr', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.cash_pay_dist_dpcp_int_exp, self.tag + '.cash_pay_dist_dpcp_int_exp', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.incl_dvd_profit_paid_sc_ms, self.tag + '.incl_dvd_profit_paid_sc_ms', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.other_cash_pay_ral_fnc_act, self.tag + '.other_cash_pay_ral_fnc_act', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.stot_cash_outflows_fnc_act, self.tag + '.stot_cash_outflows_fnc_act', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.net_cash_flows_fnc_act, self.tag + '.net_cash_flows_fnc_act', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.eff_fx_flu_cash, self.tag + '.eff_fx_flu_cash', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.net_incr_cash_cash_equ, self.tag + '.net_incr_cash_cash_equ', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.cash_cash_equ_beg_period, self.tag + '.cash_cash_equ_beg_period', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.cash_cash_equ_end_period, self.tag + '.cash_cash_equ_end_period', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.net_profit, self.tag + '.net_profit', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.unconfirmed_invest_loss, self.tag + '.unconfirmed_invest_loss', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.plus_prov_depr_assets, self.tag + '.plus_prov_depr_assets', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.depr_fa_coga_dpba, self.tag + '.depr_fa_coga_dpba', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.amort_intang_assets, self.tag + '.amort_intang_assets', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.amort_lt_deferred_exp, self.tag + '.amort_lt_deferred_exp', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.decr_deferred_exp, self.tag + '.decr_deferred_exp', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.incr_acc_exp, self.tag + '.incr_acc_exp', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.loss_disp_fiolta, self.tag + '.loss_disp_fiolta', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.loss_scr_fa, self.tag + '.loss_scr_fa', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.loss_fv_chg, self.tag + '.loss_fv_chg', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.fin_exp, self.tag + '.fin_exp', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.invest_loss, self.tag + '.invest_loss', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.decr_deferred_inc_tax_assets, self.tag + '.decr_deferred_inc_tax_assets', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.incr_deferred_inc_tax_liab, self.tag + '.incr_deferred_inc_tax_liab', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.decr_inventories, self.tag + '.decr_inventories', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.decr_oper_payable, self.tag + '.decr_oper_payable', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.incr_oper_payable, self.tag + '.incr_oper_payable', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.im_net_cash_flows_oper_act, self.tag + '.im_net_cash_flows_oper_act', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.conv_debt_into_cap, self.tag + '.conv_debt_into_cap', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.conv_corp_bonds_due_within_1y, self.tag + '.conv_corp_bonds_due_within_1y', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.fa_fnc_leases, self.tag + '.fa_fnc_leases', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.end_bal_cash, self.tag + '.end_bal_cash', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.less_beg_bal_cash, self.tag + '.less_beg_bal_cash', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.plus_end_bal_cash_equ, self.tag + '.plus_end_bal_cash_equ', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.less_beg_bal_cash_equ, self.tag + '.less_beg_bal_cash_equ', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.im_net_incr_cash_cash_equ, self.tag + '.im_net_incr_cash_cash_equ', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.free_cash_flow, self.tag + '.free_cash_flow', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.spe_bal_cash_inflows_oper, self.tag + '.spe_bal_cash_inflows_oper', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.tot_bal_cash_inflows_oper, self.tag + '.tot_bal_cash_inflows_oper', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.spe_bal_cash_outflows_oper, self.tag + '.spe_bal_cash_outflows_oper', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.tot_bal_cash_outflows_oper, self.tag + '.tot_bal_cash_outflows_oper', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.tot_bal_netcash_outflows_oper, self.tag + '.tot_bal_netcash_outflows_oper', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.spe_bal_cash_inflows_inv, self.tag + '.spe_bal_cash_inflows_inv', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.tot_bal_cash_inflows_inv, self.tag + '.tot_bal_cash_inflows_inv', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.spe_bal_cash_outflows_inv, self.tag + '.spe_bal_cash_outflows_inv', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.tot_bal_cash_outflows_inv, self.tag + '.tot_bal_cash_outflows_inv', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.tot_bal_netcash_outflows_inv, self.tag + '.tot_bal_netcash_outflows_inv', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.spe_bal_cash_inflows_fnc, self.tag + '.spe_bal_cash_inflows_fnc', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.tot_bal_cash_inflows_fnc, self.tag + '.tot_bal_cash_inflows_fnc', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.spe_bal_cash_outflows_fnc, self.tag + '.spe_bal_cash_outflows_fnc', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.tot_bal_cash_outflows_fnc, self.tag + '.tot_bal_cash_outflows_fnc', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.tot_bal_netcash_outflows_fnc, self.tag + '.tot_bal_netcash_outflows_fnc', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.spe_bal_netcash_inc, self.tag + '.spe_bal_netcash_inc', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.tot_bal_netcash_inc, self.tag + '.tot_bal_netcash_inc', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.spe_bal_netcash_equ_undir, self.tag + '.spe_bal_netcash_equ_undir', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.tot_bal_netcash_equ_undir, self.tag + '.tot_bal_netcash_equ_undir', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.spe_bal_netcash_inc_undir, self.tag + '.spe_bal_netcash_inc_undir', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.tot_bal_netcash_inc_undir, self.tag + '.tot_bal_netcash_inc_undir', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.s_dismantle_capital_add_net, self.tag + '.s_dismantle_capital_add_net', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.is_calculation, self.tag + '.is_calculation', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.securitie_netcash_received, self.tag + '.securitie_netcash_received', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.other_impair_loss_assets, self.tag + '.other_impair_loss_assets', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.credit_impairment_loss, self.tag + '.credit_impairment_loss', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.right_use_assets_dep, self.tag + '.right_use_assets_dep', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.other_accounts, self.tag + '.other_accounts', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.others, self.tag + '.others', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.melt_money_net_increase, self.tag + '.melt_money_net_increase', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.sec_fa_net_fina_instruments, self.tag + '.sec_fa_net_fina_instruments', len(uv.Dates), len(uv.Instruments), self.nquarters)
        ########################################################################################################################################


        self.stocks = glob.glob(self.dataPath + '/*')
        self.dfs: dict[str, pd.DataFrame] = {}
        self.iis: dict[str, int] = {}

        stocks = []
        for stock in self.stocks:
            stock_name = stock.rsplit('/', 1)[-1].split('.', 1)[0]
            # print(stock_name, uv.Instruments.lookup(stock_name))
            if stock_name not in uv.Instruments.data:
                continue
            
            df = pd.read_csv(stock)
            df['ann_dt'] = pd.to_datetime(df['ann_dt'], format='%Y%m%d', errors='raise')

            stocks.append(stock_name)
            self.iis.update({stock_name: uv.Instruments.lookup(stock_name)})
            self.dfs.update({stock_name: df})

        self.stocks = stocks


    def registration(self):
        #######################################################################################################################
        # 字符串类型字段(varchar/timestamp)
        dr.registerData(self.mid, self.report_period, self.tag + '.report_period')
        dr.registerData(self.mid, self.actual_ann_dt, self.tag + '.actual_ann_dt')

        # 数值类型字段(numeric)
        dr.registerData(self.mid, self.statement_type, self.tag + '.statement_type')
        dr.registerData(self.mid, self.cash_recp_sg_and_rs, self.tag + '.cash_recp_sg_and_rs')
        dr.registerData(self.mid, self.recp_tax_rends, self.tag + '.recp_tax_rends')
        dr.registerData(self.mid, self.net_incr_dep_cob, self.tag + '.net_incr_dep_cob')
        dr.registerData(self.mid, self.net_incr_loans_central_bank, self.tag + '.net_incr_loans_central_bank')
        dr.registerData(self.mid, self.net_incr_fund_borr_ofi, self.tag + '.net_incr_fund_borr_ofi')
        dr.registerData(self.mid, self.cash_recp_prem_orig_inco, self.tag + '.cash_recp_prem_orig_inco')
        dr.registerData(self.mid, self.net_incr_insured_dep, self.tag + '.net_incr_insured_dep')
        dr.registerData(self.mid, self.net_cash_received_reinsu_bus, self.tag + '.net_cash_received_reinsu_bus')
        dr.registerData(self.mid, self.net_incr_disp_tfa, self.tag + '.net_incr_disp_tfa')
        dr.registerData(self.mid, self.net_incr_int_handling_chrg, self.tag + '.net_incr_int_handling_chrg')
        dr.registerData(self.mid, self.net_incr_disp_faas, self.tag + '.net_incr_disp_faas')
        dr.registerData(self.mid, self.net_incr_loans_other_bank, self.tag + '.net_incr_loans_other_bank')
        dr.registerData(self.mid, self.net_incr_repurch_bus_fund, self.tag + '.net_incr_repurch_bus_fund')
        dr.registerData(self.mid, self.other_cash_recp_ral_oper_act, self.tag + '.other_cash_recp_ral_oper_act')
        dr.registerData(self.mid, self.stot_cash_inflows_oper_act, self.tag + '.stot_cash_inflows_oper_act')
        dr.registerData(self.mid, self.cash_pay_goods_purch_serv_rec, self.tag + '.cash_pay_goods_purch_serv_rec')
        dr.registerData(self.mid, self.cash_pay_beh_empl, self.tag + '.cash_pay_beh_empl')
        dr.registerData(self.mid, self.pay_all_typ_tax, self.tag + '.pay_all_typ_tax')
        dr.registerData(self.mid, self.net_incr_clients_loan_adv, self.tag + '.net_incr_clients_loan_adv')
        dr.registerData(self.mid, self.net_incr_dep_cbob, self.tag + '.net_incr_dep_cbob')
        dr.registerData(self.mid, self.cash_pay_claims_orig_inco, self.tag + '.cash_pay_claims_orig_inco')
        dr.registerData(self.mid, self.handling_chrg_paid, self.tag + '.handling_chrg_paid')
        dr.registerData(self.mid, self.comm_insur_plcy_paid, self.tag + '.comm_insur_plcy_paid')
        dr.registerData(self.mid, self.other_cash_pay_ral_oper_act, self.tag + '.other_cash_pay_ral_oper_act')
        dr.registerData(self.mid, self.stot_cash_outflows_oper_act, self.tag + '.stot_cash_outflows_oper_act')
        dr.registerData(self.mid, self.net_cash_flows_oper_act, self.tag + '.net_cash_flows_oper_act')
        dr.registerData(self.mid, self.cash_recp_disp_withdrwl_invest, self.tag + '.cash_recp_disp_withdrwl_invest')
        dr.registerData(self.mid, self.cash_recp_return_invest, self.tag + '.cash_recp_return_invest')
        dr.registerData(self.mid, self.net_cash_recp_disp_fiolta, self.tag + '.net_cash_recp_disp_fiolta')
        dr.registerData(self.mid, self.net_cash_recp_disp_sobu, self.tag + '.net_cash_recp_disp_sobu')
        dr.registerData(self.mid, self.other_cash_recp_ral_inv_act, self.tag + '.other_cash_recp_ral_inv_act')
        dr.registerData(self.mid, self.stot_cash_inflows_inv_act, self.tag + '.stot_cash_inflows_inv_act')
        dr.registerData(self.mid, self.cash_pay_acq_const_fiolta, self.tag + '.cash_pay_acq_const_fiolta')
        dr.registerData(self.mid, self.cash_paid_invest, self.tag + '.cash_paid_invest')
        dr.registerData(self.mid, self.net_cash_pay_aquis_sobu, self.tag + '.net_cash_pay_aquis_sobu')
        dr.registerData(self.mid, self.other_cash_pay_ral_inv_act, self.tag + '.other_cash_pay_ral_inv_act')
        dr.registerData(self.mid, self.net_incr_pledge_loan, self.tag + '.net_incr_pledge_loan')
        dr.registerData(self.mid, self.stot_cash_outflows_inv_act, self.tag + '.stot_cash_outflows_inv_act')
        dr.registerData(self.mid, self.net_cash_flows_inv_act, self.tag + '.net_cash_flows_inv_act')
        dr.registerData(self.mid, self.cash_recp_cap_contrib, self.tag + '.cash_recp_cap_contrib')
        dr.registerData(self.mid, self.incl_cash_rec_saims, self.tag + '.incl_cash_rec_saims')
        dr.registerData(self.mid, self.cash_recp_borrow, self.tag + '.cash_recp_borrow')
        dr.registerData(self.mid, self.proc_issue_bonds, self.tag + '.proc_issue_bonds')
        dr.registerData(self.mid, self.other_cash_recp_ral_fnc_act, self.tag + '.other_cash_recp_ral_fnc_act')
        dr.registerData(self.mid, self.stot_cash_inflows_fnc_act, self.tag + '.stot_cash_inflows_fnc_act')
        dr.registerData(self.mid, self.cash_prepay_amt_borr, self.tag + '.cash_prepay_amt_borr')
        dr.registerData(self.mid, self.cash_pay_dist_dpcp_int_exp, self.tag + '.cash_pay_dist_dpcp_int_exp')
        dr.registerData(self.mid, self.incl_dvd_profit_paid_sc_ms, self.tag + '.incl_dvd_profit_paid_sc_ms')
        dr.registerData(self.mid, self.other_cash_pay_ral_fnc_act, self.tag + '.other_cash_pay_ral_fnc_act')
        dr.registerData(self.mid, self.stot_cash_outflows_fnc_act, self.tag + '.stot_cash_outflows_fnc_act')
        dr.registerData(self.mid, self.net_cash_flows_fnc_act, self.tag + '.net_cash_flows_fnc_act')
        dr.registerData(self.mid, self.eff_fx_flu_cash, self.tag + '.eff_fx_flu_cash')
        dr.registerData(self.mid, self.net_incr_cash_cash_equ, self.tag + '.net_incr_cash_cash_equ')
        dr.registerData(self.mid, self.cash_cash_equ_beg_period, self.tag + '.cash_cash_equ_beg_period')
        dr.registerData(self.mid, self.cash_cash_equ_end_period, self.tag + '.cash_cash_equ_end_period')
        dr.registerData(self.mid, self.net_profit, self.tag + '.net_profit')
        dr.registerData(self.mid, self.unconfirmed_invest_loss, self.tag + '.unconfirmed_invest_loss')
        dr.registerData(self.mid, self.plus_prov_depr_assets, self.tag + '.plus_prov_depr_assets')
        dr.registerData(self.mid, self.depr_fa_coga_dpba, self.tag + '.depr_fa_coga_dpba')
        dr.registerData(self.mid, self.amort_intang_assets, self.tag + '.amort_intang_assets')
        dr.registerData(self.mid, self.amort_lt_deferred_exp, self.tag + '.amort_lt_deferred_exp')
        dr.registerData(self.mid, self.decr_deferred_exp, self.tag + '.decr_deferred_exp')
        dr.registerData(self.mid, self.incr_acc_exp, self.tag + '.incr_acc_exp')
        dr.registerData(self.mid, self.loss_disp_fiolta, self.tag + '.loss_disp_fiolta')
        dr.registerData(self.mid, self.loss_scr_fa, self.tag + '.loss_scr_fa')
        dr.registerData(self.mid, self.loss_fv_chg, self.tag + '.loss_fv_chg')
        dr.registerData(self.mid, self.fin_exp, self.tag + '.fin_exp')
        dr.registerData(self.mid, self.invest_loss, self.tag + '.invest_loss')
        dr.registerData(self.mid, self.decr_deferred_inc_tax_assets, self.tag + '.decr_deferred_inc_tax_assets')
        dr.registerData(self.mid, self.incr_deferred_inc_tax_liab, self.tag + '.incr_deferred_inc_tax_liab')
        dr.registerData(self.mid, self.decr_inventories, self.tag + '.decr_inventories')
        dr.registerData(self.mid, self.decr_oper_payable, self.tag + '.decr_oper_payable')
        dr.registerData(self.mid, self.incr_oper_payable, self.tag + '.incr_oper_payable')
        dr.registerData(self.mid, self.im_net_cash_flows_oper_act, self.tag + '.im_net_cash_flows_oper_act')
        dr.registerData(self.mid, self.conv_debt_into_cap, self.tag + '.conv_debt_into_cap')
        dr.registerData(self.mid, self.conv_corp_bonds_due_within_1y, self.tag + '.conv_corp_bonds_due_within_1y')
        dr.registerData(self.mid, self.fa_fnc_leases, self.tag + '.fa_fnc_leases')
        dr.registerData(self.mid, self.end_bal_cash, self.tag + '.end_bal_cash')
        dr.registerData(self.mid, self.less_beg_bal_cash, self.tag + '.less_beg_bal_cash')
        dr.registerData(self.mid, self.plus_end_bal_cash_equ, self.tag + '.plus_end_bal_cash_equ')
        dr.registerData(self.mid, self.less_beg_bal_cash_equ, self.tag + '.less_beg_bal_cash_equ')
        dr.registerData(self.mid, self.im_net_incr_cash_cash_equ, self.tag + '.im_net_incr_cash_cash_equ')
        dr.registerData(self.mid, self.free_cash_flow, self.tag + '.free_cash_flow')
        dr.registerData(self.mid, self.spe_bal_cash_inflows_oper, self.tag + '.spe_bal_cash_inflows_oper')
        dr.registerData(self.mid, self.tot_bal_cash_inflows_oper, self.tag + '.tot_bal_cash_inflows_oper')
        dr.registerData(self.mid, self.spe_bal_cash_outflows_oper, self.tag + '.spe_bal_cash_outflows_oper')
        dr.registerData(self.mid, self.tot_bal_cash_outflows_oper, self.tag + '.tot_bal_cash_outflows_oper')
        dr.registerData(self.mid, self.tot_bal_netcash_outflows_oper, self.tag + '.tot_bal_netcash_outflows_oper')
        dr.registerData(self.mid, self.spe_bal_cash_inflows_inv, self.tag + '.spe_bal_cash_inflows_inv')
        dr.registerData(self.mid, self.tot_bal_cash_inflows_inv, self.tag + '.tot_bal_cash_inflows_inv')
        dr.registerData(self.mid, self.spe_bal_cash_outflows_inv, self.tag + '.spe_bal_cash_outflows_inv')
        dr.registerData(self.mid, self.tot_bal_cash_outflows_inv, self.tag + '.tot_bal_cash_outflows_inv')
        dr.registerData(self.mid, self.tot_bal_netcash_outflows_inv, self.tag + '.tot_bal_netcash_outflows_inv')
        dr.registerData(self.mid, self.spe_bal_cash_inflows_fnc, self.tag + '.spe_bal_cash_inflows_fnc')
        dr.registerData(self.mid, self.tot_bal_cash_inflows_fnc, self.tag + '.tot_bal_cash_inflows_fnc')
        dr.registerData(self.mid, self.spe_bal_cash_outflows_fnc, self.tag + '.spe_bal_cash_outflows_fnc')
        dr.registerData(self.mid, self.tot_bal_cash_outflows_fnc, self.tag + '.tot_bal_cash_outflows_fnc')
        dr.registerData(self.mid, self.tot_bal_netcash_outflows_fnc, self.tag + '.tot_bal_netcash_outflows_fnc')
        dr.registerData(self.mid, self.spe_bal_netcash_inc, self.tag + '.spe_bal_netcash_inc')
        dr.registerData(self.mid, self.tot_bal_netcash_inc, self.tag + '.tot_bal_netcash_inc')
        dr.registerData(self.mid, self.spe_bal_netcash_equ_undir, self.tag + '.spe_bal_netcash_equ_undir')
        dr.registerData(self.mid, self.tot_bal_netcash_equ_undir, self.tag + '.tot_bal_netcash_equ_undir')
        dr.registerData(self.mid, self.spe_bal_netcash_inc_undir, self.tag + '.spe_bal_netcash_inc_undir')
        dr.registerData(self.mid, self.tot_bal_netcash_inc_undir, self.tag + '.tot_bal_netcash_inc_undir')
        dr.registerData(self.mid, self.s_dismantle_capital_add_net, self.tag + '.s_dismantle_capital_add_net')
        dr.registerData(self.mid, self.is_calculation, self.tag + '.is_calculation')
        dr.registerData(self.mid, self.securitie_netcash_received, self.tag + '.securitie_netcash_received')
        dr.registerData(self.mid, self.other_impair_loss_assets, self.tag + '.other_impair_loss_assets')
        dr.registerData(self.mid, self.credit_impairment_loss, self.tag + '.credit_impairment_loss')
        dr.registerData(self.mid, self.right_use_assets_dep, self.tag + '.right_use_assets_dep')
        dr.registerData(self.mid, self.other_accounts, self.tag + '.other_accounts')
        dr.registerData(self.mid, self.others, self.tag + '.others')
        dr.registerData(self.mid, self.melt_money_net_increase, self.tag + '.melt_money_net_increase')
        dr.registerData(self.mid, self.sec_fa_net_fina_instruments, self.tag + '.sec_fa_net_fina_instruments')
        #######################################################################################################################


    def loadDay(self, di):
        self.fillnan(di)
        date = pd.to_datetime(uv.Dates[di], format='%Y%m%d')


        def work(stock_name):
            try:
                # 1.
                ii = self.iis[stock_name]
                df = self.dfs[stock_name]

                # 2.
                df_after_di: pd.DataFrame = df[df['ann_dt'] <= date]
                if df_after_di.empty:
                    # logging.debug(f"df empty.")
                    return
                
                if len(df_after_di) > self.nquarters:
                    df_window = df_after_di.tail(self.nquarters)
                else:
                    df_window = df_after_di
                
                logging.info(f"Handling {di} {ii}")

                # 3.
                qi = 0
                for i in range(len(df_window) - 1, -1, -1):
                    df_qi = df_window.iloc[i]
                    if df_qi.empty:
                        logging.warning(f"df_qi empty. len of df_window: {len(df_window)}, df_after_di: {df_after_di}, i: {i}")
                        continue

                    logging.info(f"xxx[{di}, {qi}, {ii}] = df_qi['xxx']")

                    #######################################################################################################################
                    # 字符串类型字段(varchar/timestamp)
                    self.report_period[di, qi, ii] = int(df_qi['report_period'])
                    self.actual_ann_dt[di, qi, ii] = int(df_qi['actual_ann_dt'])

                    # 数值类型字段(numeric)
                    self.statement_type[di, qi, ii] = df_qi['statement_type']
                    self.cash_recp_sg_and_rs[di, qi, ii] = df_qi['cash_recp_sg_and_rs']
                    self.recp_tax_rends[di, qi, ii] = df_qi['recp_tax_rends']
                    self.net_incr_dep_cob[di, qi, ii] = df_qi['net_incr_dep_cob']
                    self.net_incr_loans_central_bank[di, qi, ii] = df_qi['net_incr_loans_central_bank']
                    self.net_incr_fund_borr_ofi[di, qi, ii] = df_qi['net_incr_fund_borr_ofi']
                    self.cash_recp_prem_orig_inco[di, qi, ii] = df_qi['cash_recp_prem_orig_inco']
                    self.net_incr_insured_dep[di, qi, ii] = df_qi['net_incr_insured_dep']
                    self.net_cash_received_reinsu_bus[di, qi, ii] = df_qi['net_cash_received_reinsu_bus']
                    self.net_incr_disp_tfa[di, qi, ii] = df_qi['net_incr_disp_tfa']
                    self.net_incr_int_handling_chrg[di, qi, ii] = df_qi['net_incr_int_handling_chrg']
                    self.net_incr_disp_faas[di, qi, ii] = df_qi['net_incr_disp_faas']
                    self.net_incr_loans_other_bank[di, qi, ii] = df_qi['net_incr_loans_other_bank']
                    self.net_incr_repurch_bus_fund[di, qi, ii] = df_qi['net_incr_repurch_bus_fund']
                    self.other_cash_recp_ral_oper_act[di, qi, ii] = df_qi['other_cash_recp_ral_oper_act']
                    self.stot_cash_inflows_oper_act[di, qi, ii] = df_qi['stot_cash_inflows_oper_act']
                    self.cash_pay_goods_purch_serv_rec[di, qi, ii] = df_qi['cash_pay_goods_purch_serv_rec']
                    self.cash_pay_beh_empl[di, qi, ii] = df_qi['cash_pay_beh_empl']
                    self.pay_all_typ_tax[di, qi, ii] = df_qi['pay_all_typ_tax']
                    self.net_incr_clients_loan_adv[di, qi, ii] = df_qi['net_incr_clients_loan_adv']
                    self.net_incr_dep_cbob[di, qi, ii] = df_qi['net_incr_dep_cbob']
                    self.cash_pay_claims_orig_inco[di, qi, ii] = df_qi['cash_pay_claims_orig_inco']
                    self.handling_chrg_paid[di, qi, ii] = df_qi['handling_chrg_paid']
                    self.comm_insur_plcy_paid[di, qi, ii] = df_qi['comm_insur_plcy_paid']
                    self.other_cash_pay_ral_oper_act[di, qi, ii] = df_qi['other_cash_pay_ral_oper_act']
                    self.stot_cash_outflows_oper_act[di, qi, ii] = df_qi['stot_cash_outflows_oper_act']
                    self.net_cash_flows_oper_act[di, qi, ii] = df_qi['net_cash_flows_oper_act']
                    self.cash_recp_disp_withdrwl_invest[di, qi, ii] = df_qi['cash_recp_disp_withdrwl_invest']
                    self.cash_recp_return_invest[di, qi, ii] = df_qi['cash_recp_return_invest']
                    self.net_cash_recp_disp_fiolta[di, qi, ii] = df_qi['net_cash_recp_disp_fiolta']
                    self.net_cash_recp_disp_sobu[di, qi, ii] = df_qi['net_cash_recp_disp_sobu']
                    self.other_cash_recp_ral_inv_act[di, qi, ii] = df_qi['other_cash_recp_ral_inv_act']
                    self.stot_cash_inflows_inv_act[di, qi, ii] = df_qi['stot_cash_inflows_inv_act']
                    self.cash_pay_acq_const_fiolta[di, qi, ii] = df_qi['cash_pay_acq_const_fiolta']
                    self.cash_paid_invest[di, qi, ii] = df_qi['cash_paid_invest']
                    self.net_cash_pay_aquis_sobu[di, qi, ii] = df_qi['net_cash_pay_aquis_sobu']
                    self.other_cash_pay_ral_inv_act[di, qi, ii] = df_qi['other_cash_pay_ral_inv_act']
                    self.net_incr_pledge_loan[di, qi, ii] = df_qi['net_incr_pledge_loan']
                    self.stot_cash_outflows_inv_act[di, qi, ii] = df_qi['stot_cash_outflows_inv_act']
                    self.net_cash_flows_inv_act[di, qi, ii] = df_qi['net_cash_flows_inv_act']
                    self.cash_recp_cap_contrib[di, qi, ii] = df_qi['cash_recp_cap_contrib']
                    self.incl_cash_rec_saims[di, qi, ii] = df_qi['incl_cash_rec_saims']
                    self.cash_recp_borrow[di, qi, ii] = df_qi['cash_recp_borrow']
                    self.proc_issue_bonds[di, qi, ii] = df_qi['proc_issue_bonds']
                    self.other_cash_recp_ral_fnc_act[di, qi, ii] = df_qi['other_cash_recp_ral_fnc_act']
                    self.stot_cash_inflows_fnc_act[di, qi, ii] = df_qi['stot_cash_inflows_fnc_act']
                    self.cash_prepay_amt_borr[di, qi, ii] = df_qi['cash_prepay_amt_borr']
                    self.cash_pay_dist_dpcp_int_exp[di, qi, ii] = df_qi['cash_pay_dist_dpcp_int_exp']
                    self.incl_dvd_profit_paid_sc_ms[di, qi, ii] = df_qi['incl_dvd_profit_paid_sc_ms']
                    self.other_cash_pay_ral_fnc_act[di, qi, ii] = df_qi['other_cash_pay_ral_fnc_act']
                    self.stot_cash_outflows_fnc_act[di, qi, ii] = df_qi['stot_cash_outflows_fnc_act']
                    self.net_cash_flows_fnc_act[di, qi, ii] = df_qi['net_cash_flows_fnc_act']
                    self.eff_fx_flu_cash[di, qi, ii] = df_qi['eff_fx_flu_cash']
                    self.net_incr_cash_cash_equ[di, qi, ii] = df_qi['net_incr_cash_cash_equ']
                    self.cash_cash_equ_beg_period[di, qi, ii] = df_qi['cash_cash_equ_beg_period']
                    self.cash_cash_equ_end_period[di, qi, ii] = df_qi['cash_cash_equ_end_period']
                    self.net_profit[di, qi, ii] = df_qi['net_profit']
                    self.unconfirmed_invest_loss[di, qi, ii] = df_qi['unconfirmed_invest_loss']
                    self.plus_prov_depr_assets[di, qi, ii] = df_qi['plus_prov_depr_assets']
                    self.depr_fa_coga_dpba[di, qi, ii] = df_qi['depr_fa_coga_dpba']
                    self.amort_intang_assets[di, qi, ii] = df_qi['amort_intang_assets']
                    self.amort_lt_deferred_exp[di, qi, ii] = df_qi['amort_lt_deferred_exp']
                    self.decr_deferred_exp[di, qi, ii] = df_qi['decr_deferred_exp']
                    self.incr_acc_exp[di, qi, ii] = df_qi['incr_acc_exp']
                    self.loss_disp_fiolta[di, qi, ii] = df_qi['loss_disp_fiolta']
                    self.loss_scr_fa[di, qi, ii] = df_qi['loss_scr_fa']
                    self.loss_fv_chg[di, qi, ii] = df_qi['loss_fv_chg']
                    self.fin_exp[di, qi, ii] = df_qi['fin_exp']
                    self.invest_loss[di, qi, ii] = df_qi['invest_loss']
                    self.decr_deferred_inc_tax_assets[di, qi, ii] = df_qi['decr_deferred_inc_tax_assets']
                    self.incr_deferred_inc_tax_liab[di, qi, ii] = df_qi['incr_deferred_inc_tax_liab']
                    self.decr_inventories[di, qi, ii] = df_qi['decr_inventories']
                    self.decr_oper_payable[di, qi, ii] = df_qi['decr_oper_payable']
                    self.incr_oper_payable[di, qi, ii] = df_qi['incr_oper_payable']
                    self.im_net_cash_flows_oper_act[di, qi, ii] = df_qi['im_net_cash_flows_oper_act']
                    self.conv_debt_into_cap[di, qi, ii] = df_qi['conv_debt_into_cap']
                    self.conv_corp_bonds_due_within_1y[di, qi, ii] = df_qi['conv_corp_bonds_due_within_1y']
                    self.fa_fnc_leases[di, qi, ii] = df_qi['fa_fnc_leases']
                    self.end_bal_cash[di, qi, ii] = df_qi['end_bal_cash']
                    self.less_beg_bal_cash[di, qi, ii] = df_qi['less_beg_bal_cash']
                    self.plus_end_bal_cash_equ[di, qi, ii] = df_qi['plus_end_bal_cash_equ']
                    self.less_beg_bal_cash_equ[di, qi, ii] = df_qi['less_beg_bal_cash_equ']
                    self.im_net_incr_cash_cash_equ[di, qi, ii] = df_qi['im_net_incr_cash_cash_equ']
                    self.free_cash_flow[di, qi, ii] = df_qi['free_cash_flow']
                    self.spe_bal_cash_inflows_oper[di, qi, ii] = df_qi['spe_bal_cash_inflows_oper']
                    self.tot_bal_cash_inflows_oper[di, qi, ii] = df_qi['tot_bal_cash_inflows_oper']
                    self.spe_bal_cash_outflows_oper[di, qi, ii] = df_qi['spe_bal_cash_outflows_oper']
                    self.tot_bal_cash_outflows_oper[di, qi, ii] = df_qi['tot_bal_cash_outflows_oper']
                    self.tot_bal_netcash_outflows_oper[di, qi, ii] = df_qi['tot_bal_netcash_outflows_oper']
                    self.spe_bal_cash_inflows_inv[di, qi, ii] = df_qi['spe_bal_cash_inflows_inv']
                    self.tot_bal_cash_inflows_inv[di, qi, ii] = df_qi['tot_bal_cash_inflows_inv']
                    self.spe_bal_cash_outflows_inv[di, qi, ii] = df_qi['spe_bal_cash_outflows_inv']
                    self.tot_bal_cash_outflows_inv[di, qi, ii] = df_qi['tot_bal_cash_outflows_inv']
                    self.tot_bal_netcash_outflows_inv[di, qi, ii] = df_qi['tot_bal_netcash_outflows_inv']
                    self.spe_bal_cash_inflows_fnc[di, qi, ii] = df_qi['spe_bal_cash_inflows_fnc']
                    self.tot_bal_cash_inflows_fnc[di, qi, ii] = df_qi['tot_bal_cash_inflows_fnc']
                    self.spe_bal_cash_outflows_fnc[di, qi, ii] = df_qi['spe_bal_cash_outflows_fnc']
                    self.tot_bal_cash_outflows_fnc[di, qi, ii] = df_qi['tot_bal_cash_outflows_fnc']
                    self.tot_bal_netcash_outflows_fnc[di, qi, ii] = df_qi['tot_bal_netcash_outflows_fnc']
                    self.spe_bal_netcash_inc[di, qi, ii] = df_qi['spe_bal_netcash_inc']
                    self.tot_bal_netcash_inc[di, qi, ii] = df_qi['tot_bal_netcash_inc']
                    self.spe_bal_netcash_equ_undir[di, qi, ii] = df_qi['spe_bal_netcash_equ_undir']
                    self.tot_bal_netcash_equ_undir[di, qi, ii] = df_qi['tot_bal_netcash_equ_undir']
                    self.spe_bal_netcash_inc_undir[di, qi, ii] = df_qi['spe_bal_netcash_inc_undir']
                    self.tot_bal_netcash_inc_undir[di, qi, ii] = df_qi['tot_bal_netcash_inc_undir']
                    self.s_dismantle_capital_add_net[di, qi, ii] = df_qi['s_dismantle_capital_add_net']
                    self.is_calculation[di, qi, ii] = df_qi['is_calculation']
                    self.securitie_netcash_received[di, qi, ii] = df_qi['securitie_netcash_received']
                    self.other_impair_loss_assets[di, qi, ii] = df_qi['other_impair_loss_assets']
                    self.credit_impairment_loss[di, qi, ii] = df_qi['credit_impairment_loss']
                    self.right_use_assets_dep[di, qi, ii] = df_qi['right_use_assets_dep']
                    self.other_accounts[di, qi, ii] = df_qi['other_accounts']
                    self.others[di, qi, ii] = df_qi['others']
                    self.melt_money_net_increase[di, qi, ii] = df_qi['melt_money_net_increase']
                    self.sec_fa_net_fina_instruments[di, qi, ii] = df_qi['sec_fa_net_fina_instruments']
                    #######################################################################################################################

                    qi += 1

            except Exception as e:
                logging.error(f"{e}. Details:\n\
                                df_qi empty:\n\
                                qi: {qi}, 12 - qi - 1: {self.nquarters - qi - 1},\n\
                                len of df_qi {len(df_qi)}, df_qi: {df_qi}")
                return



        for stock_name in self.stocks:
            work(stock_name)