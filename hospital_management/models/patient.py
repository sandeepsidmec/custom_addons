from odoo import models,fields


class HospitalPatient(models.Model):
    _name = "hospital.patient"

    patient_name=fields.Char(string="Name")
    age=fields.Integer(string="Age")


