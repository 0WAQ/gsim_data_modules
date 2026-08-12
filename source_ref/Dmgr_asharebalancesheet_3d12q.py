from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import Universe as uv
from gsim.data import DataRegistry as dr
import pandas as pd
import glob
import logging


class DmgrAShareBalancesheet3d12q(DataManagerMapped):
    def __init__(self):
        DataManagerMapped.__init__(self)
        self.dataPath = ''
        self.nquarters = 12

        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s - %(levelname)s - %(message)s',
            filename='balancesheet.log'
        )

        ########################################################################################################################################
        # 字符串类型字段(varchar/timestamp)
        self.report_period = NIO_CUBE()
        self.actual_ann_dt = NIO_CUBE()

        # 数值类型字段(numeric)
        self.statement_type = NIO_CUBE()
        self.monetary_cap = NIO_CUBE()
        self.tradable_fin_assets = NIO_CUBE()
        self.notes_rcv = NIO_CUBE()
        self.acct_rcv = NIO_CUBE()
        self.oth_rcv = NIO_CUBE()
        self.prepay = NIO_CUBE()
        self.dvd_rcv = NIO_CUBE()
        self.int_rcv = NIO_CUBE()
        self.inventories = NIO_CUBE()
        self.consumptive_bio_assets = NIO_CUBE()
        self.deferred_exp = NIO_CUBE()
        self.non_cur_assets_due_within_1y = NIO_CUBE()
        self.settle_rsrv = NIO_CUBE()
        self.loans_to_oth_banks = NIO_CUBE()
        self.prem_rcv = NIO_CUBE()
        self.rcv_from_reinsurer = NIO_CUBE()
        self.rcv_from_ceded_insur_cont_rsrv = NIO_CUBE()
        self.red_monetary_cap_for_sale = NIO_CUBE()
        self.oth_cur_assets = NIO_CUBE()
        self.tot_cur_assets = NIO_CUBE()
        self.fin_assets_avail_for_sale = NIO_CUBE()
        self.held_to_mty_invest = NIO_CUBE()
        self.long_term_eqy_invest = NIO_CUBE()
        self.invest_real_estate = NIO_CUBE()
        self.time_deposits = NIO_CUBE()
        self.oth_assets = NIO_CUBE()
        self.long_term_rec = NIO_CUBE()
        self.fix_assets = NIO_CUBE()
        self.const_in_prog = NIO_CUBE()
        self.proj_matl = NIO_CUBE()
        self.fix_assets_disp = NIO_CUBE()
        self.productive_bio_assets = NIO_CUBE()
        self.oil_and_natural_gas_assets = NIO_CUBE()
        self.intang_assets = NIO_CUBE()
        self.r_and_d_costs = NIO_CUBE()
        self.goodwill = NIO_CUBE()
        self.long_term_deferred_exp = NIO_CUBE()
        self.deferred_tax_assets = NIO_CUBE()
        self.loans_and_adv_granted = NIO_CUBE()
        self.oth_non_cur_assets = NIO_CUBE()
        self.tot_non_cur_assets = NIO_CUBE()
        self.cash_deposits_central_bank = NIO_CUBE()
        self.asset_dep_oth_banks_fin_inst = NIO_CUBE()
        self.precious_metals = NIO_CUBE()
        self.derivative_fin_assets = NIO_CUBE()
        self.agency_bus_assets = NIO_CUBE()
        self.subr_rec = NIO_CUBE()
        self.rcv_ceded_unearned_prem_rsrv = NIO_CUBE()
        self.rcv_ceded_claim_rsrv = NIO_CUBE()
        self.rcv_ceded_life_insur_rsrv = NIO_CUBE()
        self.rcv_ceded_lt_health_insur_rsrv = NIO_CUBE()
        self.mrgn_paid = NIO_CUBE()
        self.insured_pledge_loan = NIO_CUBE()
        self.cap_mrgn_paid = NIO_CUBE()
        self.independent_acct_assets = NIO_CUBE()
        self.clients_cap_deposit = NIO_CUBE()
        self.clients_rsrv_settle = NIO_CUBE()
        self.incl_seat_fees_exchange = NIO_CUBE()
        self.rcv_invest = NIO_CUBE()
        self.tot_assets = NIO_CUBE()
        self.st_borrow = NIO_CUBE()
        self.borrow_central_bank = NIO_CUBE()
        self.deposit_received_ib_deposits = NIO_CUBE()
        self.loans_oth_banks = NIO_CUBE()
        self.tradable_fin_liab = NIO_CUBE()
        self.notes_payable = NIO_CUBE()
        self.acct_payable = NIO_CUBE()
        self.adv_from_cust = NIO_CUBE()
        self.fund_sales_fin_assets_rp = NIO_CUBE()
        self.handling_charges_comm_payable = NIO_CUBE()
        self.empl_ben_payable = NIO_CUBE()
        self.taxes_surcharges_payable = NIO_CUBE()
        self.int_payable = NIO_CUBE()
        self.dvd_payable = NIO_CUBE()
        self.oth_payable = NIO_CUBE()
        self.acc_exp = NIO_CUBE()
        self.deferred_inc = NIO_CUBE()
        self.st_bonds_payable = NIO_CUBE()
        self.payable_to_reinsurer = NIO_CUBE()
        self.rsrv_insur_cont = NIO_CUBE()
        self.acting_trading_sec = NIO_CUBE()
        self.acting_uw_sec = NIO_CUBE()
        self.non_cur_liab_due_within_1y = NIO_CUBE()
        self.oth_cur_liab = NIO_CUBE()
        self.tot_cur_liab = NIO_CUBE()
        self.lt_borrow = NIO_CUBE()
        self.bonds_payable = NIO_CUBE()
        self.lt_payable = NIO_CUBE()
        self.specific_item_payable = NIO_CUBE()
        self.provisions = NIO_CUBE()
        self.deferred_tax_liab = NIO_CUBE()
        self.deferred_inc_non_cur_liab = NIO_CUBE()
        self.oth_non_cur_liab = NIO_CUBE()
        self.tot_non_cur_liab = NIO_CUBE()
        self.liab_dep_oth_banks_fin_inst = NIO_CUBE()
        self.derivative_fin_liab = NIO_CUBE()
        self.cust_bank_dep = NIO_CUBE()
        self.agency_bus_liab = NIO_CUBE()
        self.oth_liab = NIO_CUBE()
        self.prem_received_adv = NIO_CUBE()
        self.deposit_received = NIO_CUBE()
        self.insured_deposit_invest = NIO_CUBE()
        self.unearned_prem_rsrv = NIO_CUBE()
        self.out_loss_rsrv = NIO_CUBE()
        self.life_insur_rsrv = NIO_CUBE()
        self.lt_health_insur_v = NIO_CUBE()
        self.independent_acct_liab = NIO_CUBE()
        self.incl_pledge_loan = NIO_CUBE()
        self.claims_payable = NIO_CUBE()
        self.dvd_payable_insured = NIO_CUBE()
        self.tot_liab = NIO_CUBE()
        self.cap_stk = NIO_CUBE()
        self.cap_rsrv = NIO_CUBE()
        self.special_rsrv = NIO_CUBE()
        self.surplus_rsrv = NIO_CUBE()
        self.undistributed_profit = NIO_CUBE()
        self.less_tsy_stk = NIO_CUBE()
        self.prov_nom_risks = NIO_CUBE()
        self.cnvd_diff_foreign_curr_stat = NIO_CUBE()
        self.unconfirmed_invest_loss = NIO_CUBE()
        self.minority_int = NIO_CUBE()
        self.tot_shrhldr_eqy_excl_min_int = NIO_CUBE()
        self.tot_shrhldr_eqy_incl_min_int = NIO_CUBE()
        self.tot_liab_shrhldr_eqy = NIO_CUBE()
        self.spe_cur_assets_diff = NIO_CUBE()
        self.tot_cur_assets_diff = NIO_CUBE()
        self.spe_non_cur_assets_diff = NIO_CUBE()
        self.tot_non_cur_assets_diff = NIO_CUBE()
        self.spe_bal_assets_diff = NIO_CUBE()
        self.tot_bal_assets_diff = NIO_CUBE()
        self.spe_cur_liab_diff = NIO_CUBE()
        self.tot_cur_liab_diff = NIO_CUBE()
        self.spe_non_cur_liab_diff = NIO_CUBE()
        self.tot_non_cur_liab_diff = NIO_CUBE()
        self.spe_bal_liab_diff = NIO_CUBE()
        self.tot_bal_liab_diff = NIO_CUBE()
        self.spe_bal_shrhldr_eqy_diff = NIO_CUBE()
        self.tot_bal_shrhldr_eqy_diff = NIO_CUBE()
        self.spe_bal_liab_eqy_diff = NIO_CUBE()
        self.tot_bal_liab_eqy_diff = NIO_CUBE()
        self.lt_payroll_payable = NIO_CUBE()
        self.other_comp_income = NIO_CUBE()
        self.other_equity_tools = NIO_CUBE()
        self.other_equity_tools_p_shr = NIO_CUBE()
        self.lending_funds = NIO_CUBE()
        self.accounts_receivable = NIO_CUBE()
        self.st_financing_payable = NIO_CUBE()
        self.payables = NIO_CUBE()
        self.tot_shr = NIO_CUBE()
        self.hfs_assets = NIO_CUBE()
        self.hfs_sales = NIO_CUBE()
        self.fin_assets_cost_sharing = NIO_CUBE()
        self.fin_assets_fair_value = NIO_CUBE()
        self.contractual_assets = NIO_CUBE()
        self.contract_liabilities = NIO_CUBE()
        self.accounts_receivable_bill = NIO_CUBE()
        self.accounts_payable = NIO_CUBE()
        self.oth_rcv_tot = NIO_CUBE()
        self.stm_bs_tot = NIO_CUBE()
        self.const_in_prog_tot = NIO_CUBE()
        self.oth_payable_tot = NIO_CUBE()
        self.lt_payable_tot = NIO_CUBE()
        self.debt_investment = NIO_CUBE()
        self.other_debt_investment = NIO_CUBE()
        self.other_equity_investment = NIO_CUBE()
        self.other_illiquidfinancial_assets = NIO_CUBE()
        self.other_sustainable_bond = NIO_CUBE()
        self.receivables_financing = NIO_CUBE()
        self.right_use_assets = NIO_CUBE()
        self.lease_liab = NIO_CUBE()
        self.iflisted_data = NIO_CUBE()
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
        self.addData(self.monetary_cap, self.tag + '.monetary_cap', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.tradable_fin_assets, self.tag + '.tradable_fin_assets', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.notes_rcv, self.tag + '.notes_rcv', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.acct_rcv, self.tag + '.acct_rcv', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.oth_rcv, self.tag + '.oth_rcv', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.prepay, self.tag + '.prepay', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.dvd_rcv, self.tag + '.dvd_rcv', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.int_rcv, self.tag + '.int_rcv', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.inventories, self.tag + '.inventories', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.consumptive_bio_assets, self.tag + '.consumptive_bio_assets', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.deferred_exp, self.tag + '.deferred_exp', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.non_cur_assets_due_within_1y, self.tag + '.non_cur_assets_due_within_1y', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.settle_rsrv, self.tag + '.settle_rsrv', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.loans_to_oth_banks, self.tag + '.loans_to_oth_banks', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.prem_rcv, self.tag + '.prem_rcv', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.rcv_from_reinsurer, self.tag + '.rcv_from_reinsurer', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.rcv_from_ceded_insur_cont_rsrv, self.tag + '.rcv_from_ceded_insur_cont_rsrv', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.red_monetary_cap_for_sale, self.tag + '.red_monetary_cap_for_sale', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.oth_cur_assets, self.tag + '.oth_cur_assets', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.tot_cur_assets, self.tag + '.tot_cur_assets', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.fin_assets_avail_for_sale, self.tag + '.fin_assets_avail_for_sale', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.held_to_mty_invest, self.tag + '.held_to_mty_invest', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.long_term_eqy_invest, self.tag + '.long_term_eqy_invest', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.invest_real_estate, self.tag + '.invest_real_estate', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.time_deposits, self.tag + '.time_deposits', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.oth_assets, self.tag + '.oth_assets', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.long_term_rec, self.tag + '.long_term_rec', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.fix_assets, self.tag + '.fix_assets', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.const_in_prog, self.tag + '.const_in_prog', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.proj_matl, self.tag + '.proj_matl', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.fix_assets_disp, self.tag + '.fix_assets_disp', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.productive_bio_assets, self.tag + '.productive_bio_assets', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.oil_and_natural_gas_assets, self.tag + '.oil_and_natural_gas_assets', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.intang_assets, self.tag + '.intang_assets', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.r_and_d_costs, self.tag + '.r_and_d_costs', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.goodwill, self.tag + '.goodwill', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.long_term_deferred_exp, self.tag + '.long_term_deferred_exp', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.deferred_tax_assets, self.tag + '.deferred_tax_assets', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.loans_and_adv_granted, self.tag + '.loans_and_adv_granted', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.oth_non_cur_assets, self.tag + '.oth_non_cur_assets', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.tot_non_cur_assets, self.tag + '.tot_non_cur_assets', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.cash_deposits_central_bank, self.tag + '.cash_deposits_central_bank', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.asset_dep_oth_banks_fin_inst, self.tag + '.asset_dep_oth_banks_fin_inst', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.precious_metals, self.tag + '.precious_metals', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.derivative_fin_assets, self.tag + '.derivative_fin_assets', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.agency_bus_assets, self.tag + '.agency_bus_assets', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.subr_rec, self.tag + '.subr_rec', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.rcv_ceded_unearned_prem_rsrv, self.tag + '.rcv_ceded_unearned_prem_rsrv', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.rcv_ceded_claim_rsrv, self.tag + '.rcv_ceded_claim_rsrv', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.rcv_ceded_life_insur_rsrv, self.tag + '.rcv_ceded_life_insur_rsrv', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.rcv_ceded_lt_health_insur_rsrv, self.tag + '.rcv_ceded_lt_health_insur_rsrv', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.mrgn_paid, self.tag + '.mrgn_paid', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.insured_pledge_loan, self.tag + '.insured_pledge_loan', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.cap_mrgn_paid, self.tag + '.cap_mrgn_paid', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.independent_acct_assets, self.tag + '.independent_acct_assets', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.clients_cap_deposit, self.tag + '.clients_cap_deposit', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.clients_rsrv_settle, self.tag + '.clients_rsrv_settle', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.incl_seat_fees_exchange, self.tag + '.incl_seat_fees_exchange', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.rcv_invest, self.tag + '.rcv_invest', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.tot_assets, self.tag + '.tot_assets', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.st_borrow, self.tag + '.st_borrow', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.borrow_central_bank, self.tag + '.borrow_central_bank', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.deposit_received_ib_deposits, self.tag + '.deposit_received_ib_deposits', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.loans_oth_banks, self.tag + '.loans_oth_banks', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.tradable_fin_liab, self.tag + '.tradable_fin_liab', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.notes_payable, self.tag + '.notes_payable', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.acct_payable, self.tag + '.acct_payable', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.adv_from_cust, self.tag + '.adv_from_cust', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.fund_sales_fin_assets_rp, self.tag + '.fund_sales_fin_assets_rp', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.handling_charges_comm_payable, self.tag + '.handling_charges_comm_payable', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.empl_ben_payable, self.tag + '.empl_ben_payable', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.taxes_surcharges_payable, self.tag + '.taxes_surcharges_payable', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.int_payable, self.tag + '.int_payable', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.dvd_payable, self.tag + '.dvd_payable', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.oth_payable, self.tag + '.oth_payable', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.acc_exp, self.tag + '.acc_exp', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.deferred_inc, self.tag + '.deferred_inc', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.st_bonds_payable, self.tag + '.st_bonds_payable', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.payable_to_reinsurer, self.tag + '.payable_to_reinsurer', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.rsrv_insur_cont, self.tag + '.rsrv_insur_cont', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.acting_trading_sec, self.tag + '.acting_trading_sec', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.acting_uw_sec, self.tag + '.acting_uw_sec', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.non_cur_liab_due_within_1y, self.tag + '.non_cur_liab_due_within_1y', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.oth_cur_liab, self.tag + '.oth_cur_liab', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.tot_cur_liab, self.tag + '.tot_cur_liab', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.lt_borrow, self.tag + '.lt_borrow', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.bonds_payable, self.tag + '.bonds_payable', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.lt_payable, self.tag + '.lt_payable', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.specific_item_payable, self.tag + '.specific_item_payable', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.provisions, self.tag + '.provisions', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.deferred_tax_liab, self.tag + '.deferred_tax_liab', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.deferred_inc_non_cur_liab, self.tag + '.deferred_inc_non_cur_liab', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.oth_non_cur_liab, self.tag + '.oth_non_cur_liab', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.tot_non_cur_liab, self.tag + '.tot_non_cur_liab', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.liab_dep_oth_banks_fin_inst, self.tag + '.liab_dep_oth_banks_fin_inst', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.derivative_fin_liab, self.tag + '.derivative_fin_liab', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.cust_bank_dep, self.tag + '.cust_bank_dep', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.agency_bus_liab, self.tag + '.agency_bus_liab', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.oth_liab, self.tag + '.oth_liab', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.prem_received_adv, self.tag + '.prem_received_adv', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.deposit_received, self.tag + '.deposit_received', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.insured_deposit_invest, self.tag + '.insured_deposit_invest', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.unearned_prem_rsrv, self.tag + '.unearned_prem_rsrv', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.out_loss_rsrv, self.tag + '.out_loss_rsrv', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.life_insur_rsrv, self.tag + '.life_insur_rsrv', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.lt_health_insur_v, self.tag + '.lt_health_insur_v', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.independent_acct_liab, self.tag + '.independent_acct_liab', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.incl_pledge_loan, self.tag + '.incl_pledge_loan', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.claims_payable, self.tag + '.claims_payable', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.dvd_payable_insured, self.tag + '.dvd_payable_insured', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.tot_liab, self.tag + '.tot_liab', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.cap_stk, self.tag + '.cap_stk', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.cap_rsrv, self.tag + '.cap_rsrv', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.special_rsrv, self.tag + '.special_rsrv', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.surplus_rsrv, self.tag + '.surplus_rsrv', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.undistributed_profit, self.tag + '.undistributed_profit', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.less_tsy_stk, self.tag + '.less_tsy_stk', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.prov_nom_risks, self.tag + '.prov_nom_risks', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.cnvd_diff_foreign_curr_stat, self.tag + '.cnvd_diff_foreign_curr_stat', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.unconfirmed_invest_loss, self.tag + '.unconfirmed_invest_loss', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.minority_int, self.tag + '.minority_int', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.tot_shrhldr_eqy_excl_min_int, self.tag + '.tot_shrhldr_eqy_excl_min_int', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.tot_shrhldr_eqy_incl_min_int, self.tag + '.tot_shrhldr_eqy_incl_min_int', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.tot_liab_shrhldr_eqy, self.tag + '.tot_liab_shrhldr_eqy', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.spe_cur_assets_diff, self.tag + '.spe_cur_assets_diff', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.tot_cur_assets_diff, self.tag + '.tot_cur_assets_diff', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.spe_non_cur_assets_diff, self.tag + '.spe_non_cur_assets_diff', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.tot_non_cur_assets_diff, self.tag + '.tot_non_cur_assets_diff', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.spe_bal_assets_diff, self.tag + '.spe_bal_assets_diff', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.tot_bal_assets_diff, self.tag + '.tot_bal_assets_diff', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.spe_cur_liab_diff, self.tag + '.spe_cur_liab_diff', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.tot_cur_liab_diff, self.tag + '.tot_cur_liab_diff', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.spe_non_cur_liab_diff, self.tag + '.spe_non_cur_liab_diff', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.tot_non_cur_liab_diff, self.tag + '.tot_non_cur_liab_diff', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.spe_bal_liab_diff, self.tag + '.spe_bal_liab_diff', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.tot_bal_liab_diff, self.tag + '.tot_bal_liab_diff', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.spe_bal_shrhldr_eqy_diff, self.tag + '.spe_bal_shrhldr_eqy_diff', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.tot_bal_shrhldr_eqy_diff, self.tag + '.tot_bal_shrhldr_eqy_diff', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.spe_bal_liab_eqy_diff, self.tag + '.spe_bal_liab_eqy_diff', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.tot_bal_liab_eqy_diff, self.tag + '.tot_bal_liab_eqy_diff', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.lt_payroll_payable, self.tag + '.lt_payroll_payable', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.other_comp_income, self.tag + '.other_comp_income', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.other_equity_tools, self.tag + '.other_equity_tools', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.other_equity_tools_p_shr, self.tag + '.other_equity_tools_p_shr', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.lending_funds, self.tag + '.lending_funds', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.accounts_receivable, self.tag + '.accounts_receivable', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.st_financing_payable, self.tag + '.st_financing_payable', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.payables, self.tag + '.payables', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.tot_shr, self.tag + '.tot_shr', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.hfs_assets, self.tag + '.hfs_assets', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.hfs_sales, self.tag + '.hfs_sales', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.fin_assets_cost_sharing, self.tag + '.fin_assets_cost_sharing', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.fin_assets_fair_value, self.tag + '.fin_assets_fair_value', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.contractual_assets, self.tag + '.contractual_assets', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.contract_liabilities, self.tag + '.contract_liabilities', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.accounts_receivable_bill, self.tag + '.accounts_receivable_bill', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.accounts_payable, self.tag + '.accounts_payable', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.oth_rcv_tot, self.tag + '.oth_rcv_tot', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.stm_bs_tot, self.tag + '.stm_bs_tot', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.const_in_prog_tot, self.tag + '.const_in_prog_tot', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.oth_payable_tot, self.tag + '.oth_payable_tot', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.lt_payable_tot, self.tag + '.lt_payable_tot', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.debt_investment, self.tag + '.debt_investment', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.other_debt_investment, self.tag + '.other_debt_investment', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.other_equity_investment, self.tag + '.other_equity_investment', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.other_illiquidfinancial_assets, self.tag + '.other_illiquidfinancial_assets', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.other_sustainable_bond, self.tag + '.other_sustainable_bond', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.receivables_financing, self.tag + '.receivables_financing', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.right_use_assets, self.tag + '.right_use_assets', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.lease_liab, self.tag + '.lease_liab', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.iflisted_data, self.tag + '.iflisted_data', len(uv.Dates), len(uv.Instruments), self.nquarters)
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
        dr.registerData(self.mid, self.monetary_cap, self.tag + '.monetary_cap')
        dr.registerData(self.mid, self.tradable_fin_assets, self.tag + '.tradable_fin_assets')
        dr.registerData(self.mid, self.notes_rcv, self.tag + '.notes_rcv')
        dr.registerData(self.mid, self.acct_rcv, self.tag + '.acct_rcv')
        dr.registerData(self.mid, self.oth_rcv, self.tag + '.oth_rcv')
        dr.registerData(self.mid, self.prepay, self.tag + '.prepay')
        dr.registerData(self.mid, self.dvd_rcv, self.tag + '.dvd_rcv')
        dr.registerData(self.mid, self.int_rcv, self.tag + '.int_rcv')
        dr.registerData(self.mid, self.inventories, self.tag + '.inventories')
        dr.registerData(self.mid, self.consumptive_bio_assets, self.tag + '.consumptive_bio_assets')
        dr.registerData(self.mid, self.deferred_exp, self.tag + '.deferred_exp')
        dr.registerData(self.mid, self.non_cur_assets_due_within_1y, self.tag + '.non_cur_assets_due_within_1y')
        dr.registerData(self.mid, self.settle_rsrv, self.tag + '.settle_rsrv')
        dr.registerData(self.mid, self.loans_to_oth_banks, self.tag + '.loans_to_oth_banks')
        dr.registerData(self.mid, self.prem_rcv, self.tag + '.prem_rcv')
        dr.registerData(self.mid, self.rcv_from_reinsurer, self.tag + '.rcv_from_reinsurer')
        dr.registerData(self.mid, self.rcv_from_ceded_insur_cont_rsrv, self.tag + '.rcv_from_ceded_insur_cont_rsrv')
        dr.registerData(self.mid, self.red_monetary_cap_for_sale, self.tag + '.red_monetary_cap_for_sale')
        dr.registerData(self.mid, self.oth_cur_assets, self.tag + '.oth_cur_assets')
        dr.registerData(self.mid, self.tot_cur_assets, self.tag + '.tot_cur_assets')
        dr.registerData(self.mid, self.fin_assets_avail_for_sale, self.tag + '.fin_assets_avail_for_sale')
        dr.registerData(self.mid, self.held_to_mty_invest, self.tag + '.held_to_mty_invest')
        dr.registerData(self.mid, self.long_term_eqy_invest, self.tag + '.long_term_eqy_invest')
        dr.registerData(self.mid, self.invest_real_estate, self.tag + '.invest_real_estate')
        dr.registerData(self.mid, self.time_deposits, self.tag + '.time_deposits')
        dr.registerData(self.mid, self.oth_assets, self.tag + '.oth_assets')
        dr.registerData(self.mid, self.long_term_rec, self.tag + '.long_term_rec')
        dr.registerData(self.mid, self.fix_assets, self.tag + '.fix_assets')
        dr.registerData(self.mid, self.const_in_prog, self.tag + '.const_in_prog')
        dr.registerData(self.mid, self.proj_matl, self.tag + '.proj_matl')
        dr.registerData(self.mid, self.fix_assets_disp, self.tag + '.fix_assets_disp')
        dr.registerData(self.mid, self.productive_bio_assets, self.tag + '.productive_bio_assets')
        dr.registerData(self.mid, self.oil_and_natural_gas_assets, self.tag + '.oil_and_natural_gas_assets')
        dr.registerData(self.mid, self.intang_assets, self.tag + '.intang_assets')
        dr.registerData(self.mid, self.r_and_d_costs, self.tag + '.r_and_d_costs')
        dr.registerData(self.mid, self.goodwill, self.tag + '.goodwill')
        dr.registerData(self.mid, self.long_term_deferred_exp, self.tag + '.long_term_deferred_exp')
        dr.registerData(self.mid, self.deferred_tax_assets, self.tag + '.deferred_tax_assets')
        dr.registerData(self.mid, self.loans_and_adv_granted, self.tag + '.loans_and_adv_granted')
        dr.registerData(self.mid, self.oth_non_cur_assets, self.tag + '.oth_non_cur_assets')
        dr.registerData(self.mid, self.tot_non_cur_assets, self.tag + '.tot_non_cur_assets')
        dr.registerData(self.mid, self.cash_deposits_central_bank, self.tag + '.cash_deposits_central_bank')
        dr.registerData(self.mid, self.asset_dep_oth_banks_fin_inst, self.tag + '.asset_dep_oth_banks_fin_inst')
        dr.registerData(self.mid, self.precious_metals, self.tag + '.precious_metals')
        dr.registerData(self.mid, self.derivative_fin_assets, self.tag + '.derivative_fin_assets')
        dr.registerData(self.mid, self.agency_bus_assets, self.tag + '.agency_bus_assets')
        dr.registerData(self.mid, self.subr_rec, self.tag + '.subr_rec')
        dr.registerData(self.mid, self.rcv_ceded_unearned_prem_rsrv, self.tag + '.rcv_ceded_unearned_prem_rsrv')
        dr.registerData(self.mid, self.rcv_ceded_claim_rsrv, self.tag + '.rcv_ceded_claim_rsrv')
        dr.registerData(self.mid, self.rcv_ceded_life_insur_rsrv, self.tag + '.rcv_ceded_life_insur_rsrv')
        dr.registerData(self.mid, self.rcv_ceded_lt_health_insur_rsrv, self.tag + '.rcv_ceded_lt_health_insur_rsrv')
        dr.registerData(self.mid, self.mrgn_paid, self.tag + '.mrgn_paid')
        dr.registerData(self.mid, self.insured_pledge_loan, self.tag + '.insured_pledge_loan')
        dr.registerData(self.mid, self.cap_mrgn_paid, self.tag + '.cap_mrgn_paid')
        dr.registerData(self.mid, self.independent_acct_assets, self.tag + '.independent_acct_assets')
        dr.registerData(self.mid, self.clients_cap_deposit, self.tag + '.clients_cap_deposit')
        dr.registerData(self.mid, self.clients_rsrv_settle, self.tag + '.clients_rsrv_settle')
        dr.registerData(self.mid, self.incl_seat_fees_exchange, self.tag + '.incl_seat_fees_exchange')
        dr.registerData(self.mid, self.rcv_invest, self.tag + '.rcv_invest')
        dr.registerData(self.mid, self.tot_assets, self.tag + '.tot_assets')
        dr.registerData(self.mid, self.st_borrow, self.tag + '.st_borrow')
        dr.registerData(self.mid, self.borrow_central_bank, self.tag + '.borrow_central_bank')
        dr.registerData(self.mid, self.deposit_received_ib_deposits, self.tag + '.deposit_received_ib_deposits')
        dr.registerData(self.mid, self.loans_oth_banks, self.tag + '.loans_oth_banks')
        dr.registerData(self.mid, self.tradable_fin_liab, self.tag + '.tradable_fin_liab')
        dr.registerData(self.mid, self.notes_payable, self.tag + '.notes_payable')
        dr.registerData(self.mid, self.acct_payable, self.tag + '.acct_payable')
        dr.registerData(self.mid, self.adv_from_cust, self.tag + '.adv_from_cust')
        dr.registerData(self.mid, self.fund_sales_fin_assets_rp, self.tag + '.fund_sales_fin_assets_rp')
        dr.registerData(self.mid, self.handling_charges_comm_payable, self.tag + '.handling_charges_comm_payable')
        dr.registerData(self.mid, self.empl_ben_payable, self.tag + '.empl_ben_payable')
        dr.registerData(self.mid, self.taxes_surcharges_payable, self.tag + '.taxes_surcharges_payable')
        dr.registerData(self.mid, self.int_payable, self.tag + '.int_payable')
        dr.registerData(self.mid, self.dvd_payable, self.tag + '.dvd_payable')
        dr.registerData(self.mid, self.oth_payable, self.tag + '.oth_payable')
        dr.registerData(self.mid, self.acc_exp, self.tag + '.acc_exp')
        dr.registerData(self.mid, self.deferred_inc, self.tag + '.deferred_inc')
        dr.registerData(self.mid, self.st_bonds_payable, self.tag + '.st_bonds_payable')
        dr.registerData(self.mid, self.payable_to_reinsurer, self.tag + '.payable_to_reinsurer')
        dr.registerData(self.mid, self.rsrv_insur_cont, self.tag + '.rsrv_insur_cont')
        dr.registerData(self.mid, self.acting_trading_sec, self.tag + '.acting_trading_sec')
        dr.registerData(self.mid, self.acting_uw_sec, self.tag + '.acting_uw_sec')
        dr.registerData(self.mid, self.non_cur_liab_due_within_1y, self.tag + '.non_cur_liab_due_within_1y')
        dr.registerData(self.mid, self.oth_cur_liab, self.tag + '.oth_cur_liab')
        dr.registerData(self.mid, self.tot_cur_liab, self.tag + '.tot_cur_liab')
        dr.registerData(self.mid, self.lt_borrow, self.tag + '.lt_borrow')
        dr.registerData(self.mid, self.bonds_payable, self.tag + '.bonds_payable')
        dr.registerData(self.mid, self.lt_payable, self.tag + '.lt_payable')
        dr.registerData(self.mid, self.specific_item_payable, self.tag + '.specific_item_payable')
        dr.registerData(self.mid, self.provisions, self.tag + '.provisions')
        dr.registerData(self.mid, self.deferred_tax_liab, self.tag + '.deferred_tax_liab')
        dr.registerData(self.mid, self.deferred_inc_non_cur_liab, self.tag + '.deferred_inc_non_cur_liab')
        dr.registerData(self.mid, self.oth_non_cur_liab, self.tag + '.oth_non_cur_liab')
        dr.registerData(self.mid, self.tot_non_cur_liab, self.tag + '.tot_non_cur_liab')
        dr.registerData(self.mid, self.liab_dep_oth_banks_fin_inst, self.tag + '.liab_dep_oth_banks_fin_inst')
        dr.registerData(self.mid, self.derivative_fin_liab, self.tag + '.derivative_fin_liab')
        dr.registerData(self.mid, self.cust_bank_dep, self.tag + '.cust_bank_dep')
        dr.registerData(self.mid, self.agency_bus_liab, self.tag + '.agency_bus_liab')
        dr.registerData(self.mid, self.oth_liab, self.tag + '.oth_liab')
        dr.registerData(self.mid, self.prem_received_adv, self.tag + '.prem_received_adv')
        dr.registerData(self.mid, self.deposit_received, self.tag + '.deposit_received')
        dr.registerData(self.mid, self.insured_deposit_invest, self.tag + '.insured_deposit_invest')
        dr.registerData(self.mid, self.unearned_prem_rsrv, self.tag + '.unearned_prem_rsrv')
        dr.registerData(self.mid, self.out_loss_rsrv, self.tag + '.out_loss_rsrv')
        dr.registerData(self.mid, self.life_insur_rsrv, self.tag + '.life_insur_rsrv')
        dr.registerData(self.mid, self.lt_health_insur_v, self.tag + '.lt_health_insur_v')
        dr.registerData(self.mid, self.independent_acct_liab, self.tag + '.independent_acct_liab')
        dr.registerData(self.mid, self.incl_pledge_loan, self.tag + '.incl_pledge_loan')
        dr.registerData(self.mid, self.claims_payable, self.tag + '.claims_payable')
        dr.registerData(self.mid, self.dvd_payable_insured, self.tag + '.dvd_payable_insured')
        dr.registerData(self.mid, self.tot_liab, self.tag + '.tot_liab')
        dr.registerData(self.mid, self.cap_stk, self.tag + '.cap_stk')
        dr.registerData(self.mid, self.cap_rsrv, self.tag + '.cap_rsrv')
        dr.registerData(self.mid, self.special_rsrv, self.tag + '.special_rsrv')
        dr.registerData(self.mid, self.surplus_rsrv, self.tag + '.surplus_rsrv')
        dr.registerData(self.mid, self.undistributed_profit, self.tag + '.undistributed_profit')
        dr.registerData(self.mid, self.less_tsy_stk, self.tag + '.less_tsy_stk')
        dr.registerData(self.mid, self.prov_nom_risks, self.tag + '.prov_nom_risks')
        dr.registerData(self.mid, self.cnvd_diff_foreign_curr_stat, self.tag + '.cnvd_diff_foreign_curr_stat')
        dr.registerData(self.mid, self.unconfirmed_invest_loss, self.tag + '.unconfirmed_invest_loss')
        dr.registerData(self.mid, self.minority_int, self.tag + '.minority_int')
        dr.registerData(self.mid, self.tot_shrhldr_eqy_excl_min_int, self.tag + '.tot_shrhldr_eqy_excl_min_int')
        dr.registerData(self.mid, self.tot_shrhldr_eqy_incl_min_int, self.tag + '.tot_shrhldr_eqy_incl_min_int')
        dr.registerData(self.mid, self.tot_liab_shrhldr_eqy, self.tag + '.tot_liab_shrhldr_eqy')
        dr.registerData(self.mid, self.spe_cur_assets_diff, self.tag + '.spe_cur_assets_diff')
        dr.registerData(self.mid, self.tot_cur_assets_diff, self.tag + '.tot_cur_assets_diff')
        dr.registerData(self.mid, self.spe_non_cur_assets_diff, self.tag + '.spe_non_cur_assets_diff')
        dr.registerData(self.mid, self.tot_non_cur_assets_diff, self.tag + '.tot_non_cur_assets_diff')
        dr.registerData(self.mid, self.spe_bal_assets_diff, self.tag + '.spe_bal_assets_diff')
        dr.registerData(self.mid, self.tot_bal_assets_diff, self.tag + '.tot_bal_assets_diff')
        dr.registerData(self.mid, self.spe_cur_liab_diff, self.tag + '.spe_cur_liab_diff')
        dr.registerData(self.mid, self.tot_cur_liab_diff, self.tag + '.tot_cur_liab_diff')
        dr.registerData(self.mid, self.spe_non_cur_liab_diff, self.tag + '.spe_non_cur_liab_diff')
        dr.registerData(self.mid, self.tot_non_cur_liab_diff, self.tag + '.tot_non_cur_liab_diff')
        dr.registerData(self.mid, self.spe_bal_liab_diff, self.tag + '.spe_bal_liab_diff')
        dr.registerData(self.mid, self.tot_bal_liab_diff, self.tag + '.tot_bal_liab_diff')
        dr.registerData(self.mid, self.spe_bal_shrhldr_eqy_diff, self.tag + '.spe_bal_shrhldr_eqy_diff')
        dr.registerData(self.mid, self.tot_bal_shrhldr_eqy_diff, self.tag + '.tot_bal_shrhldr_eqy_diff')
        dr.registerData(self.mid, self.spe_bal_liab_eqy_diff, self.tag + '.spe_bal_liab_eqy_diff')
        dr.registerData(self.mid, self.tot_bal_liab_eqy_diff, self.tag + '.tot_bal_liab_eqy_diff')
        dr.registerData(self.mid, self.lt_payroll_payable, self.tag + '.lt_payroll_payable')
        dr.registerData(self.mid, self.other_comp_income, self.tag + '.other_comp_income')
        dr.registerData(self.mid, self.other_equity_tools, self.tag + '.other_equity_tools')
        dr.registerData(self.mid, self.other_equity_tools_p_shr, self.tag + '.other_equity_tools_p_shr')
        dr.registerData(self.mid, self.lending_funds, self.tag + '.lending_funds')
        dr.registerData(self.mid, self.accounts_receivable, self.tag + '.accounts_receivable')
        dr.registerData(self.mid, self.st_financing_payable, self.tag + '.st_financing_payable')
        dr.registerData(self.mid, self.payables, self.tag + '.payables')
        dr.registerData(self.mid, self.tot_shr, self.tag + '.tot_shr')
        dr.registerData(self.mid, self.hfs_assets, self.tag + '.hfs_assets')
        dr.registerData(self.mid, self.hfs_sales, self.tag + '.hfs_sales')
        dr.registerData(self.mid, self.fin_assets_cost_sharing, self.tag + '.fin_assets_cost_sharing')
        dr.registerData(self.mid, self.fin_assets_fair_value, self.tag + '.fin_assets_fair_value')
        dr.registerData(self.mid, self.contractual_assets, self.tag + '.contractual_assets')
        dr.registerData(self.mid, self.contract_liabilities, self.tag + '.contract_liabilities')
        dr.registerData(self.mid, self.accounts_receivable_bill, self.tag + '.accounts_receivable_bill')
        dr.registerData(self.mid, self.accounts_payable, self.tag + '.accounts_payable')
        dr.registerData(self.mid, self.oth_rcv_tot, self.tag + '.oth_rcv_tot')
        dr.registerData(self.mid, self.stm_bs_tot, self.tag + '.stm_bs_tot')
        dr.registerData(self.mid, self.const_in_prog_tot, self.tag + '.const_in_prog_tot')
        dr.registerData(self.mid, self.oth_payable_tot, self.tag + '.oth_payable_tot')
        dr.registerData(self.mid, self.lt_payable_tot, self.tag + '.lt_payable_tot')
        dr.registerData(self.mid, self.debt_investment, self.tag + '.debt_investment')
        dr.registerData(self.mid, self.other_debt_investment, self.tag + '.other_debt_investment')
        dr.registerData(self.mid, self.other_equity_investment, self.tag + '.other_equity_investment')
        dr.registerData(self.mid, self.other_illiquidfinancial_assets, self.tag + '.other_illiquidfinancial_assets')
        dr.registerData(self.mid, self.other_sustainable_bond, self.tag + '.other_sustainable_bond')
        dr.registerData(self.mid, self.receivables_financing, self.tag + '.receivables_financing')
        dr.registerData(self.mid, self.right_use_assets, self.tag + '.right_use_assets')
        dr.registerData(self.mid, self.lease_liab, self.tag + '.lease_liab')
        dr.registerData(self.mid, self.iflisted_data, self.tag + '.iflisted_data')
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
                    self.monetary_cap[di, qi, ii] = df_qi['monetary_cap']
                    self.tradable_fin_assets[di, qi, ii] = df_qi['tradable_fin_assets']
                    self.notes_rcv[di, qi, ii] = df_qi['notes_rcv']
                    self.acct_rcv[di, qi, ii] = df_qi['acct_rcv']
                    self.oth_rcv[di, qi, ii] = df_qi['oth_rcv']
                    self.prepay[di, qi, ii] = df_qi['prepay']
                    self.dvd_rcv[di, qi, ii] = df_qi['dvd_rcv']
                    self.int_rcv[di, qi, ii] = df_qi['int_rcv']
                    self.inventories[di, qi, ii] = df_qi['inventories']
                    self.consumptive_bio_assets[di, qi, ii] = df_qi['consumptive_bio_assets']
                    self.deferred_exp[di, qi, ii] = df_qi['deferred_exp']
                    self.non_cur_assets_due_within_1y[di, qi, ii] = df_qi['non_cur_assets_due_within_1y']
                    self.settle_rsrv[di, qi, ii] = df_qi['settle_rsrv']
                    self.loans_to_oth_banks[di, qi, ii] = df_qi['loans_to_oth_banks']
                    self.prem_rcv[di, qi, ii] = df_qi['prem_rcv']
                    self.rcv_from_reinsurer[di, qi, ii] = df_qi['rcv_from_reinsurer']
                    self.rcv_from_ceded_insur_cont_rsrv[di, qi, ii] = df_qi['rcv_from_ceded_insur_cont_rsrv']
                    self.red_monetary_cap_for_sale[di, qi, ii] = df_qi['red_monetary_cap_for_sale']
                    self.oth_cur_assets[di, qi, ii] = df_qi['oth_cur_assets']
                    self.tot_cur_assets[di, qi, ii] = df_qi['tot_cur_assets']
                    self.fin_assets_avail_for_sale[di, qi, ii] = df_qi['fin_assets_avail_for_sale']
                    self.held_to_mty_invest[di, qi, ii] = df_qi['held_to_mty_invest']
                    self.long_term_eqy_invest[di, qi, ii] = df_qi['long_term_eqy_invest']
                    self.invest_real_estate[di, qi, ii] = df_qi['invest_real_estate']
                    self.time_deposits[di, qi, ii] = df_qi['time_deposits']
                    self.oth_assets[di, qi, ii] = df_qi['oth_assets']
                    self.long_term_rec[di, qi, ii] = df_qi['long_term_rec']
                    self.fix_assets[di, qi, ii] = df_qi['fix_assets']
                    self.const_in_prog[di, qi, ii] = df_qi['const_in_prog']
                    self.proj_matl[di, qi, ii] = df_qi['proj_matl']
                    self.fix_assets_disp[di, qi, ii] = df_qi['fix_assets_disp']
                    self.productive_bio_assets[di, qi, ii] = df_qi['productive_bio_assets']
                    self.oil_and_natural_gas_assets[di, qi, ii] = df_qi['oil_and_natural_gas_assets']
                    self.intang_assets[di, qi, ii] = df_qi['intang_assets']
                    self.r_and_d_costs[di, qi, ii] = df_qi['r_and_d_costs']
                    self.goodwill[di, qi, ii] = df_qi['goodwill']
                    self.long_term_deferred_exp[di, qi, ii] = df_qi['long_term_deferred_exp']
                    self.deferred_tax_assets[di, qi, ii] = df_qi['deferred_tax_assets']
                    self.loans_and_adv_granted[di, qi, ii] = df_qi['loans_and_adv_granted']
                    self.oth_non_cur_assets[di, qi, ii] = df_qi['oth_non_cur_assets']
                    self.tot_non_cur_assets[di, qi, ii] = df_qi['tot_non_cur_assets']
                    self.cash_deposits_central_bank[di, qi, ii] = df_qi['cash_deposits_central_bank']
                    self.asset_dep_oth_banks_fin_inst[di, qi, ii] = df_qi['asset_dep_oth_banks_fin_inst']
                    self.precious_metals[di, qi, ii] = df_qi['precious_metals']
                    self.derivative_fin_assets[di, qi, ii] = df_qi['derivative_fin_assets']
                    self.agency_bus_assets[di, qi, ii] = df_qi['agency_bus_assets']
                    self.subr_rec[di, qi, ii] = df_qi['subr_rec']
                    self.rcv_ceded_unearned_prem_rsrv[di, qi, ii] = df_qi['rcv_ceded_unearned_prem_rsrv']
                    self.rcv_ceded_claim_rsrv[di, qi, ii] = df_qi['rcv_ceded_claim_rsrv']
                    self.rcv_ceded_life_insur_rsrv[di, qi, ii] = df_qi['rcv_ceded_life_insur_rsrv']
                    self.rcv_ceded_lt_health_insur_rsrv[di, qi, ii] = df_qi['rcv_ceded_lt_health_insur_rsrv']
                    self.mrgn_paid[di, qi, ii] = df_qi['mrgn_paid']
                    self.insured_pledge_loan[di, qi, ii] = df_qi['insured_pledge_loan']
                    self.cap_mrgn_paid[di, qi, ii] = df_qi['cap_mrgn_paid']
                    self.independent_acct_assets[di, qi, ii] = df_qi['independent_acct_assets']
                    self.clients_cap_deposit[di, qi, ii] = df_qi['clients_cap_deposit']
                    self.clients_rsrv_settle[di, qi, ii] = df_qi['clients_rsrv_settle']
                    self.incl_seat_fees_exchange[di, qi, ii] = df_qi['incl_seat_fees_exchange']
                    self.rcv_invest[di, qi, ii] = df_qi['rcv_invest']
                    self.tot_assets[di, qi, ii] = df_qi['tot_assets']
                    self.st_borrow[di, qi, ii] = df_qi['st_borrow']
                    self.borrow_central_bank[di, qi, ii] = df_qi['borrow_central_bank']
                    self.deposit_received_ib_deposits[di, qi, ii] = df_qi['deposit_received_ib_deposits']
                    self.loans_oth_banks[di, qi, ii] = df_qi['loans_oth_banks']
                    self.tradable_fin_liab[di, qi, ii] = df_qi['tradable_fin_liab']
                    self.notes_payable[di, qi, ii] = df_qi['notes_payable']
                    self.acct_payable[di, qi, ii] = df_qi['acct_payable']
                    self.adv_from_cust[di, qi, ii] = df_qi['adv_from_cust']
                    self.fund_sales_fin_assets_rp[di, qi, ii] = df_qi['fund_sales_fin_assets_rp']
                    self.handling_charges_comm_payable[di, qi, ii] = df_qi['handling_charges_comm_payable']
                    self.empl_ben_payable[di, qi, ii] = df_qi['empl_ben_payable']
                    self.taxes_surcharges_payable[di, qi, ii] = df_qi['taxes_surcharges_payable']
                    self.int_payable[di, qi, ii] = df_qi['int_payable']
                    self.dvd_payable[di, qi, ii] = df_qi['dvd_payable']
                    self.oth_payable[di, qi, ii] = df_qi['oth_payable']
                    self.acc_exp[di, qi, ii] = df_qi['acc_exp']
                    self.deferred_inc[di, qi, ii] = df_qi['deferred_inc']
                    self.st_bonds_payable[di, qi, ii] = df_qi['st_bonds_payable']
                    self.payable_to_reinsurer[di, qi, ii] = df_qi['payable_to_reinsurer']
                    self.rsrv_insur_cont[di, qi, ii] = df_qi['rsrv_insur_cont']
                    self.acting_trading_sec[di, qi, ii] = df_qi['acting_trading_sec']
                    self.acting_uw_sec[di, qi, ii] = df_qi['acting_uw_sec']
                    self.non_cur_liab_due_within_1y[di, qi, ii] = df_qi['non_cur_liab_due_within_1y']
                    self.oth_cur_liab[di, qi, ii] = df_qi['oth_cur_liab']
                    self.tot_cur_liab[di, qi, ii] = df_qi['tot_cur_liab']
                    self.lt_borrow[di, qi, ii] = df_qi['lt_borrow']
                    self.bonds_payable[di, qi, ii] = df_qi['bonds_payable']
                    self.lt_payable[di, qi, ii] = df_qi['lt_payable']
                    self.specific_item_payable[di, qi, ii] = df_qi['specific_item_payable']
                    self.provisions[di, qi, ii] = df_qi['provisions']
                    self.deferred_tax_liab[di, qi, ii] = df_qi['deferred_tax_liab']
                    self.deferred_inc_non_cur_liab[di, qi, ii] = df_qi['deferred_inc_non_cur_liab']
                    self.oth_non_cur_liab[di, qi, ii] = df_qi['oth_non_cur_liab']
                    self.tot_non_cur_liab[di, qi, ii] = df_qi['tot_non_cur_liab']
                    self.liab_dep_oth_banks_fin_inst[di, qi, ii] = df_qi['liab_dep_oth_banks_fin_inst']
                    self.derivative_fin_liab[di, qi, ii] = df_qi['derivative_fin_liab']
                    self.cust_bank_dep[di, qi, ii] = df_qi['cust_bank_dep']
                    self.agency_bus_liab[di, qi, ii] = df_qi['agency_bus_liab']
                    self.oth_liab[di, qi, ii] = df_qi['oth_liab']
                    self.prem_received_adv[di, qi, ii] = df_qi['prem_received_adv']
                    self.deposit_received[di, qi, ii] = df_qi['deposit_received']
                    self.insured_deposit_invest[di, qi, ii] = df_qi['insured_deposit_invest']
                    self.unearned_prem_rsrv[di, qi, ii] = df_qi['unearned_prem_rsrv']
                    self.out_loss_rsrv[di, qi, ii] = df_qi['out_loss_rsrv']
                    self.life_insur_rsrv[di, qi, ii] = df_qi['life_insur_rsrv']
                    self.lt_health_insur_v[di, qi, ii] = df_qi['lt_health_insur_v']
                    self.independent_acct_liab[di, qi, ii] = df_qi['independent_acct_liab']
                    self.incl_pledge_loan[di, qi, ii] = df_qi['incl_pledge_loan']
                    self.claims_payable[di, qi, ii] = df_qi['claims_payable']
                    self.dvd_payable_insured[di, qi, ii] = df_qi['dvd_payable_insured']
                    self.tot_liab[di, qi, ii] = df_qi['tot_liab']
                    self.cap_stk[di, qi, ii] = df_qi['cap_stk']
                    self.cap_rsrv[di, qi, ii] = df_qi['cap_rsrv']
                    self.special_rsrv[di, qi, ii] = df_qi['special_rsrv']
                    self.surplus_rsrv[di, qi, ii] = df_qi['surplus_rsrv']
                    self.undistributed_profit[di, qi, ii] = df_qi['undistributed_profit']
                    self.less_tsy_stk[di, qi, ii] = df_qi['less_tsy_stk']
                    self.prov_nom_risks[di, qi, ii] = df_qi['prov_nom_risks']
                    self.cnvd_diff_foreign_curr_stat[di, qi, ii] = df_qi['cnvd_diff_foreign_curr_stat']
                    self.unconfirmed_invest_loss[di, qi, ii] = df_qi['unconfirmed_invest_loss']
                    self.minority_int[di, qi, ii] = df_qi['minority_int']
                    self.tot_shrhldr_eqy_excl_min_int[di, qi, ii] = df_qi['tot_shrhldr_eqy_excl_min_int']
                    self.tot_shrhldr_eqy_incl_min_int[di, qi, ii] = df_qi['tot_shrhldr_eqy_incl_min_int']
                    self.tot_liab_shrhldr_eqy[di, qi, ii] = df_qi['tot_liab_shrhldr_eqy']
                    self.spe_cur_assets_diff[di, qi, ii] = df_qi['spe_cur_assets_diff']
                    self.tot_cur_assets_diff[di, qi, ii] = df_qi['tot_cur_assets_diff']
                    self.spe_non_cur_assets_diff[di, qi, ii] = df_qi['spe_non_cur_assets_diff']
                    self.tot_non_cur_assets_diff[di, qi, ii] = df_qi['tot_non_cur_assets_diff']
                    self.spe_bal_assets_diff[di, qi, ii] = df_qi['spe_bal_assets_diff']
                    self.tot_bal_assets_diff[di, qi, ii] = df_qi['tot_bal_assets_diff']
                    self.spe_cur_liab_diff[di, qi, ii] = df_qi['spe_cur_liab_diff']
                    self.tot_cur_liab_diff[di, qi, ii] = df_qi['tot_cur_liab_diff']
                    self.spe_non_cur_liab_diff[di, qi, ii] = df_qi['spe_non_cur_liab_diff']
                    self.tot_non_cur_liab_diff[di, qi, ii] = df_qi['tot_non_cur_liab_diff']
                    self.spe_bal_liab_diff[di, qi, ii] = df_qi['spe_bal_liab_diff']
                    self.tot_bal_liab_diff[di, qi, ii] = df_qi['tot_bal_liab_diff']
                    self.spe_bal_shrhldr_eqy_diff[di, qi, ii] = df_qi['spe_bal_shrhldr_eqy_diff']
                    self.tot_bal_shrhldr_eqy_diff[di, qi, ii] = df_qi['tot_bal_shrhldr_eqy_diff']
                    self.spe_bal_liab_eqy_diff[di, qi, ii] = df_qi['spe_bal_liab_eqy_diff']
                    self.tot_bal_liab_eqy_diff[di, qi, ii] = df_qi['tot_bal_liab_eqy_diff']
                    self.lt_payroll_payable[di, qi, ii] = df_qi['lt_payroll_payable']
                    self.other_comp_income[di, qi, ii] = df_qi['other_comp_income']
                    self.other_equity_tools[di, qi, ii] = df_qi['other_equity_tools']
                    self.other_equity_tools_p_shr[di, qi, ii] = df_qi['other_equity_tools_p_shr']
                    self.lending_funds[di, qi, ii] = df_qi['lending_funds']
                    self.accounts_receivable[di, qi, ii] = df_qi['accounts_receivable']
                    self.st_financing_payable[di, qi, ii] = df_qi['st_financing_payable']
                    self.payables[di, qi, ii] = df_qi['payables']
                    self.tot_shr[di, qi, ii] = df_qi['tot_shr']
                    self.hfs_assets[di, qi, ii] = df_qi['hfs_assets']
                    self.hfs_sales[di, qi, ii] = df_qi['hfs_sales']
                    self.fin_assets_cost_sharing[di, qi, ii] = df_qi['fin_assets_cost_sharing']
                    self.fin_assets_fair_value[di, qi, ii] = df_qi['fin_assets_fair_value']
                    self.contractual_assets[di, qi, ii] = df_qi['contractual_assets']
                    self.contract_liabilities[di, qi, ii] = df_qi['contract_liabilities']
                    self.accounts_receivable_bill[di, qi, ii] = df_qi['accounts_receivable_bill']
                    self.accounts_payable[di, qi, ii] = df_qi['accounts_payable']
                    self.oth_rcv_tot[di, qi, ii] = df_qi['oth_rcv_tot']
                    self.stm_bs_tot[di, qi, ii] = df_qi['stm_bs_tot']
                    self.const_in_prog_tot[di, qi, ii] = df_qi['const_in_prog_tot']
                    self.oth_payable_tot[di, qi, ii] = df_qi['oth_payable_tot']
                    self.lt_payable_tot[di, qi, ii] = df_qi['lt_payable_tot']
                    self.debt_investment[di, qi, ii] = df_qi['debt_investment']
                    self.other_debt_investment[di, qi, ii] = df_qi['other_debt_investment']
                    self.other_equity_investment[di, qi, ii] = df_qi['other_equity_investment']
                    self.other_illiquidfinancial_assets[di, qi, ii] = df_qi['other_illiquidfinancial_assets']
                    self.other_sustainable_bond[di, qi, ii] = df_qi['other_sustainable_bond']
                    self.receivables_financing[di, qi, ii] = df_qi['receivables_financing']
                    self.right_use_assets[di, qi, ii] = df_qi['right_use_assets']
                    self.lease_liab[di, qi, ii] = df_qi['lease_liab']
                    self.iflisted_data[di, qi, ii] = df_qi['iflisted_data']
                    #######################################################################################################################

                    qi += 1

            except Exception as e:
                logging.error(f"{e}. Details: \
                                df_qi empty: \
                                qi: {qi}, 12 - qi - 1: {self.nquarters - qi - 1}, \
                                len of df_qi {len(df_qi)}, df_qi: {df_qi}")
                return


        for stock_name in self.stocks:
            work(stock_name)
