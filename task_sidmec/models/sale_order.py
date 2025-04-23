from odoo import models, _
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def unlink(self):
        for order in self:
            if order.state not in ['draft', 'sent', 'cancel']:
                raise UserError(_("You cannot delete a confirmed sales order."))
        return super(SaleOrder, self).unlink()
