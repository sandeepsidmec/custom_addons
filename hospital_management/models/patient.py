from odoo import models, fields


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _rec_name = "patient_id"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    patient_id = fields.Many2one(comodel_name="res.partner", string="Name", tracking=True, required=True, )
    age = fields.Integer(string="Age")
    gender = fields.Selection([("male", "Male"), ("female", "Female")], "Gender")
    is_patient_in_ward = fields.Boolean("is patient in ward")
    admit_date = fields.Date("Admit date")
    discharge_date = fields.Date("discharge Date")

    patient_names = fields.Many2many(comodel_name="res.partner", string="Names")

