from email.policy import default

from odoo import models, fields
from datetime import date


from odoo.api import ValuesType, Self


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _rec_name = "patient_id"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char("patient sequence", default="New")
    patient_id = fields.Many2one(comodel_name="res.partner", domain=[("email", "!=", False)], string="Name",
                                 tracking=True, required=True)

    email = fields.Char(related="patient_id.email", string="email")
    age = fields.Integer(string="Age")
    gender = fields.Selection([("male", "Male"), ("female", "Female")], "Gender")
    is_patient_in_ward = fields.Boolean("is patient in ward")
    admit_date = fields.Date("Admit date")
    discharge_date = fields.Date("discharge Date")
    doctor_names = fields.Many2many(comodel_name="hospital.doctor", string="Doctors")
    doctor_name = fields.Many2one(comodel_name="hospital.doctor", string="Doctor")
    date = fields.Date("Date")
    patient_lines = fields.One2many("hospital.appointment.line", "patient", "Order lines")

    user_id = fields.Many2one("res.users", "user")
    company_id = fields.Many2one("res.company", "Company")

    status = fields.Selection([("admit", "Admitted"), ("discharge", "Discharged")], "status", default='admit',
                              compute="status_date")
    image_1920 = fields.Binary("image")

    def create(self, vals):
        vals["user_id"] = self.env.user.id
        vals["company_id"] = self.env.user.company_id.id
        # vals["name"] = self.env['ir.sequence'].next_by_code('hospital.appointment')
        return super(HospitalAppointment, self).create(vals)

    """
    
    patient=-self.env["hospital.patient"].search([('id','=',self.id)})
    """

    """
       vals={
           "user_id": self.env.user.id,
           "company_id": self.env.user.company_id.id
       }
       
       self.env["hospital.patient"].create(vals)
       
       """

    def send_email(self):
        for rec in self:
            template = self.env.ref("hospital_management.mail_template_appointment_confirm")
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
        today = date.today()
        for i in self:
            if i.discharge_date and today > i.discharge_date:
                i.status = 'discharge'
            else:
                i.status = 'admit'

    def Confirm(self):
        for record in self:
            record.status = 'discharge'


class HospitalAppointmentLines(models.Model):
    _name = "hospital.appointment.line"

    product_id = fields.Many2one("product.product", "product Name")
    qty = fields.Integer("qty")
    unit_price = fields.Float("Unit price")
    subtotal = fields.Float("sub-total", compute="compute_subtotal")
    patient = fields.Many2one("hospital.appointment", "patient")

    def compute_subtotal(self):
        for i in self:
            i.subtotal = i.qty * i.unit_price
