from odoo import fields, models, _


class CustomerReport(models.TransientModel):
    _name = 'customer.invoices.wizard'
    _description = 'customer invoices report'

    customer_id = fields.Many2one("res.partner", "customer")
    age = fields.Integer("Age")
    email = fields.Char(string="email")

    def view_pdf_report(self):
        print("hello")
