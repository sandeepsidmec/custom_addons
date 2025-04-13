from odoo import models,fields

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    vendor_name = fields.Char("Vendor")