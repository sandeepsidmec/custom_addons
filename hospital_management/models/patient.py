from odoo import models, fields


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _rec_name = "patient_name"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    patient_name = fields.Char(string="Name", tracking=True)
    age = fields.Integer(string="Age")
