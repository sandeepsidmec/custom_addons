from odoo import fields, models, _


class StudentReport(models.TransientModel):
    _name = 'student.invoices.wizard'
    _description = 'student invoices report'

    student_id = fields.Many2one("res.partner", "Student")
    allotment_date = fields.Date("Allotment Date")
    joining_date = fields.Date("Joining Date")

    def view_pdf_report(self):
        print("hello")
