# -*- coding: utf-8 -*-
 
from odoo import api, fields, models, tools, SUPERUSER_ID
 

        
class on_change_function(models.Model):
    
    _inherit = 'sale.order'
    
@api.depends('x_tra_log_imp_perc', 'x_ma_oe_perc')
def _compute_tra_log_imp(self):
    for record in self:
        record.tra_log_imp = record.x_tra_log_imp_perc + record.x_ma_oe_perc 
        
        
@api.depends('amount_total', 'x_ma_oe_perc')
def _compute_ma_oe(self):
    for record in self:
        if record.amount_total > 0: 
            record.x_ma_oe = record.amount_total * record.x_ma_oe_perc / 100
        
        
@api.depends('amount_total', 'x_marg_mac_perc')
def _compute_marg_mac(self):
 for record in self:
    if record.amount_total > 0: 
        record.x_marg_mac = record.amount_total * record.x_marg_mac_perc / 100
        
        
@api.depends('amount_total', 'x_marg_mac', 'x_ma_oe')
def _compute_pri_mat_mo(self):
    for record in self:
        if record.amount_total > 0: 
            ecord.x_pri_mat_mo = record.amount_total  + record.x_marg_mac + record.x_ma_oe
        
        
        
@api.depends('x_pri_mat_mo')
def _compute_pri_tot(self):
    for record in self:
        if record.amount_total > 0: 
            record.x_pri_tot = record.x_pri_mat_mo
        
        

        

        

        
    x_tra_log_imp = fields.Float('Transport Et Logistique Import', compute='_product_price_ttc', readonly=True, store=True)

    x_marg_mac = fields.Monetary('Marge Mac Sys', store=True)
    x_pri_mat_mo = fields.Float('Prix Material+M.O', store=True)
    
    x_tra_log_imp_perc = fields.Float('Percentage transport et logistique Import(%)',store=True)
    x_ma_oe_perc = fields.Float('Main doeuvre(%)', store=True)
    x_marg_mac_perc = fields.Float('Percentage Marge MAC SYST (%)', compute='_product_price_ttc', store=True)
    x_pri_tot = fields.Monetary('prix total', store=True)
    x_ma_oe = fields.Float('main douevre', store=True)
    


        