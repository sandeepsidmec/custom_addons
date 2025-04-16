from odoo import models, fields


class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _rec_name = "name"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char("Name" , required=True)
    experience = fields.Integer("Experience")
