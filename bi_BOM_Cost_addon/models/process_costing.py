# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models

class MrpProduction(models.Model):
    _inherit = "mrp.production"
        
    pro_material_cost_ids = fields.One2many(copy=True)
    pro_labour_cost_ids = fields.One2many(copy=True)
    pro_overhead_cost_ids = fields.One2many(copy=True)
    pro_total_material_cost = fields.Float(copy=True)
    
    
