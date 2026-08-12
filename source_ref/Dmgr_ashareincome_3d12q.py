from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import Universe as uv
from gsim.data import DataRegistry as dr
import pandas as pd
import glob
import logging


class DmgrAShareCashflow3d12q(DataManagerMapped):
    def __init__(self):
        DataManagerMapped.__init__(self)
        self.dataPath = ''
        self.nquarters = 12

        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s - %(levelname)s - %(message)s',
            filename='income.log'
        )

        ########################################################################################################################################
        self.report_period = NIO_CUBE()
        self.statement_type = NIO_CUBE()
        self.tot_oper_rev = NIO_CUBE()
        self.oper_rev = NIO_CUBE()
        self.int_inc = NIO_CUBE()
        self.net_int_inc = NIO_CUBE()
        self.insur_prem_unearned = NIO_CUBE()
        self.handling_chrg_comm_inc = NIO_CUBE()
        self.net_handling_chrg_comm_inc = NIO_CUBE()
        self.net_inc_other_ops = NIO_CUBE()
        self.plus_net_inc_other_bus = NIO_CUBE()
        self.prem_inc = NIO_CUBE()
        self.less_ceded_out_prem = NIO_CUBE()
        self.chg_unearned_prem_res = NIO_CUBE()
        self.incl_reinsurance_prem_inc = NIO_CUBE()
        self.net_inc_sec_trading_brok_bus = NIO_CUBE()
        self.net_inc_sec_uw_bus = NIO_CUBE()
        self.net_inc_ec_asset_mgmt_bus = NIO_CUBE()
        self.other_bus_inc = NIO_CUBE()
        self.plus_net_gain_chg_fv = NIO_CUBE()
        self.plus_net_invest_inc = NIO_CUBE()
        self.incl_inc_invest_assoc_jv_entp = NIO_CUBE()
        self.plus_net_gain_fx_trans = NIO_CUBE()
        self.tot_oper_cost = NIO_CUBE()
        self.less_oper_cost = NIO_CUBE()
        self.less_int_exp = NIO_CUBE()
        self.less_handling_chrg_comm_exp = NIO_CUBE()
        self.less_taxes_surcharges_ops = NIO_CUBE()
        self.less_selling_dist_exp = NIO_CUBE()
        self.less_gerl_admin_exp = NIO_CUBE()
        self.less_fin_exp = NIO_CUBE()
        self.less_impair_loss_assets = NIO_CUBE()
        self.prepay_surr = NIO_CUBE()
        self.tot_claim_exp = NIO_CUBE()
        self.chg_insur_cont_rsrv = NIO_CUBE()
        self.dvd_exp_insured = NIO_CUBE()
        self.reinsurance_exp = NIO_CUBE()
        self.oper_exp = NIO_CUBE()
        self.less_claim_recb_reinsurer = NIO_CUBE()
        self.less_ins_rsrv_recb_reinsurer = NIO_CUBE()
        self.less_exp_recb_reinsurer = NIO_CUBE()
        self.other_bus_cost = NIO_CUBE()
        self.oper_profit = NIO_CUBE()
        self.plus_non_oper_rev = NIO_CUBE()
        self.less_non_oper_exp = NIO_CUBE()
        self.il_net_loss_disp_noncur_asset = NIO_CUBE()
        self.tot_profit = NIO_CUBE()
        self.inc_tax = NIO_CUBE()
        self.unconfirmed_invest_loss = NIO_CUBE()
        self.net_profit_incl_min_int_inc = NIO_CUBE()
        self.net_profit_excl_min_int_inc = NIO_CUBE()
        self.minority_int_inc = NIO_CUBE()
        self.other_compreh_inc = NIO_CUBE()
        self.tot_compreh_inc = NIO_CUBE()
        self.tot_compreh_inc_parent_comp = NIO_CUBE()
        self.tot_compreh_inc_min_shrhldr = NIO_CUBE()
        self.ebit = NIO_CUBE()
        self.ebitda = NIO_CUBE()
        self.net_profit_after_ded_nr_lp = NIO_CUBE()
        self.net_profit_under_intl_acc_sta = NIO_CUBE()
        self.s_fa_eps_basic = NIO_CUBE()
        self.s_fa_eps_diluted = NIO_CUBE()
        self.actual_ann_dt = NIO_CUBE()
        self.insurance_expense = NIO_CUBE()
        self.spe_bal_oper_profit = NIO_CUBE()
        self.tot_bal_oper_profit = NIO_CUBE()
        self.spe_bal_tot_profit = NIO_CUBE()
        self.tot_bal_tot_profit = NIO_CUBE()
        self.spe_bal_net_profit = NIO_CUBE()
        self.tot_bal_net_profit = NIO_CUBE()
        self.undistributed_profit = NIO_CUBE()
        self.adjlossgain_prevyear = NIO_CUBE()
        self.transfer_from_surplusreserve = NIO_CUBE()
        self.transfer_from_housingimprest = NIO_CUBE()
        self.transfer_from_others = NIO_CUBE()
        self.distributable_profit = NIO_CUBE()
        self.withdr_legalsurplus = NIO_CUBE()
        self.withdr_legalpubwelfunds = NIO_CUBE()
        self.workers_welfare = NIO_CUBE()
        self.withdr_buzexpwelfare = NIO_CUBE()
        self.withdr_reservefund = NIO_CUBE()
        self.distributable_profit_shrhder = NIO_CUBE()
        self.prfshare_dvd_payable = NIO_CUBE()
        self.withdr_othersurpreserve = NIO_CUBE()
        self.comshare_dvd_payable = NIO_CUBE()
        self.capitalized_comstock_div = NIO_CUBE()
        self.net_after_ded_nr_lp_correct = NIO_CUBE()
        self.other_income = NIO_CUBE()
        self.asset_disposal_income = NIO_CUBE()
        self.continued_net_profit = NIO_CUBE()
        self.end_net_profit = NIO_CUBE()
        self.credit_impairment_loss = NIO_CUBE()
        self.net_exposure_hedging_benefits = NIO_CUBE()
        self.rd_expense = NIO_CUBE()
        self.stmnote_finexp = NIO_CUBE()
        self.fin_exp_int_inc = NIO_CUBE()
        self.is_calculation = NIO_CUBE()
        self.other_impair_loss_assets = NIO_CUBE()
        self.tot_oper_cost2 = NIO_CUBE()
        self.amodcost_fin_assets = NIO_CUBE()
        self.tot_opt_inc_dif = NIO_CUBE()
        self.tot_opt_cost_dif = NIO_CUBE()
        ########################################################################################################################################


    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.dataPath: str = cfg.getAttributeString('dataPath')
        self.nquarters: int = cfg.getAttributeDefault('nquarters', 12)
        
        ########################################################################################################################################
        self.addData(self.report_period, self.tag + '.report_period', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.statement_type, self.tag + '.statement_type', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.tot_oper_rev, self.tag + '.tot_oper_rev', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.oper_rev, self.tag + '.oper_rev', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.int_inc, self.tag + '.int_inc', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.net_int_inc, self.tag + '.net_int_inc', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.insur_prem_unearned, self.tag + '.insur_prem_unearned', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.handling_chrg_comm_inc, self.tag + '.handling_chrg_comm_inc', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.net_handling_chrg_comm_inc, self.tag + '.net_handling_chrg_comm_inc', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.net_inc_other_ops, self.tag + '.net_inc_other_ops', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.plus_net_inc_other_bus, self.tag + '.plus_net_inc_other_bus', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.prem_inc, self.tag + '.prem_inc', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.less_ceded_out_prem, self.tag + '.less_ceded_out_prem', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.chg_unearned_prem_res, self.tag + '.chg_unearned_prem_res', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.incl_reinsurance_prem_inc, self.tag + '.incl_reinsurance_prem_inc', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.net_inc_sec_trading_brok_bus, self.tag + '.net_inc_sec_trading_brok_bus', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.net_inc_sec_uw_bus, self.tag + '.net_inc_sec_uw_bus', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.net_inc_ec_asset_mgmt_bus, self.tag + '.net_inc_ec_asset_mgmt_bus', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.other_bus_inc, self.tag + '.other_bus_inc', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.plus_net_gain_chg_fv, self.tag + '.plus_net_gain_chg_fv', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.plus_net_invest_inc, self.tag + '.plus_net_invest_inc', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.incl_inc_invest_assoc_jv_entp, self.tag + '.incl_inc_invest_assoc_jv_entp', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.plus_net_gain_fx_trans, self.tag + '.plus_net_gain_fx_trans', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.tot_oper_cost, self.tag + '.tot_oper_cost', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.less_oper_cost, self.tag + '.less_oper_cost', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.less_int_exp, self.tag + '.less_int_exp', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.less_handling_chrg_comm_exp, self.tag + '.less_handling_chrg_comm_exp', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.less_taxes_surcharges_ops, self.tag + '.less_taxes_surcharges_ops', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.less_selling_dist_exp, self.tag + '.less_selling_dist_exp', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.less_gerl_admin_exp, self.tag + '.less_gerl_admin_exp', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.less_fin_exp, self.tag + '.less_fin_exp', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.less_impair_loss_assets, self.tag + '.less_impair_loss_assets', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.prepay_surr, self.tag + '.prepay_surr', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.tot_claim_exp, self.tag + '.tot_claim_exp', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.chg_insur_cont_rsrv, self.tag + '.chg_insur_cont_rsrv', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.dvd_exp_insured, self.tag + '.dvd_exp_insured', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.reinsurance_exp, self.tag + '.reinsurance_exp', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.oper_exp, self.tag + '.oper_exp', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.less_claim_recb_reinsurer, self.tag + '.less_claim_recb_reinsurer', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.less_ins_rsrv_recb_reinsurer, self.tag + '.less_ins_rsrv_recb_reinsurer', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.less_exp_recb_reinsurer, self.tag + '.less_exp_recb_reinsurer', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.other_bus_cost, self.tag + '.other_bus_cost', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.oper_profit, self.tag + '.oper_profit', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.plus_non_oper_rev, self.tag + '.plus_non_oper_rev', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.less_non_oper_exp, self.tag + '.less_non_oper_exp', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.il_net_loss_disp_noncur_asset, self.tag + '.il_net_loss_disp_noncur_asset', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.tot_profit, self.tag + '.tot_profit', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.inc_tax, self.tag + '.inc_tax', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.unconfirmed_invest_loss, self.tag + '.unconfirmed_invest_loss', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.net_profit_incl_min_int_inc, self.tag + '.net_profit_incl_min_int_inc', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.net_profit_excl_min_int_inc, self.tag + '.net_profit_excl_min_int_inc', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.minority_int_inc, self.tag + '.minority_int_inc', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.other_compreh_inc, self.tag + '.other_compreh_inc', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.tot_compreh_inc, self.tag + '.tot_compreh_inc', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.tot_compreh_inc_parent_comp, self.tag + '.tot_compreh_inc_parent_comp', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.tot_compreh_inc_min_shrhldr, self.tag + '.tot_compreh_inc_min_shrhldr', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.ebit, self.tag + '.ebit', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.ebitda, self.tag + '.ebitda', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.net_profit_after_ded_nr_lp, self.tag + '.net_profit_after_ded_nr_lp', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.net_profit_under_intl_acc_sta, self.tag + '.net_profit_under_intl_acc_sta', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.s_fa_eps_basic, self.tag + '.s_fa_eps_basic', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.s_fa_eps_diluted, self.tag + '.s_fa_eps_diluted', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.actual_ann_dt, self.tag + '.actual_ann_dt', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.insurance_expense, self.tag + '.insurance_expense', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.spe_bal_oper_profit, self.tag + '.spe_bal_oper_profit', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.tot_bal_oper_profit, self.tag + '.tot_bal_oper_profit', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.spe_bal_tot_profit, self.tag + '.spe_bal_tot_profit', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.tot_bal_tot_profit, self.tag + '.tot_bal_tot_profit', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.spe_bal_net_profit, self.tag + '.spe_bal_net_profit', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.tot_bal_net_profit, self.tag + '.tot_bal_net_profit', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.undistributed_profit, self.tag + '.undistributed_profit', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.adjlossgain_prevyear, self.tag + '.adjlossgain_prevyear', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.transfer_from_surplusreserve, self.tag + '.transfer_from_surplusreserve', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.transfer_from_housingimprest, self.tag + '.transfer_from_housingimprest', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.transfer_from_others, self.tag + '.transfer_from_others', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.distributable_profit, self.tag + '.distributable_profit', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.withdr_legalsurplus, self.tag + '.withdr_legalsurplus', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.withdr_legalpubwelfunds, self.tag + '.withdr_legalpubwelfunds', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.workers_welfare, self.tag + '.workers_welfare', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.withdr_buzexpwelfare, self.tag + '.withdr_buzexpwelfare', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.withdr_reservefund, self.tag + '.withdr_reservefund', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.distributable_profit_shrhder, self.tag + '.distributable_profit_shrhder', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.prfshare_dvd_payable, self.tag + '.prfshare_dvd_payable', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.withdr_othersurpreserve, self.tag + '.withdr_othersurpreserve', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.comshare_dvd_payable, self.tag + '.comshare_dvd_payable', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.capitalized_comstock_div, self.tag + '.capitalized_comstock_div', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.net_after_ded_nr_lp_correct, self.tag + '.net_after_ded_nr_lp_correct', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.other_income, self.tag + '.other_income', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.asset_disposal_income, self.tag + '.asset_disposal_income', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.continued_net_profit, self.tag + '.continued_net_profit', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.end_net_profit, self.tag + '.end_net_profit', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.credit_impairment_loss, self.tag + '.credit_impairment_loss', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.net_exposure_hedging_benefits, self.tag + '.net_exposure_hedging_benefits', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.rd_expense, self.tag + '.rd_expense', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.stmnote_finexp, self.tag + '.stmnote_finexp', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.fin_exp_int_inc, self.tag + '.fin_exp_int_inc', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.is_calculation, self.tag + '.is_calculation', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.other_impair_loss_assets, self.tag + '.other_impair_loss_assets', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.tot_oper_cost2, self.tag + '.tot_oper_cost2', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.amodcost_fin_assets, self.tag + '.amodcost_fin_assets', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.tot_opt_inc_dif, self.tag + '.tot_opt_inc_dif', len(uv.Dates), len(uv.Instruments), self.nquarters)
        self.addData(self.tot_opt_cost_dif, self.tag + '.tot_opt_cost_dif', len(uv.Dates), len(uv.Instruments), self.nquarters)
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
        dr.registerData(self.mid, self.report_period, self.tag + '.report_period')
        dr.registerData(self.mid, self.statement_type, self.tag + '.statement_type')
        dr.registerData(self.mid, self.tot_oper_rev, self.tag + '.tot_oper_rev')
        dr.registerData(self.mid, self.oper_rev, self.tag + '.oper_rev')
        dr.registerData(self.mid, self.int_inc, self.tag + '.int_inc')
        dr.registerData(self.mid, self.net_int_inc, self.tag + '.net_int_inc')
        dr.registerData(self.mid, self.insur_prem_unearned, self.tag + '.insur_prem_unearned')
        dr.registerData(self.mid, self.handling_chrg_comm_inc, self.tag + '.handling_chrg_comm_inc')
        dr.registerData(self.mid, self.net_handling_chrg_comm_inc, self.tag + '.net_handling_chrg_comm_inc')
        dr.registerData(self.mid, self.net_inc_other_ops, self.tag + '.net_inc_other_ops')
        dr.registerData(self.mid, self.plus_net_inc_other_bus, self.tag + '.plus_net_inc_other_bus')
        dr.registerData(self.mid, self.prem_inc, self.tag + '.prem_inc')
        dr.registerData(self.mid, self.less_ceded_out_prem, self.tag + '.less_ceded_out_prem')
        dr.registerData(self.mid, self.chg_unearned_prem_res, self.tag + '.chg_unearned_prem_res')
        dr.registerData(self.mid, self.incl_reinsurance_prem_inc, self.tag + '.incl_reinsurance_prem_inc')
        dr.registerData(self.mid, self.net_inc_sec_trading_brok_bus, self.tag + '.net_inc_sec_trading_brok_bus')
        dr.registerData(self.mid, self.net_inc_sec_uw_bus, self.tag + '.net_inc_sec_uw_bus')
        dr.registerData(self.mid, self.net_inc_ec_asset_mgmt_bus, self.tag + '.net_inc_ec_asset_mgmt_bus')
        dr.registerData(self.mid, self.other_bus_inc, self.tag + '.other_bus_inc')
        dr.registerData(self.mid, self.plus_net_gain_chg_fv, self.tag + '.plus_net_gain_chg_fv')
        dr.registerData(self.mid, self.plus_net_invest_inc, self.tag + '.plus_net_invest_inc')
        dr.registerData(self.mid, self.incl_inc_invest_assoc_jv_entp, self.tag + '.incl_inc_invest_assoc_jv_entp')
        dr.registerData(self.mid, self.plus_net_gain_fx_trans, self.tag + '.plus_net_gain_fx_trans')
        dr.registerData(self.mid, self.tot_oper_cost, self.tag + '.tot_oper_cost')
        dr.registerData(self.mid, self.less_oper_cost, self.tag + '.less_oper_cost')
        dr.registerData(self.mid, self.less_int_exp, self.tag + '.less_int_exp')
        dr.registerData(self.mid, self.less_handling_chrg_comm_exp, self.tag + '.less_handling_chrg_comm_exp')
        dr.registerData(self.mid, self.less_taxes_surcharges_ops, self.tag + '.less_taxes_surcharges_ops')
        dr.registerData(self.mid, self.less_selling_dist_exp, self.tag + '.less_selling_dist_exp')
        dr.registerData(self.mid, self.less_gerl_admin_exp, self.tag + '.less_gerl_admin_exp')
        dr.registerData(self.mid, self.less_fin_exp, self.tag + '.less_fin_exp')
        dr.registerData(self.mid, self.less_impair_loss_assets, self.tag + '.less_impair_loss_assets')
        dr.registerData(self.mid, self.prepay_surr, self.tag + '.prepay_surr')
        dr.registerData(self.mid, self.tot_claim_exp, self.tag + '.tot_claim_exp')
        dr.registerData(self.mid, self.chg_insur_cont_rsrv, self.tag + '.chg_insur_cont_rsrv')
        dr.registerData(self.mid, self.dvd_exp_insured, self.tag + '.dvd_exp_insured')
        dr.registerData(self.mid, self.reinsurance_exp, self.tag + '.reinsurance_exp')
        dr.registerData(self.mid, self.oper_exp, self.tag + '.oper_exp')
        dr.registerData(self.mid, self.less_claim_recb_reinsurer, self.tag + '.less_claim_recb_reinsurer')
        dr.registerData(self.mid, self.less_ins_rsrv_recb_reinsurer, self.tag + '.less_ins_rsrv_recb_reinsurer')
        dr.registerData(self.mid, self.less_exp_recb_reinsurer, self.tag + '.less_exp_recb_reinsurer')
        dr.registerData(self.mid, self.other_bus_cost, self.tag + '.other_bus_cost')
        dr.registerData(self.mid, self.oper_profit, self.tag + '.oper_profit')
        dr.registerData(self.mid, self.plus_non_oper_rev, self.tag + '.plus_non_oper_rev')
        dr.registerData(self.mid, self.less_non_oper_exp, self.tag + '.less_non_oper_exp')
        dr.registerData(self.mid, self.il_net_loss_disp_noncur_asset, self.tag + '.il_net_loss_disp_noncur_asset')
        dr.registerData(self.mid, self.tot_profit, self.tag + '.tot_profit')
        dr.registerData(self.mid, self.inc_tax, self.tag + '.inc_tax')
        dr.registerData(self.mid, self.unconfirmed_invest_loss, self.tag + '.unconfirmed_invest_loss')
        dr.registerData(self.mid, self.net_profit_incl_min_int_inc, self.tag + '.net_profit_incl_min_int_inc')
        dr.registerData(self.mid, self.net_profit_excl_min_int_inc, self.tag + '.net_profit_excl_min_int_inc')
        dr.registerData(self.mid, self.minority_int_inc, self.tag + '.minority_int_inc')
        dr.registerData(self.mid, self.other_compreh_inc, self.tag + '.other_compreh_inc')
        dr.registerData(self.mid, self.tot_compreh_inc, self.tag + '.tot_compreh_inc')
        dr.registerData(self.mid, self.tot_compreh_inc_parent_comp, self.tag + '.tot_compreh_inc_parent_comp')
        dr.registerData(self.mid, self.tot_compreh_inc_min_shrhldr, self.tag + '.tot_compreh_inc_min_shrhldr')
        dr.registerData(self.mid, self.ebit, self.tag + '.ebit')
        dr.registerData(self.mid, self.ebitda, self.tag + '.ebitda')
        dr.registerData(self.mid, self.net_profit_after_ded_nr_lp, self.tag + '.net_profit_after_ded_nr_lp')
        dr.registerData(self.mid, self.net_profit_under_intl_acc_sta, self.tag + '.net_profit_under_intl_acc_sta')
        dr.registerData(self.mid, self.s_fa_eps_basic, self.tag + '.s_fa_eps_basic')
        dr.registerData(self.mid, self.s_fa_eps_diluted, self.tag + '.s_fa_eps_diluted')
        dr.registerData(self.mid, self.actual_ann_dt, self.tag + '.actual_ann_dt')
        dr.registerData(self.mid, self.insurance_expense, self.tag + '.insurance_expense')
        dr.registerData(self.mid, self.spe_bal_oper_profit, self.tag + '.spe_bal_oper_profit')
        dr.registerData(self.mid, self.tot_bal_oper_profit, self.tag + '.tot_bal_oper_profit')
        dr.registerData(self.mid, self.spe_bal_tot_profit, self.tag + '.spe_bal_tot_profit')
        dr.registerData(self.mid, self.tot_bal_tot_profit, self.tag + '.tot_bal_tot_profit')
        dr.registerData(self.mid, self.spe_bal_net_profit, self.tag + '.spe_bal_net_profit')
        dr.registerData(self.mid, self.tot_bal_net_profit, self.tag + '.tot_bal_net_profit')
        dr.registerData(self.mid, self.undistributed_profit, self.tag + '.undistributed_profit')
        dr.registerData(self.mid, self.adjlossgain_prevyear, self.tag + '.adjlossgain_prevyear')
        dr.registerData(self.mid, self.transfer_from_surplusreserve, self.tag + '.transfer_from_surplusreserve')
        dr.registerData(self.mid, self.transfer_from_housingimprest, self.tag + '.transfer_from_housingimprest')
        dr.registerData(self.mid, self.transfer_from_others, self.tag + '.transfer_from_others')
        dr.registerData(self.mid, self.distributable_profit, self.tag + '.distributable_profit')
        dr.registerData(self.mid, self.withdr_legalsurplus, self.tag + '.withdr_legalsurplus')
        dr.registerData(self.mid, self.withdr_legalpubwelfunds, self.tag + '.withdr_legalpubwelfunds')
        dr.registerData(self.mid, self.workers_welfare, self.tag + '.workers_welfare')
        dr.registerData(self.mid, self.withdr_buzexpwelfare, self.tag + '.withdr_buzexpwelfare')
        dr.registerData(self.mid, self.withdr_reservefund, self.tag + '.withdr_reservefund')
        dr.registerData(self.mid, self.distributable_profit_shrhder, self.tag + '.distributable_profit_shrhder')
        dr.registerData(self.mid, self.prfshare_dvd_payable, self.tag + '.prfshare_dvd_payable')
        dr.registerData(self.mid, self.withdr_othersurpreserve, self.tag + '.withdr_othersurpreserve')
        dr.registerData(self.mid, self.comshare_dvd_payable, self.tag + '.comshare_dvd_payable')
        dr.registerData(self.mid, self.capitalized_comstock_div, self.tag + '.capitalized_comstock_div')
        dr.registerData(self.mid, self.net_after_ded_nr_lp_correct, self.tag + '.net_after_ded_nr_lp_correct')
        dr.registerData(self.mid, self.other_income, self.tag + '.other_income')
        dr.registerData(self.mid, self.asset_disposal_income, self.tag + '.asset_disposal_income')
        dr.registerData(self.mid, self.continued_net_profit, self.tag + '.continued_net_profit')
        dr.registerData(self.mid, self.end_net_profit, self.tag + '.end_net_profit')
        dr.registerData(self.mid, self.credit_impairment_loss, self.tag + '.credit_impairment_loss')
        dr.registerData(self.mid, self.net_exposure_hedging_benefits, self.tag + '.net_exposure_hedging_benefits')
        dr.registerData(self.mid, self.rd_expense, self.tag + '.rd_expense')
        dr.registerData(self.mid, self.stmnote_finexp, self.tag + '.stmnote_finexp')
        dr.registerData(self.mid, self.fin_exp_int_inc, self.tag + '.fin_exp_int_inc')
        dr.registerData(self.mid, self.is_calculation, self.tag + '.is_calculation')
        dr.registerData(self.mid, self.other_impair_loss_assets, self.tag + '.other_impair_loss_assets')
        dr.registerData(self.mid, self.tot_oper_cost2, self.tag + '.tot_oper_cost2')
        dr.registerData(self.mid, self.amodcost_fin_assets, self.tag + '.amodcost_fin_assets')
        dr.registerData(self.mid, self.tot_opt_inc_dif, self.tag + '.tot_opt_inc_dif')
        dr.registerData(self.mid, self.tot_opt_cost_dif, self.tag + '.tot_opt_cost_dif')
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
                    self.report_period[di, qi, ii] = int(df_qi['report_period'])
                    self.actual_ann_dt[di, qi, ii] = int(df_qi['actual_ann_dt'])

                    self.statement_type[di, qi, ii] = df_qi['statement_type']
                    self.tot_oper_rev[di, qi, ii] = df_qi['tot_oper_rev']
                    self.oper_rev[di, qi, ii] = df_qi['oper_rev']
                    self.int_inc[di, qi, ii] = df_qi['int_inc']
                    self.net_int_inc[di, qi, ii] = df_qi['net_int_inc']
                    self.insur_prem_unearned[di, qi, ii] = df_qi['insur_prem_unearned']
                    self.handling_chrg_comm_inc[di, qi, ii] = df_qi['handling_chrg_comm_inc']
                    self.net_handling_chrg_comm_inc[di, qi, ii] = df_qi['net_handling_chrg_comm_inc']
                    self.net_inc_other_ops[di, qi, ii] = df_qi['net_inc_other_ops']
                    self.plus_net_inc_other_bus[di, qi, ii] = df_qi['plus_net_inc_other_bus']
                    self.prem_inc[di, qi, ii] = df_qi['prem_inc']
                    self.less_ceded_out_prem[di, qi, ii] = df_qi['less_ceded_out_prem']
                    self.chg_unearned_prem_res[di, qi, ii] = df_qi['chg_unearned_prem_res']
                    self.incl_reinsurance_prem_inc[di, qi, ii] = df_qi['incl_reinsurance_prem_inc']
                    self.net_inc_sec_trading_brok_bus[di, qi, ii] = df_qi['net_inc_sec_trading_brok_bus']
                    self.net_inc_sec_uw_bus[di, qi, ii] = df_qi['net_inc_sec_uw_bus']
                    self.net_inc_ec_asset_mgmt_bus[di, qi, ii] = df_qi['net_inc_ec_asset_mgmt_bus']
                    self.other_bus_inc[di, qi, ii] = df_qi['other_bus_inc']
                    self.plus_net_gain_chg_fv[di, qi, ii] = df_qi['plus_net_gain_chg_fv']
                    self.plus_net_invest_inc[di, qi, ii] = df_qi['plus_net_invest_inc']
                    self.incl_inc_invest_assoc_jv_entp[di, qi, ii] = df_qi['incl_inc_invest_assoc_jv_entp']
                    self.plus_net_gain_fx_trans[di, qi, ii] = df_qi['plus_net_gain_fx_trans']
                    self.tot_oper_cost[di, qi, ii] = df_qi['tot_oper_cost']
                    self.less_oper_cost[di, qi, ii] = df_qi['less_oper_cost']
                    self.less_int_exp[di, qi, ii] = df_qi['less_int_exp']
                    self.less_handling_chrg_comm_exp[di, qi, ii] = df_qi['less_handling_chrg_comm_exp']
                    self.less_taxes_surcharges_ops[di, qi, ii] = df_qi['less_taxes_surcharges_ops']
                    self.less_selling_dist_exp[di, qi, ii] = df_qi['less_selling_dist_exp']
                    self.less_gerl_admin_exp[di, qi, ii] = df_qi['less_gerl_admin_exp']
                    self.less_fin_exp[di, qi, ii] = df_qi['less_fin_exp']
                    self.less_impair_loss_assets[di, qi, ii] = df_qi['less_impair_loss_assets']
                    self.prepay_surr[di, qi, ii] = df_qi['prepay_surr']
                    self.tot_claim_exp[di, qi, ii] = df_qi['tot_claim_exp']
                    self.chg_insur_cont_rsrv[di, qi, ii] = df_qi['chg_insur_cont_rsrv']
                    self.dvd_exp_insured[di, qi, ii] = df_qi['dvd_exp_insured']
                    self.reinsurance_exp[di, qi, ii] = df_qi['reinsurance_exp']
                    self.oper_exp[di, qi, ii] = df_qi['oper_exp']
                    self.less_claim_recb_reinsurer[di, qi, ii] = df_qi['less_claim_recb_reinsurer']
                    self.less_ins_rsrv_recb_reinsurer[di, qi, ii] = df_qi['less_ins_rsrv_recb_reinsurer']
                    self.less_exp_recb_reinsurer[di, qi, ii] = df_qi['less_exp_recb_reinsurer']
                    self.other_bus_cost[di, qi, ii] = df_qi['other_bus_cost']
                    self.oper_profit[di, qi, ii] = df_qi['oper_profit']
                    self.plus_non_oper_rev[di, qi, ii] = df_qi['plus_non_oper_rev']
                    self.less_non_oper_exp[di, qi, ii] = df_qi['less_non_oper_exp']
                    self.il_net_loss_disp_noncur_asset[di, qi, ii] = df_qi['il_net_loss_disp_noncur_asset']
                    self.tot_profit[di, qi, ii] = df_qi['tot_profit']
                    self.inc_tax[di, qi, ii] = df_qi['inc_tax']
                    self.unconfirmed_invest_loss[di, qi, ii] = df_qi['unconfirmed_invest_loss']
                    self.net_profit_incl_min_int_inc[di, qi, ii] = df_qi['net_profit_incl_min_int_inc']
                    self.net_profit_excl_min_int_inc[di, qi, ii] = df_qi['net_profit_excl_min_int_inc']
                    self.minority_int_inc[di, qi, ii] = df_qi['minority_int_inc']
                    self.other_compreh_inc[di, qi, ii] = df_qi['other_compreh_inc']
                    self.tot_compreh_inc[di, qi, ii] = df_qi['tot_compreh_inc']
                    self.tot_compreh_inc_parent_comp[di, qi, ii] = df_qi['tot_compreh_inc_parent_comp']
                    self.tot_compreh_inc_min_shrhldr[di, qi, ii] = df_qi['tot_compreh_inc_min_shrhldr']
                    self.ebit[di, qi, ii] = df_qi['ebit']
                    self.ebitda[di, qi, ii] = df_qi['ebitda']
                    self.net_profit_after_ded_nr_lp[di, qi, ii] = df_qi['net_profit_after_ded_nr_lp']
                    self.net_profit_under_intl_acc_sta[di, qi, ii] = df_qi['net_profit_under_intl_acc_sta']
                    self.s_fa_eps_basic[di, qi, ii] = df_qi['s_fa_eps_basic']
                    self.s_fa_eps_diluted[di, qi, ii] = df_qi['s_fa_eps_diluted']
                    self.insurance_expense[di, qi, ii] = df_qi['insurance_expense']
                    self.spe_bal_oper_profit[di, qi, ii] = df_qi['spe_bal_oper_profit']
                    self.tot_bal_oper_profit[di, qi, ii] = df_qi['tot_bal_oper_profit']
                    self.spe_bal_tot_profit[di, qi, ii] = df_qi['spe_bal_tot_profit']
                    self.tot_bal_tot_profit[di, qi, ii] = df_qi['tot_bal_tot_profit']
                    self.spe_bal_net_profit[di, qi, ii] = df_qi['spe_bal_net_profit']
                    self.tot_bal_net_profit[di, qi, ii] = df_qi['tot_bal_net_profit']
                    self.undistributed_profit[di, qi, ii] = df_qi['undistributed_profit']
                    self.adjlossgain_prevyear[di, qi, ii] = df_qi['adjlossgain_prevyear']
                    self.transfer_from_surplusreserve[di, qi, ii] = df_qi['transfer_from_surplusreserve']
                    self.transfer_from_housingimprest[di, qi, ii] = df_qi['transfer_from_housingimprest']
                    self.transfer_from_others[di, qi, ii] = df_qi['transfer_from_others']
                    self.distributable_profit[di, qi, ii] = df_qi['distributable_profit']
                    self.withdr_legalsurplus[di, qi, ii] = df_qi['withdr_legalsurplus']
                    self.withdr_legalpubwelfunds[di, qi, ii] = df_qi['withdr_legalpubwelfunds']
                    self.workers_welfare[di, qi, ii] = df_qi['workers_welfare']
                    self.withdr_buzexpwelfare[di, qi, ii] = df_qi['withdr_buzexpwelfare']
                    self.withdr_reservefund[di, qi, ii] = df_qi['withdr_reservefund']
                    self.distributable_profit_shrhder[di, qi, ii] = df_qi['distributable_profit_shrhder']
                    self.prfshare_dvd_payable[di, qi, ii] = df_qi['prfshare_dvd_payable']
                    self.withdr_othersurpreserve[di, qi, ii] = df_qi['withdr_othersurpreserve']
                    self.comshare_dvd_payable[di, qi, ii] = df_qi['comshare_dvd_payable']
                    self.capitalized_comstock_div[di, qi, ii] = df_qi['capitalized_comstock_div']
                    self.net_after_ded_nr_lp_correct[di, qi, ii] = df_qi['net_after_ded_nr_lp_correct']
                    self.other_income[di, qi, ii] = df_qi['other_income']
                    self.asset_disposal_income[di, qi, ii] = df_qi['asset_disposal_income']
                    self.continued_net_profit[di, qi, ii] = df_qi['continued_net_profit']
                    self.end_net_profit[di, qi, ii] = df_qi['end_net_profit']
                    self.credit_impairment_loss[di, qi, ii] = df_qi['credit_impairment_loss']
                    self.net_exposure_hedging_benefits[di, qi, ii] = df_qi['net_exposure_hedging_benefits']
                    self.rd_expense[di, qi, ii] = df_qi['rd_expense']
                    self.stmnote_finexp[di, qi, ii] = df_qi['stmnote_finexp']
                    self.fin_exp_int_inc[di, qi, ii] = df_qi['fin_exp_int_inc']
                    self.is_calculation[di, qi, ii] = df_qi['is_calculation']
                    self.other_impair_loss_assets[di, qi, ii] = df_qi['other_impair_loss_assets']
                    self.tot_oper_cost2[di, qi, ii] = df_qi['tot_oper_cost2']
                    self.amodcost_fin_assets[di, qi, ii] = df_qi['amodcost_fin_assets']
                    self.tot_opt_inc_dif[di, qi, ii] = df_qi['tot_opt_inc_dif']
                    self.tot_opt_cost_dif[di, qi, ii] = df_qi['tot_opt_cost_dif']
                    #######################################################################################################################

                    qi += 1

            except Exception as e:
                logging.error(f"{e}. Details:\n\
                                df_qi empty:\n\
                                qi: {qi}, 12 - qi - 1: {self.nquarters - qi - 1}\n\
                                len of df_qi {len(df_qi)}, df_qi: {df_qi}")
                return


        for stock_name in self.stocks:
            work(stock_name)
