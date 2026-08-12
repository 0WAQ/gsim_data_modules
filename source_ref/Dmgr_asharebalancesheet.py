
from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils import Calendar
import numpy as np
import os
import operator
import csv

class Dmgrasharebalancesheet(DataManagerMapped):
    def __init__(self, ):
        DataManagerMapped.__init__(self, )
        self.dataPath = None
        self.backfill = True
        self.report_period = NIO_MATRIX()
        self.statement_type = NIO_MATRIX()
        self.monetary_cap = NIO_MATRIX()
        self.tradable_fin_assets = NIO_MATRIX()
        self.notes_rcv = NIO_MATRIX()
        self.acct_rcv = NIO_MATRIX()
        self.oth_rcv = NIO_MATRIX()
        self.prepay = NIO_MATRIX()
        self.dvd_rcv = NIO_MATRIX()
        self.int_rcv = NIO_MATRIX()
        self.inventories = NIO_MATRIX()
        self.consumptive_bio_assets = NIO_MATRIX()
        self.deferred_exp = NIO_MATRIX()
        self.non_cur_assets_due_within_1y = NIO_MATRIX()
        self.settle_rsrv = NIO_MATRIX()
        self.loans_to_oth_banks = NIO_MATRIX()
        self.prem_rcv = NIO_MATRIX()
        self.rcv_from_reinsurer = NIO_MATRIX()
        self.rcv_from_ceded_insur_cont_rsrv = NIO_MATRIX()
        self.red_monetary_cap_for_sale = NIO_MATRIX()
        self.oth_cur_assets = NIO_MATRIX()
        self.tot_cur_assets = NIO_MATRIX()
        self.fin_assets_avail_for_sale = NIO_MATRIX()
        self.held_to_mty_invest = NIO_MATRIX()
        self.long_term_eqy_invest = NIO_MATRIX()
        self.invest_real_estate = NIO_MATRIX()
        self.time_deposits = NIO_MATRIX()
        self.oth_assets = NIO_MATRIX()
        self.long_term_rec = NIO_MATRIX()
        self.fix_assets = NIO_MATRIX()
        self.const_in_prog = NIO_MATRIX()
        self.proj_matl = NIO_MATRIX()
        self.fix_assets_disp = NIO_MATRIX()
        self.productive_bio_assets = NIO_MATRIX()
        self.oil_and_natural_gas_assets = NIO_MATRIX()
        self.intang_assets = NIO_MATRIX()
        self.r_and_d_costs = NIO_MATRIX()
        self.goodwill = NIO_MATRIX()
        self.long_term_deferred_exp = NIO_MATRIX()
        self.deferred_tax_assets = NIO_MATRIX()
        self.loans_and_adv_granted = NIO_MATRIX()
        self.oth_non_cur_assets = NIO_MATRIX()
        self.tot_non_cur_assets = NIO_MATRIX()
        self.cash_deposits_central_bank = NIO_MATRIX()
        self.asset_dep_oth_banks_fin_inst = NIO_MATRIX()
        self.precious_metals = NIO_MATRIX()
        self.derivative_fin_assets = NIO_MATRIX()
        self.agency_bus_assets = NIO_MATRIX()
        self.subr_rec = NIO_MATRIX()
        self.rcv_ceded_unearned_prem_rsrv = NIO_MATRIX()
        self.rcv_ceded_claim_rsrv = NIO_MATRIX()
        self.rcv_ceded_life_insur_rsrv = NIO_MATRIX()
        self.rcv_ceded_lt_health_insur_rsrv = NIO_MATRIX()
        self.mrgn_paid = NIO_MATRIX()
        self.insured_pledge_loan = NIO_MATRIX()
        self.cap_mrgn_paid = NIO_MATRIX()
        self.independent_acct_assets = NIO_MATRIX()
        self.clients_cap_deposit = NIO_MATRIX()
        self.clients_rsrv_settle = NIO_MATRIX()
        self.incl_seat_fees_exchange = NIO_MATRIX()
        self.rcv_invest = NIO_MATRIX()
        self.tot_assets = NIO_MATRIX()
        self.st_borrow = NIO_MATRIX()
        self.borrow_central_bank = NIO_MATRIX()
        self.deposit_received_ib_deposits = NIO_MATRIX()
        self.loans_oth_banks = NIO_MATRIX()
        self.tradable_fin_liab = NIO_MATRIX()
        self.notes_payable = NIO_MATRIX()
        self.acct_payable = NIO_MATRIX()
        self.adv_from_cust = NIO_MATRIX()
        self.fund_sales_fin_assets_rp = NIO_MATRIX()
        self.handling_charges_comm_payable = NIO_MATRIX()
        self.empl_ben_payable = NIO_MATRIX()
        self.taxes_surcharges_payable = NIO_MATRIX()
        self.int_payable = NIO_MATRIX()
        self.dvd_payable = NIO_MATRIX()
        self.oth_payable = NIO_MATRIX()
        self.acc_exp = NIO_MATRIX()
        self.deferred_inc = NIO_MATRIX()
        self.st_bonds_payable = NIO_MATRIX()
        self.payable_to_reinsurer = NIO_MATRIX()
        self.rsrv_insur_cont = NIO_MATRIX()
        self.acting_trading_sec = NIO_MATRIX()
        self.acting_uw_sec = NIO_MATRIX()
        self.non_cur_liab_due_within_1y = NIO_MATRIX()
        self.oth_cur_liab = NIO_MATRIX()
        self.tot_cur_liab = NIO_MATRIX()
        self.lt_borrow = NIO_MATRIX()
        self.bonds_payable = NIO_MATRIX()
        self.lt_payable = NIO_MATRIX()
        self.specific_item_payable = NIO_MATRIX()
        self.provisions = NIO_MATRIX()
        self.deferred_tax_liab = NIO_MATRIX()
        self.deferred_inc_non_cur_liab = NIO_MATRIX()
        self.oth_non_cur_liab = NIO_MATRIX()
        self.tot_non_cur_liab = NIO_MATRIX()
        self.liab_dep_oth_banks_fin_inst = NIO_MATRIX()
        self.derivative_fin_liab = NIO_MATRIX()
        self.cust_bank_dep = NIO_MATRIX()
        self.agency_bus_liab = NIO_MATRIX()
        self.oth_liab = NIO_MATRIX()
        self.prem_received_adv = NIO_MATRIX()
        self.deposit_received = NIO_MATRIX()
        self.insured_deposit_invest = NIO_MATRIX()
        self.unearned_prem_rsrv = NIO_MATRIX()
        self.out_loss_rsrv = NIO_MATRIX()
        self.life_insur_rsrv = NIO_MATRIX()
        self.lt_health_insur_v = NIO_MATRIX()
        self.independent_acct_liab = NIO_MATRIX()
        self.incl_pledge_loan = NIO_MATRIX()
        self.claims_payable = NIO_MATRIX()
        self.dvd_payable_insured = NIO_MATRIX()
        self.tot_liab = NIO_MATRIX()
        self.cap_stk = NIO_MATRIX()
        self.cap_rsrv = NIO_MATRIX()
        self.special_rsrv = NIO_MATRIX()
        self.surplus_rsrv = NIO_MATRIX()
        self.undistributed_profit = NIO_MATRIX()
        self.less_tsy_stk = NIO_MATRIX()
        self.prov_nom_risks = NIO_MATRIX()
        self.cnvd_diff_foreign_curr_stat = NIO_MATRIX()
        self.unconfirmed_invest_loss = NIO_MATRIX()
        self.minority_int = NIO_MATRIX()
        self.tot_shrhldr_eqy_excl_min_int = NIO_MATRIX()
        self.tot_shrhldr_eqy_incl_min_int = NIO_MATRIX()
        self.tot_liab_shrhldr_eqy = NIO_MATRIX()
        self.comp_type_code = NIO_MATRIX()
        self.actual_ann_dt = NIO_MATRIX()
        self.spe_cur_assets_diff = NIO_MATRIX()
        self.tot_cur_assets_diff = NIO_MATRIX()
        self.spe_non_cur_assets_diff = NIO_MATRIX()
        self.tot_non_cur_assets_diff = NIO_MATRIX()
        self.spe_bal_assets_diff = NIO_MATRIX()
        self.tot_bal_assets_diff = NIO_MATRIX()
        self.spe_cur_liab_diff = NIO_MATRIX()
        self.tot_cur_liab_diff = NIO_MATRIX()
        self.spe_non_cur_liab_diff = NIO_MATRIX()
        self.tot_non_cur_liab_diff = NIO_MATRIX()
        self.spe_bal_liab_diff = NIO_MATRIX()
        self.tot_bal_liab_diff = NIO_MATRIX()
        self.spe_bal_shrhldr_eqy_diff = NIO_MATRIX()
        self.tot_bal_shrhldr_eqy_diff = NIO_MATRIX()
        self.spe_bal_liab_eqy_diff = NIO_MATRIX()
        self.tot_bal_liab_eqy_diff = NIO_MATRIX()
        self.lt_payroll_payable = NIO_MATRIX()
        self.other_comp_income = NIO_MATRIX()
        self.other_equity_tools = NIO_MATRIX()
        self.other_equity_tools_p_shr = NIO_MATRIX()
        self.lending_funds = NIO_MATRIX()
        self.accounts_receivable = NIO_MATRIX()
        self.st_financing_payable = NIO_MATRIX()
        self.payables = NIO_MATRIX()
        self.tot_shr = NIO_MATRIX()
        self.hfs_assets = NIO_MATRIX()
        self.hfs_sales = NIO_MATRIX()
        self.fin_assets_cost_sharing = NIO_MATRIX()
        self.fin_assets_fair_value = NIO_MATRIX()
        self.contractual_assets = NIO_MATRIX()
        self.contract_liabilities = NIO_MATRIX()
        self.accounts_receivable_bill = NIO_MATRIX()
        self.accounts_payable = NIO_MATRIX()
        self.oth_rcv_tot = NIO_MATRIX()
        self.stm_bs_tot = NIO_MATRIX()
        self.const_in_prog_tot = NIO_MATRIX()
        self.oth_payable_tot = NIO_MATRIX()
        self.lt_payable_tot = NIO_MATRIX()
        self.debt_investment = NIO_MATRIX()
        self.other_debt_investment = NIO_MATRIX()
        self.other_equity_investment = NIO_MATRIX()
        self.other_illiquidfinancial_assets = NIO_MATRIX()
        self.other_sustainable_bond = NIO_MATRIX()
        self.receivables_financing = NIO_MATRIX()
        self.right_use_assets = NIO_MATRIX()
        self.lease_liab = NIO_MATRIX()
        return

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.dataPath = cfg.getAttributeString('dataPath')
        self.backfill = cfg.getAttributeDefault('backfill', True)
        self.addDailyData(self.report_period,self.tag + '.report_period')
        self.addDailyData(self.statement_type,self.tag + '.statement_type')
        self.addDailyData(self.monetary_cap,self.tag + '.monetary_cap')
        self.addDailyData(self.tradable_fin_assets,self.tag + '.tradable_fin_assets')
        self.addDailyData(self.notes_rcv,self.tag + '.notes_rcv')
        self.addDailyData(self.acct_rcv,self.tag + '.acct_rcv')
        self.addDailyData(self.oth_rcv,self.tag + '.oth_rcv')
        self.addDailyData(self.prepay,self.tag + '.prepay')
        self.addDailyData(self.dvd_rcv,self.tag + '.dvd_rcv')
        self.addDailyData(self.int_rcv,self.tag + '.int_rcv')
        self.addDailyData(self.inventories,self.tag + '.inventories')
        self.addDailyData(self.consumptive_bio_assets,self.tag + '.consumptive_bio_assets')
        self.addDailyData(self.deferred_exp,self.tag + '.deferred_exp')
        self.addDailyData(self.non_cur_assets_due_within_1y,self.tag + '.non_cur_assets_due_within_1y')
        self.addDailyData(self.settle_rsrv,self.tag + '.settle_rsrv')
        self.addDailyData(self.loans_to_oth_banks,self.tag + '.loans_to_oth_banks')
        self.addDailyData(self.prem_rcv,self.tag + '.prem_rcv')
        self.addDailyData(self.rcv_from_reinsurer,self.tag + '.rcv_from_reinsurer')
        self.addDailyData(self.rcv_from_ceded_insur_cont_rsrv,self.tag + '.rcv_from_ceded_insur_cont_rsrv')
        self.addDailyData(self.red_monetary_cap_for_sale,self.tag + '.red_monetary_cap_for_sale')
        self.addDailyData(self.oth_cur_assets,self.tag + '.oth_cur_assets')
        self.addDailyData(self.tot_cur_assets,self.tag + '.tot_cur_assets')
        self.addDailyData(self.fin_assets_avail_for_sale,self.tag + '.fin_assets_avail_for_sale')
        self.addDailyData(self.held_to_mty_invest,self.tag + '.held_to_mty_invest')
        self.addDailyData(self.long_term_eqy_invest,self.tag + '.long_term_eqy_invest')
        self.addDailyData(self.invest_real_estate,self.tag + '.invest_real_estate')
        self.addDailyData(self.time_deposits,self.tag + '.time_deposits')
        self.addDailyData(self.oth_assets,self.tag + '.oth_assets')
        self.addDailyData(self.long_term_rec,self.tag + '.long_term_rec')
        self.addDailyData(self.fix_assets,self.tag + '.fix_assets')
        self.addDailyData(self.const_in_prog,self.tag + '.const_in_prog')
        self.addDailyData(self.proj_matl,self.tag + '.proj_matl')
        self.addDailyData(self.fix_assets_disp,self.tag + '.fix_assets_disp')
        self.addDailyData(self.productive_bio_assets,self.tag + '.productive_bio_assets')
        self.addDailyData(self.oil_and_natural_gas_assets,self.tag + '.oil_and_natural_gas_assets')
        self.addDailyData(self.intang_assets,self.tag + '.intang_assets')
        self.addDailyData(self.r_and_d_costs,self.tag + '.r_and_d_costs')
        self.addDailyData(self.goodwill,self.tag + '.goodwill')
        self.addDailyData(self.long_term_deferred_exp,self.tag + '.long_term_deferred_exp')
        self.addDailyData(self.deferred_tax_assets,self.tag + '.deferred_tax_assets')
        self.addDailyData(self.loans_and_adv_granted,self.tag + '.loans_and_adv_granted')
        self.addDailyData(self.oth_non_cur_assets,self.tag + '.oth_non_cur_assets')
        self.addDailyData(self.tot_non_cur_assets,self.tag + '.tot_non_cur_assets')
        self.addDailyData(self.cash_deposits_central_bank,self.tag + '.cash_deposits_central_bank')
        self.addDailyData(self.asset_dep_oth_banks_fin_inst,self.tag + '.asset_dep_oth_banks_fin_inst')
        self.addDailyData(self.precious_metals,self.tag + '.precious_metals')
        self.addDailyData(self.derivative_fin_assets,self.tag + '.derivative_fin_assets')
        self.addDailyData(self.agency_bus_assets,self.tag + '.agency_bus_assets')
        self.addDailyData(self.subr_rec,self.tag + '.subr_rec')
        self.addDailyData(self.rcv_ceded_unearned_prem_rsrv,self.tag + '.rcv_ceded_unearned_prem_rsrv')
        self.addDailyData(self.rcv_ceded_claim_rsrv,self.tag + '.rcv_ceded_claim_rsrv')
        self.addDailyData(self.rcv_ceded_life_insur_rsrv,self.tag + '.rcv_ceded_life_insur_rsrv')
        self.addDailyData(self.rcv_ceded_lt_health_insur_rsrv,self.tag + '.rcv_ceded_lt_health_insur_rsrv')
        self.addDailyData(self.mrgn_paid,self.tag + '.mrgn_paid')
        self.addDailyData(self.insured_pledge_loan,self.tag + '.insured_pledge_loan')
        self.addDailyData(self.cap_mrgn_paid,self.tag + '.cap_mrgn_paid')
        self.addDailyData(self.independent_acct_assets,self.tag + '.independent_acct_assets')
        self.addDailyData(self.clients_cap_deposit,self.tag + '.clients_cap_deposit')
        self.addDailyData(self.clients_rsrv_settle,self.tag + '.clients_rsrv_settle')
        self.addDailyData(self.incl_seat_fees_exchange,self.tag + '.incl_seat_fees_exchange')
        self.addDailyData(self.rcv_invest,self.tag + '.rcv_invest')
        self.addDailyData(self.tot_assets,self.tag + '.tot_assets')
        self.addDailyData(self.st_borrow,self.tag + '.st_borrow')
        self.addDailyData(self.borrow_central_bank,self.tag + '.borrow_central_bank')
        self.addDailyData(self.deposit_received_ib_deposits,self.tag + '.deposit_received_ib_deposits')
        self.addDailyData(self.loans_oth_banks,self.tag + '.loans_oth_banks')
        self.addDailyData(self.tradable_fin_liab,self.tag + '.tradable_fin_liab')
        self.addDailyData(self.notes_payable,self.tag + '.notes_payable')
        self.addDailyData(self.acct_payable,self.tag + '.acct_payable')
        self.addDailyData(self.adv_from_cust,self.tag + '.adv_from_cust')
        self.addDailyData(self.fund_sales_fin_assets_rp,self.tag + '.fund_sales_fin_assets_rp')
        self.addDailyData(self.handling_charges_comm_payable,self.tag + '.handling_charges_comm_payable')
        self.addDailyData(self.empl_ben_payable,self.tag + '.empl_ben_payable')
        self.addDailyData(self.taxes_surcharges_payable,self.tag + '.taxes_surcharges_payable')
        self.addDailyData(self.int_payable,self.tag + '.int_payable')
        self.addDailyData(self.dvd_payable,self.tag + '.dvd_payable')
        self.addDailyData(self.oth_payable,self.tag + '.oth_payable')
        self.addDailyData(self.acc_exp,self.tag + '.acc_exp')
        self.addDailyData(self.deferred_inc,self.tag + '.deferred_inc')
        self.addDailyData(self.st_bonds_payable,self.tag + '.st_bonds_payable')
        self.addDailyData(self.payable_to_reinsurer,self.tag + '.payable_to_reinsurer')
        self.addDailyData(self.rsrv_insur_cont,self.tag + '.rsrv_insur_cont')
        self.addDailyData(self.acting_trading_sec,self.tag + '.acting_trading_sec')
        self.addDailyData(self.acting_uw_sec,self.tag + '.acting_uw_sec')
        self.addDailyData(self.non_cur_liab_due_within_1y,self.tag + '.non_cur_liab_due_within_1y')
        self.addDailyData(self.oth_cur_liab,self.tag + '.oth_cur_liab')
        self.addDailyData(self.tot_cur_liab,self.tag + '.tot_cur_liab')
        self.addDailyData(self.lt_borrow,self.tag + '.lt_borrow')
        self.addDailyData(self.bonds_payable,self.tag + '.bonds_payable')
        self.addDailyData(self.lt_payable,self.tag + '.lt_payable')
        self.addDailyData(self.specific_item_payable,self.tag + '.specific_item_payable')
        self.addDailyData(self.provisions,self.tag + '.provisions')
        self.addDailyData(self.deferred_tax_liab,self.tag + '.deferred_tax_liab')
        self.addDailyData(self.deferred_inc_non_cur_liab,self.tag + '.deferred_inc_non_cur_liab')
        self.addDailyData(self.oth_non_cur_liab,self.tag + '.oth_non_cur_liab')
        self.addDailyData(self.tot_non_cur_liab,self.tag + '.tot_non_cur_liab')
        self.addDailyData(self.liab_dep_oth_banks_fin_inst,self.tag + '.liab_dep_oth_banks_fin_inst')
        self.addDailyData(self.derivative_fin_liab,self.tag + '.derivative_fin_liab')
        self.addDailyData(self.cust_bank_dep,self.tag + '.cust_bank_dep')
        self.addDailyData(self.agency_bus_liab,self.tag + '.agency_bus_liab')
        self.addDailyData(self.oth_liab,self.tag + '.oth_liab')
        self.addDailyData(self.prem_received_adv,self.tag + '.prem_received_adv')
        self.addDailyData(self.deposit_received,self.tag + '.deposit_received')
        self.addDailyData(self.insured_deposit_invest,self.tag + '.insured_deposit_invest')
        self.addDailyData(self.unearned_prem_rsrv,self.tag + '.unearned_prem_rsrv')
        self.addDailyData(self.out_loss_rsrv,self.tag + '.out_loss_rsrv')
        self.addDailyData(self.life_insur_rsrv,self.tag + '.life_insur_rsrv')
        self.addDailyData(self.lt_health_insur_v,self.tag + '.lt_health_insur_v')
        self.addDailyData(self.independent_acct_liab,self.tag + '.independent_acct_liab')
        self.addDailyData(self.incl_pledge_loan,self.tag + '.incl_pledge_loan')
        self.addDailyData(self.claims_payable,self.tag + '.claims_payable')
        self.addDailyData(self.dvd_payable_insured,self.tag + '.dvd_payable_insured')
        self.addDailyData(self.tot_liab,self.tag + '.tot_liab')
        self.addDailyData(self.cap_stk,self.tag + '.cap_stk')
        self.addDailyData(self.cap_rsrv,self.tag + '.cap_rsrv')
        self.addDailyData(self.special_rsrv,self.tag + '.special_rsrv')
        self.addDailyData(self.surplus_rsrv,self.tag + '.surplus_rsrv')
        self.addDailyData(self.undistributed_profit,self.tag + '.undistributed_profit')
        self.addDailyData(self.less_tsy_stk,self.tag + '.less_tsy_stk')
        self.addDailyData(self.prov_nom_risks,self.tag + '.prov_nom_risks')
        self.addDailyData(self.cnvd_diff_foreign_curr_stat,self.tag + '.cnvd_diff_foreign_curr_stat')
        self.addDailyData(self.unconfirmed_invest_loss,self.tag + '.unconfirmed_invest_loss')
        self.addDailyData(self.minority_int,self.tag + '.minority_int')
        self.addDailyData(self.tot_shrhldr_eqy_excl_min_int,self.tag + '.tot_shrhldr_eqy_excl_min_int')
        self.addDailyData(self.tot_shrhldr_eqy_incl_min_int,self.tag + '.tot_shrhldr_eqy_incl_min_int')
        self.addDailyData(self.tot_liab_shrhldr_eqy,self.tag + '.tot_liab_shrhldr_eqy')
        self.addDailyData(self.comp_type_code,self.tag + '.comp_type_code')
        self.addDailyData(self.actual_ann_dt,self.tag + '.actual_ann_dt')
        self.addDailyData(self.spe_cur_assets_diff,self.tag + '.spe_cur_assets_diff')
        self.addDailyData(self.tot_cur_assets_diff,self.tag + '.tot_cur_assets_diff')
        self.addDailyData(self.spe_non_cur_assets_diff,self.tag + '.spe_non_cur_assets_diff')
        self.addDailyData(self.tot_non_cur_assets_diff,self.tag + '.tot_non_cur_assets_diff')
        self.addDailyData(self.spe_bal_assets_diff,self.tag + '.spe_bal_assets_diff')
        self.addDailyData(self.tot_bal_assets_diff,self.tag + '.tot_bal_assets_diff')
        self.addDailyData(self.spe_cur_liab_diff,self.tag + '.spe_cur_liab_diff')
        self.addDailyData(self.tot_cur_liab_diff,self.tag + '.tot_cur_liab_diff')
        self.addDailyData(self.spe_non_cur_liab_diff,self.tag + '.spe_non_cur_liab_diff')
        self.addDailyData(self.tot_non_cur_liab_diff,self.tag + '.tot_non_cur_liab_diff')
        self.addDailyData(self.spe_bal_liab_diff,self.tag + '.spe_bal_liab_diff')
        self.addDailyData(self.tot_bal_liab_diff,self.tag + '.tot_bal_liab_diff')
        self.addDailyData(self.spe_bal_shrhldr_eqy_diff,self.tag + '.spe_bal_shrhldr_eqy_diff')
        self.addDailyData(self.tot_bal_shrhldr_eqy_diff,self.tag + '.tot_bal_shrhldr_eqy_diff')
        self.addDailyData(self.spe_bal_liab_eqy_diff,self.tag + '.spe_bal_liab_eqy_diff')
        self.addDailyData(self.tot_bal_liab_eqy_diff,self.tag + '.tot_bal_liab_eqy_diff')
        self.addDailyData(self.lt_payroll_payable,self.tag + '.lt_payroll_payable')
        self.addDailyData(self.other_comp_income,self.tag + '.other_comp_income')
        self.addDailyData(self.other_equity_tools,self.tag + '.other_equity_tools')
        self.addDailyData(self.other_equity_tools_p_shr,self.tag + '.other_equity_tools_p_shr')
        self.addDailyData(self.lending_funds,self.tag + '.lending_funds')
        self.addDailyData(self.accounts_receivable,self.tag + '.accounts_receivable')
        self.addDailyData(self.st_financing_payable,self.tag + '.st_financing_payable')
        self.addDailyData(self.payables,self.tag + '.payables')
        self.addDailyData(self.tot_shr,self.tag + '.tot_shr')
        self.addDailyData(self.hfs_assets,self.tag + '.hfs_assets')
        self.addDailyData(self.hfs_sales,self.tag + '.hfs_sales')
        self.addDailyData(self.fin_assets_cost_sharing,self.tag + '.fin_assets_cost_sharing')
        self.addDailyData(self.fin_assets_fair_value,self.tag + '.fin_assets_fair_value')
        self.addDailyData(self.contractual_assets,self.tag + '.contractual_assets')
        self.addDailyData(self.contract_liabilities,self.tag + '.contract_liabilities')
        self.addDailyData(self.accounts_receivable_bill,self.tag + '.accounts_receivable_bill')
        self.addDailyData(self.accounts_payable,self.tag + '.accounts_payable')
        self.addDailyData(self.oth_rcv_tot,self.tag + '.oth_rcv_tot')
        self.addDailyData(self.stm_bs_tot,self.tag + '.stm_bs_tot')
        self.addDailyData(self.const_in_prog_tot,self.tag + '.const_in_prog_tot')
        self.addDailyData(self.oth_payable_tot,self.tag + '.oth_payable_tot')
        self.addDailyData(self.lt_payable_tot,self.tag + '.lt_payable_tot')
        self.addDailyData(self.debt_investment,self.tag + '.debt_investment')
        self.addDailyData(self.other_debt_investment,self.tag + '.other_debt_investment')
        self.addDailyData(self.other_equity_investment,self.tag + '.other_equity_investment')
        self.addDailyData(self.other_illiquidfinancial_assets,self.tag + '.other_illiquidfinancial_assets')
        self.addDailyData(self.other_sustainable_bond,self.tag + '.other_sustainable_bond')
        self.addDailyData(self.receivables_financing,self.tag + '.receivables_financing')
        self.addDailyData(self.right_use_assets,self.tag + '.right_use_assets')
        self.addDailyData(self.lease_liab,self.tag + '.lease_liab')
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
            self.monetary_cap[di, ii]  = float(linespt[7])
            self.tradable_fin_assets[di, ii]  = float(linespt[8])
            self.notes_rcv[di, ii]  = float(linespt[9])
            self.acct_rcv[di, ii]  = float(linespt[10])
            self.oth_rcv[di, ii]  = float(linespt[11])
            self.prepay[di, ii]  = float(linespt[12])
            self.dvd_rcv[di, ii]  = float(linespt[13])
            self.int_rcv[di, ii]  = float(linespt[14])
            self.inventories[di, ii]  = float(linespt[15])
            self.consumptive_bio_assets[di, ii]  = float(linespt[16])
            self.deferred_exp[di, ii]  = float(linespt[17])
            self.non_cur_assets_due_within_1y[di, ii]  = float(linespt[18])
            self.settle_rsrv[di, ii]  = float(linespt[19])
            self.loans_to_oth_banks[di, ii]  = float(linespt[20])
            self.prem_rcv[di, ii]  = float(linespt[21])
            self.rcv_from_reinsurer[di, ii]  = float(linespt[22])
            self.rcv_from_ceded_insur_cont_rsrv[di, ii]  = float(linespt[23])
            self.red_monetary_cap_for_sale[di, ii]  = float(linespt[24])
            self.oth_cur_assets[di, ii]  = float(linespt[25])
            self.tot_cur_assets[di, ii]  = float(linespt[26])
            self.fin_assets_avail_for_sale[di, ii]  = float(linespt[27])
            self.held_to_mty_invest[di, ii]  = float(linespt[28])
            self.long_term_eqy_invest[di, ii]  = float(linespt[29])
            self.invest_real_estate[di, ii]  = float(linespt[30])
            self.time_deposits[di, ii]  = float(linespt[31])
            self.oth_assets[di, ii]  = float(linespt[32])
            self.long_term_rec[di, ii]  = float(linespt[33])
            self.fix_assets[di, ii]  = float(linespt[34])
            self.const_in_prog[di, ii]  = float(linespt[35])
            self.proj_matl[di, ii]  = float(linespt[36])
            self.fix_assets_disp[di, ii]  = float(linespt[37])
            self.productive_bio_assets[di, ii]  = float(linespt[38])
            self.oil_and_natural_gas_assets[di, ii]  = float(linespt[39])
            self.intang_assets[di, ii]  = float(linespt[40])
            self.r_and_d_costs[di, ii]  = float(linespt[41])
            self.goodwill[di, ii]  = float(linespt[42])
            self.long_term_deferred_exp[di, ii]  = float(linespt[43])
            self.deferred_tax_assets[di, ii]  = float(linespt[44])
            self.loans_and_adv_granted[di, ii]  = float(linespt[45])
            self.oth_non_cur_assets[di, ii]  = float(linespt[46])
            self.tot_non_cur_assets[di, ii]  = float(linespt[47])
            self.cash_deposits_central_bank[di, ii]  = float(linespt[48])
            self.asset_dep_oth_banks_fin_inst[di, ii]  = float(linespt[49])
            self.precious_metals[di, ii]  = float(linespt[50])
            self.derivative_fin_assets[di, ii]  = float(linespt[51])
            self.agency_bus_assets[di, ii]  = float(linespt[52])
            self.subr_rec[di, ii]  = float(linespt[53])
            self.rcv_ceded_unearned_prem_rsrv[di, ii]  = float(linespt[54])
            self.rcv_ceded_claim_rsrv[di, ii]  = float(linespt[55])
            self.rcv_ceded_life_insur_rsrv[di, ii]  = float(linespt[56])
            self.rcv_ceded_lt_health_insur_rsrv[di, ii]  = float(linespt[57])
            self.mrgn_paid[di, ii]  = float(linespt[58])
            self.insured_pledge_loan[di, ii]  = float(linespt[59])
            self.cap_mrgn_paid[di, ii]  = float(linespt[60])
            self.independent_acct_assets[di, ii]  = float(linespt[61])
            self.clients_cap_deposit[di, ii]  = float(linespt[62])
            self.clients_rsrv_settle[di, ii]  = float(linespt[63])
            self.incl_seat_fees_exchange[di, ii]  = float(linespt[64])
            self.rcv_invest[di, ii]  = float(linespt[65])
            self.tot_assets[di, ii]  = float(linespt[66])
            self.st_borrow[di, ii]  = float(linespt[67])
            self.borrow_central_bank[di, ii]  = float(linespt[68])
            self.deposit_received_ib_deposits[di, ii]  = float(linespt[69])
            self.loans_oth_banks[di, ii]  = float(linespt[70])
            self.tradable_fin_liab[di, ii]  = float(linespt[71])
            self.notes_payable[di, ii]  = float(linespt[72])
            self.acct_payable[di, ii]  = float(linespt[73])
            self.adv_from_cust[di, ii]  = float(linespt[74])
            self.fund_sales_fin_assets_rp[di, ii]  = float(linespt[75])
            self.handling_charges_comm_payable[di, ii]  = float(linespt[76])
            self.empl_ben_payable[di, ii]  = float(linespt[77])
            self.taxes_surcharges_payable[di, ii]  = float(linespt[78])
            self.int_payable[di, ii]  = float(linespt[79])
            self.dvd_payable[di, ii]  = float(linespt[80])
            self.oth_payable[di, ii]  = float(linespt[81])
            self.acc_exp[di, ii]  = float(linespt[82])
            self.deferred_inc[di, ii]  = float(linespt[83])
            self.st_bonds_payable[di, ii]  = float(linespt[84])
            self.payable_to_reinsurer[di, ii]  = float(linespt[85])
            self.rsrv_insur_cont[di, ii]  = float(linespt[86])
            self.acting_trading_sec[di, ii]  = float(linespt[87])
            self.acting_uw_sec[di, ii]  = float(linespt[88])
            self.non_cur_liab_due_within_1y[di, ii]  = float(linespt[89])
            self.oth_cur_liab[di, ii]  = float(linespt[90])
            self.tot_cur_liab[di, ii]  = float(linespt[91])
            self.lt_borrow[di, ii]  = float(linespt[92])
            self.bonds_payable[di, ii]  = float(linespt[93])
            self.lt_payable[di, ii]  = float(linespt[94])
            self.specific_item_payable[di, ii]  = float(linespt[95])
            self.provisions[di, ii]  = float(linespt[96])
            self.deferred_tax_liab[di, ii]  = float(linespt[97])
            self.deferred_inc_non_cur_liab[di, ii]  = float(linespt[98])
            self.oth_non_cur_liab[di, ii]  = float(linespt[99])
            self.tot_non_cur_liab[di, ii]  = float(linespt[100])
            self.liab_dep_oth_banks_fin_inst[di, ii]  = float(linespt[101])
            self.derivative_fin_liab[di, ii]  = float(linespt[102])
            self.cust_bank_dep[di, ii]  = float(linespt[103])
            self.agency_bus_liab[di, ii]  = float(linespt[104])
            self.oth_liab[di, ii]  = float(linespt[105])
            self.prem_received_adv[di, ii]  = float(linespt[106])
            self.deposit_received[di, ii]  = float(linespt[107])
            self.insured_deposit_invest[di, ii]  = float(linespt[108])
            self.unearned_prem_rsrv[di, ii]  = float(linespt[109])
            self.out_loss_rsrv[di, ii]  = float(linespt[110])
            self.life_insur_rsrv[di, ii]  = float(linespt[111])
            self.lt_health_insur_v[di, ii]  = float(linespt[112])
            self.independent_acct_liab[di, ii]  = float(linespt[113])
            self.incl_pledge_loan[di, ii]  = float(linespt[114])
            self.claims_payable[di, ii]  = float(linespt[115])
            self.dvd_payable_insured[di, ii]  = float(linespt[116])
            self.tot_liab[di, ii]  = float(linespt[117])
            self.cap_stk[di, ii]  = float(linespt[118])
            self.cap_rsrv[di, ii]  = float(linespt[119])
            self.special_rsrv[di, ii]  = float(linespt[120])
            self.surplus_rsrv[di, ii]  = float(linespt[121])
            self.undistributed_profit[di, ii]  = float(linespt[122])
            self.less_tsy_stk[di, ii]  = float(linespt[123])
            self.prov_nom_risks[di, ii]  = float(linespt[124])
            self.cnvd_diff_foreign_curr_stat[di, ii]  = float(linespt[125])
            self.unconfirmed_invest_loss[di, ii]  = float(linespt[126])
            self.minority_int[di, ii]  = float(linespt[127])
            self.tot_shrhldr_eqy_excl_min_int[di, ii]  = float(linespt[128])
            self.tot_shrhldr_eqy_incl_min_int[di, ii]  = float(linespt[129])
            self.tot_liab_shrhldr_eqy[di, ii]  = float(linespt[130])
            self.comp_type_code[di, ii]  = float(linespt[131])
            self.actual_ann_dt[di, ii]  = float(linespt[132])
            self.spe_cur_assets_diff[di, ii]  = float(linespt[133])
            self.tot_cur_assets_diff[di, ii]  = float(linespt[134])
            self.spe_non_cur_assets_diff[di, ii]  = float(linespt[135])
            self.tot_non_cur_assets_diff[di, ii]  = float(linespt[136])
            self.spe_bal_assets_diff[di, ii]  = float(linespt[137])
            self.tot_bal_assets_diff[di, ii]  = float(linespt[138])
            self.spe_cur_liab_diff[di, ii]  = float(linespt[139])
            self.tot_cur_liab_diff[di, ii]  = float(linespt[140])
            self.spe_non_cur_liab_diff[di, ii]  = float(linespt[141])
            self.tot_non_cur_liab_diff[di, ii]  = float(linespt[142])
            self.spe_bal_liab_diff[di, ii]  = float(linespt[143])
            self.tot_bal_liab_diff[di, ii]  = float(linespt[144])
            self.spe_bal_shrhldr_eqy_diff[di, ii]  = float(linespt[145])
            self.tot_bal_shrhldr_eqy_diff[di, ii]  = float(linespt[146])
            self.spe_bal_liab_eqy_diff[di, ii]  = float(linespt[147])
            self.tot_bal_liab_eqy_diff[di, ii]  = float(linespt[148])
            self.lt_payroll_payable[di, ii]  = float(linespt[149])
            self.other_comp_income[di, ii]  = float(linespt[150])
            self.other_equity_tools[di, ii]  = float(linespt[151])
            self.other_equity_tools_p_shr[di, ii]  = float(linespt[152])
            self.lending_funds[di, ii]  = float(linespt[153])
            self.accounts_receivable[di, ii]  = float(linespt[154])
            self.st_financing_payable[di, ii]  = float(linespt[155])
            self.payables[di, ii]  = float(linespt[156])
            self.tot_shr[di, ii]  = float(linespt[158])
            self.hfs_assets[di, ii]  = float(linespt[159])
            self.hfs_sales[di, ii]  = float(linespt[160])
            self.fin_assets_cost_sharing[di, ii]  = float(linespt[161])
            self.fin_assets_fair_value[di, ii]  = float(linespt[162])
            self.contractual_assets[di, ii]  = float(linespt[163])
            self.contract_liabilities[di, ii]  = float(linespt[164])
            self.accounts_receivable_bill[di, ii]  = float(linespt[165])
            self.accounts_payable[di, ii]  = float(linespt[166])
            self.oth_rcv_tot[di, ii]  = float(linespt[167])
            self.stm_bs_tot[di, ii]  = float(linespt[168])
            self.const_in_prog_tot[di, ii]  = float(linespt[169])
            self.oth_payable_tot[di, ii]  = float(linespt[170])
            self.lt_payable_tot[di, ii]  = float(linespt[171])
            self.debt_investment[di, ii]  = float(linespt[172])
            self.other_debt_investment[di, ii]  = float(linespt[173])
            self.other_equity_investment[di, ii]  = float(linespt[174])
            self.other_illiquidfinancial_assets[di, ii]  = float(linespt[175])
            self.other_sustainable_bond[di, ii]  = float(linespt[176])
            self.receivables_financing[di, ii]  = float(linespt[177])
            self.right_use_assets[di, ii]  = float(linespt[178])
            self.lease_liab[di, ii]  = float(linespt[179])
            updated += 1
        infile.close()
        print('[ %s ] Updated %d stocks on day %d' %  (self.tag, updated, uv.Dates[di]))
        return

    def doBackfill(self, di):

        self.report_period[di] = self.report_period[di - 1]
        self.statement_type[di] = self.statement_type[di - 1]
        self.monetary_cap[di] = self.monetary_cap[di - 1]
        self.tradable_fin_assets[di] = self.tradable_fin_assets[di - 1]
        self.notes_rcv[di] = self.notes_rcv[di - 1]
        self.acct_rcv[di] = self.acct_rcv[di - 1]
        self.oth_rcv[di] = self.oth_rcv[di - 1]
        self.prepay[di] = self.prepay[di - 1]
        self.dvd_rcv[di] = self.dvd_rcv[di - 1]
        self.int_rcv[di] = self.int_rcv[di - 1]
        self.inventories[di] = self.inventories[di - 1]
        self.consumptive_bio_assets[di] = self.consumptive_bio_assets[di - 1]
        self.deferred_exp[di] = self.deferred_exp[di - 1]
        self.non_cur_assets_due_within_1y[di] = self.non_cur_assets_due_within_1y[di - 1]
        self.settle_rsrv[di] = self.settle_rsrv[di - 1]
        self.loans_to_oth_banks[di] = self.loans_to_oth_banks[di - 1]
        self.prem_rcv[di] = self.prem_rcv[di - 1]
        self.rcv_from_reinsurer[di] = self.rcv_from_reinsurer[di - 1]
        self.rcv_from_ceded_insur_cont_rsrv[di] = self.rcv_from_ceded_insur_cont_rsrv[di - 1]
        self.red_monetary_cap_for_sale[di] = self.red_monetary_cap_for_sale[di - 1]
        self.oth_cur_assets[di] = self.oth_cur_assets[di - 1]
        self.tot_cur_assets[di] = self.tot_cur_assets[di - 1]
        self.fin_assets_avail_for_sale[di] = self.fin_assets_avail_for_sale[di - 1]
        self.held_to_mty_invest[di] = self.held_to_mty_invest[di - 1]
        self.long_term_eqy_invest[di] = self.long_term_eqy_invest[di - 1]
        self.invest_real_estate[di] = self.invest_real_estate[di - 1]
        self.time_deposits[di] = self.time_deposits[di - 1]
        self.oth_assets[di] = self.oth_assets[di - 1]
        self.long_term_rec[di] = self.long_term_rec[di - 1]
        self.fix_assets[di] = self.fix_assets[di - 1]
        self.const_in_prog[di] = self.const_in_prog[di - 1]
        self.proj_matl[di] = self.proj_matl[di - 1]
        self.fix_assets_disp[di] = self.fix_assets_disp[di - 1]
        self.productive_bio_assets[di] = self.productive_bio_assets[di - 1]
        self.oil_and_natural_gas_assets[di] = self.oil_and_natural_gas_assets[di - 1]
        self.intang_assets[di] = self.intang_assets[di - 1]
        self.r_and_d_costs[di] = self.r_and_d_costs[di - 1]
        self.goodwill[di] = self.goodwill[di - 1]
        self.long_term_deferred_exp[di] = self.long_term_deferred_exp[di - 1]
        self.deferred_tax_assets[di] = self.deferred_tax_assets[di - 1]
        self.loans_and_adv_granted[di] = self.loans_and_adv_granted[di - 1]
        self.oth_non_cur_assets[di] = self.oth_non_cur_assets[di - 1]
        self.tot_non_cur_assets[di] = self.tot_non_cur_assets[di - 1]
        self.cash_deposits_central_bank[di] = self.cash_deposits_central_bank[di - 1]
        self.asset_dep_oth_banks_fin_inst[di] = self.asset_dep_oth_banks_fin_inst[di - 1]
        self.precious_metals[di] = self.precious_metals[di - 1]
        self.derivative_fin_assets[di] = self.derivative_fin_assets[di - 1]
        self.agency_bus_assets[di] = self.agency_bus_assets[di - 1]
        self.subr_rec[di] = self.subr_rec[di - 1]
        self.rcv_ceded_unearned_prem_rsrv[di] = self.rcv_ceded_unearned_prem_rsrv[di - 1]
        self.rcv_ceded_claim_rsrv[di] = self.rcv_ceded_claim_rsrv[di - 1]
        self.rcv_ceded_life_insur_rsrv[di] = self.rcv_ceded_life_insur_rsrv[di - 1]
        self.rcv_ceded_lt_health_insur_rsrv[di] = self.rcv_ceded_lt_health_insur_rsrv[di - 1]
        self.mrgn_paid[di] = self.mrgn_paid[di - 1]
        self.insured_pledge_loan[di] = self.insured_pledge_loan[di - 1]
        self.cap_mrgn_paid[di] = self.cap_mrgn_paid[di - 1]
        self.independent_acct_assets[di] = self.independent_acct_assets[di - 1]
        self.clients_cap_deposit[di] = self.clients_cap_deposit[di - 1]
        self.clients_rsrv_settle[di] = self.clients_rsrv_settle[di - 1]
        self.incl_seat_fees_exchange[di] = self.incl_seat_fees_exchange[di - 1]
        self.rcv_invest[di] = self.rcv_invest[di - 1]
        self.tot_assets[di] = self.tot_assets[di - 1]
        self.st_borrow[di] = self.st_borrow[di - 1]
        self.borrow_central_bank[di] = self.borrow_central_bank[di - 1]
        self.deposit_received_ib_deposits[di] = self.deposit_received_ib_deposits[di - 1]
        self.loans_oth_banks[di] = self.loans_oth_banks[di - 1]
        self.tradable_fin_liab[di] = self.tradable_fin_liab[di - 1]
        self.notes_payable[di] = self.notes_payable[di - 1]
        self.acct_payable[di] = self.acct_payable[di - 1]
        self.adv_from_cust[di] = self.adv_from_cust[di - 1]
        self.fund_sales_fin_assets_rp[di] = self.fund_sales_fin_assets_rp[di - 1]
        self.handling_charges_comm_payable[di] = self.handling_charges_comm_payable[di - 1]
        self.empl_ben_payable[di] = self.empl_ben_payable[di - 1]
        self.taxes_surcharges_payable[di] = self.taxes_surcharges_payable[di - 1]
        self.int_payable[di] = self.int_payable[di - 1]
        self.dvd_payable[di] = self.dvd_payable[di - 1]
        self.oth_payable[di] = self.oth_payable[di - 1]
        self.acc_exp[di] = self.acc_exp[di - 1]
        self.deferred_inc[di] = self.deferred_inc[di - 1]
        self.st_bonds_payable[di] = self.st_bonds_payable[di - 1]
        self.payable_to_reinsurer[di] = self.payable_to_reinsurer[di - 1]
        self.rsrv_insur_cont[di] = self.rsrv_insur_cont[di - 1]
        self.acting_trading_sec[di] = self.acting_trading_sec[di - 1]
        self.acting_uw_sec[di] = self.acting_uw_sec[di - 1]
        self.non_cur_liab_due_within_1y[di] = self.non_cur_liab_due_within_1y[di - 1]
        self.oth_cur_liab[di] = self.oth_cur_liab[di - 1]
        self.tot_cur_liab[di] = self.tot_cur_liab[di - 1]
        self.lt_borrow[di] = self.lt_borrow[di - 1]
        self.bonds_payable[di] = self.bonds_payable[di - 1]
        self.lt_payable[di] = self.lt_payable[di - 1]
        self.specific_item_payable[di] = self.specific_item_payable[di - 1]
        self.provisions[di] = self.provisions[di - 1]
        self.deferred_tax_liab[di] = self.deferred_tax_liab[di - 1]
        self.deferred_inc_non_cur_liab[di] = self.deferred_inc_non_cur_liab[di - 1]
        self.oth_non_cur_liab[di] = self.oth_non_cur_liab[di - 1]
        self.tot_non_cur_liab[di] = self.tot_non_cur_liab[di - 1]
        self.liab_dep_oth_banks_fin_inst[di] = self.liab_dep_oth_banks_fin_inst[di - 1]
        self.derivative_fin_liab[di] = self.derivative_fin_liab[di - 1]
        self.cust_bank_dep[di] = self.cust_bank_dep[di - 1]
        self.agency_bus_liab[di] = self.agency_bus_liab[di - 1]
        self.oth_liab[di] = self.oth_liab[di - 1]
        self.prem_received_adv[di] = self.prem_received_adv[di - 1]
        self.deposit_received[di] = self.deposit_received[di - 1]
        self.insured_deposit_invest[di] = self.insured_deposit_invest[di - 1]
        self.unearned_prem_rsrv[di] = self.unearned_prem_rsrv[di - 1]
        self.out_loss_rsrv[di] = self.out_loss_rsrv[di - 1]
        self.life_insur_rsrv[di] = self.life_insur_rsrv[di - 1]
        self.lt_health_insur_v[di] = self.lt_health_insur_v[di - 1]
        self.independent_acct_liab[di] = self.independent_acct_liab[di - 1]
        self.incl_pledge_loan[di] = self.incl_pledge_loan[di - 1]
        self.claims_payable[di] = self.claims_payable[di - 1]
        self.dvd_payable_insured[di] = self.dvd_payable_insured[di - 1]
        self.tot_liab[di] = self.tot_liab[di - 1]
        self.cap_stk[di] = self.cap_stk[di - 1]
        self.cap_rsrv[di] = self.cap_rsrv[di - 1]
        self.special_rsrv[di] = self.special_rsrv[di - 1]
        self.surplus_rsrv[di] = self.surplus_rsrv[di - 1]
        self.undistributed_profit[di] = self.undistributed_profit[di - 1]
        self.less_tsy_stk[di] = self.less_tsy_stk[di - 1]
        self.prov_nom_risks[di] = self.prov_nom_risks[di - 1]
        self.cnvd_diff_foreign_curr_stat[di] = self.cnvd_diff_foreign_curr_stat[di - 1]
        self.unconfirmed_invest_loss[di] = self.unconfirmed_invest_loss[di - 1]
        self.minority_int[di] = self.minority_int[di - 1]
        self.tot_shrhldr_eqy_excl_min_int[di] = self.tot_shrhldr_eqy_excl_min_int[di - 1]
        self.tot_shrhldr_eqy_incl_min_int[di] = self.tot_shrhldr_eqy_incl_min_int[di - 1]
        self.tot_liab_shrhldr_eqy[di] = self.tot_liab_shrhldr_eqy[di - 1]
        self.comp_type_code[di] = self.comp_type_code[di - 1]
        self.actual_ann_dt[di] = self.actual_ann_dt[di - 1]
        self.spe_cur_assets_diff[di] = self.spe_cur_assets_diff[di - 1]
        self.tot_cur_assets_diff[di] = self.tot_cur_assets_diff[di - 1]
        self.spe_non_cur_assets_diff[di] = self.spe_non_cur_assets_diff[di - 1]
        self.tot_non_cur_assets_diff[di] = self.tot_non_cur_assets_diff[di - 1]
        self.spe_bal_assets_diff[di] = self.spe_bal_assets_diff[di - 1]
        self.tot_bal_assets_diff[di] = self.tot_bal_assets_diff[di - 1]
        self.spe_cur_liab_diff[di] = self.spe_cur_liab_diff[di - 1]
        self.tot_cur_liab_diff[di] = self.tot_cur_liab_diff[di - 1]
        self.spe_non_cur_liab_diff[di] = self.spe_non_cur_liab_diff[di - 1]
        self.tot_non_cur_liab_diff[di] = self.tot_non_cur_liab_diff[di - 1]
        self.spe_bal_liab_diff[di] = self.spe_bal_liab_diff[di - 1]
        self.tot_bal_liab_diff[di] = self.tot_bal_liab_diff[di - 1]
        self.spe_bal_shrhldr_eqy_diff[di] = self.spe_bal_shrhldr_eqy_diff[di - 1]
        self.tot_bal_shrhldr_eqy_diff[di] = self.tot_bal_shrhldr_eqy_diff[di - 1]
        self.spe_bal_liab_eqy_diff[di] = self.spe_bal_liab_eqy_diff[di - 1]
        self.tot_bal_liab_eqy_diff[di] = self.tot_bal_liab_eqy_diff[di - 1]
        self.lt_payroll_payable[di] = self.lt_payroll_payable[di - 1]
        self.other_comp_income[di] = self.other_comp_income[di - 1]
        self.other_equity_tools[di] = self.other_equity_tools[di - 1]
        self.other_equity_tools_p_shr[di] = self.other_equity_tools_p_shr[di - 1]
        self.lending_funds[di] = self.lending_funds[di - 1]
        self.accounts_receivable[di] = self.accounts_receivable[di - 1]
        self.st_financing_payable[di] = self.st_financing_payable[di - 1]
        self.payables[di] = self.payables[di - 1]
        self.tot_shr[di] = self.tot_shr[di - 1]
        self.hfs_assets[di] = self.hfs_assets[di - 1]
        self.hfs_sales[di] = self.hfs_sales[di - 1]
        self.fin_assets_cost_sharing[di] = self.fin_assets_cost_sharing[di - 1]
        self.fin_assets_fair_value[di] = self.fin_assets_fair_value[di - 1]
        self.contractual_assets[di] = self.contractual_assets[di - 1]
        self.contract_liabilities[di] = self.contract_liabilities[di - 1]
        self.accounts_receivable_bill[di] = self.accounts_receivable_bill[di - 1]
        self.accounts_payable[di] = self.accounts_payable[di - 1]
        self.oth_rcv_tot[di] = self.oth_rcv_tot[di - 1]
        self.stm_bs_tot[di] = self.stm_bs_tot[di - 1]
        self.const_in_prog_tot[di] = self.const_in_prog_tot[di - 1]
        self.oth_payable_tot[di] = self.oth_payable_tot[di - 1]
        self.lt_payable_tot[di] = self.lt_payable_tot[di - 1]
        self.debt_investment[di] = self.debt_investment[di - 1]
        self.other_debt_investment[di] = self.other_debt_investment[di - 1]
        self.other_equity_investment[di] = self.other_equity_investment[di - 1]
        self.other_illiquidfinancial_assets[di] = self.other_illiquidfinancial_assets[di - 1]
        self.other_sustainable_bond[di] = self.other_sustainable_bond[di - 1]
        self.receivables_financing[di] = self.receivables_financing[di - 1]
        self.right_use_assets[di] = self.right_use_assets[di - 1]
        self.lease_liab[di] = self.lease_liab[di - 1]