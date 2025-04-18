from odoo import models, fields
from datetime import date


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _rec_name = "patient_id"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    patient_id = fields.Many2one(comodel_name="res.partner", domain=[("email", "!=", False)], string="Name",
                                 tracking=True, required=True, stored=True)
    email = fields.Char(related="patient_id.email", string="email")
    age = fields.Integer(string="Age")
    gender = fields.Selection([("male", "Male"), ("female", "Female")], "Gender")
    is_patient_in_ward = fields.Boolean("is patient in ward")
    admit_date = fields.Date("Admit date")
    discharge_date = fields.Date("discharge Date")
    doctor_names = fields.Many2many(comodel_name="hospital.doctor", string="Doctors")
    date = fields.Date("Date")
    patient_lines = fields.One2many("hospital.patient.line", "patient", "Order lines")

    user_id = fields.Many2one("res.users", "user", compute="compute_user_company")
    company_id = fields.Many2one("res.company", "Company", compute="compute_user_company")

    status = fields.Selection([("admit", "Admitted"), ("discharge", "Discharged")], "status", default='admit',compute="status_date")
    image_1920 = fields.Binary("image")


    # @api.onchange("patient_id")
    # def onchange_patient_name(self):
    #     for rec in self:
    #         print(rec)
    #         rec.email = rec.patient_id.email

    # def compute_patient_email(self):
    #     for rec in self:
    #         rec.email = rec.patient_id.email

    def compute_user_company(self):
        for rec in self:
            rec.user_id = self.env.user
            rec.company_id = self.env.user.company_id.id

    def send_email(self):
        for rec in self:
            template = self.env.ref("hospital_management.mail_template_patient_confirm")
            template.send_mail(rec.id, force_send=True)

    def view_patient_lines(self):
        self.ensure_one()
        return {
            'name': "view patient invoices",
            'view_mode': 'list',
            'res_model': 'hospital.patient.line',
            'domain': [('patient', '=', self.id)],
            'type': 'ir.actions.act_window',
        }

    def status_date(self):
        today=date.today()
        for i in self:
            if today > i.discharge_date:
                i.status='discharge'
            else:
                i.status='admit'

class HospitalPatientLines(models.Model):
    _name = "hospital.patient.line"

    product_id = fields.Many2one("product.product", "product Name")
    qty = fields.Integer("qty")
    unit_price = fields.Float("Unit price")
    subtotal = fields.Float("sub-total", compute="subtotal")
    patient = fields.Many2one("hospital.patient", "patient")

    def subtotal(self):
        for i in self:
            i.subtotal = i.qty * i.unit_price
