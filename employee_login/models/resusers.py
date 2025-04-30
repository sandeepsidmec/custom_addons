from odoo import models, fields, api


class ResUser(models.Model):
    _inherit = "res.users"

    allowed_employees = fields.Many2many('hr.employee', string='Allowed Employee')


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    employee = fields.Many2one('hr.employee', string="Employee")
