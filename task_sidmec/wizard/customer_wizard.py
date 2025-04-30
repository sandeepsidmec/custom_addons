from odoo import fields, models, _ , api
from odoo.exceptions import ValidationError


class CustomerReport(models.TransientModel):
    _name = 'customer.invoices.wizard'
    _description = 'customer invoices report'

    customer_id = fields.Many2one("res.partner", "customer")
    age = fields.Integer("Age")
    email = fields.Char(string="email")

    def view_pdf_report(self):
        """Trigger the PDF report using the selected customer"""
        task_customer = self.env['task.customer'].search([
            ('customer_id', '=', self.customer_id.id)
        ], limit=1)

        if not task_customer:
            raise ValidationError("No task.customer record found for the selected customer!")

        return self.env.ref('task_sidmec.report_customer_pdf').report_action(task_customer)

    @api.onchange('customer_id')
    def _onchange_customer(self):
        if self.customer_id:
            self.email = self.customer_id.email


