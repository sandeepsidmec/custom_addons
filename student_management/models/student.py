from odoo import models, fields


class CollegeStudent(models.Model):
    _name = 'college.student'
    _description = 'student info'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "name"

    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")
    dob = fields.Date(string="Date of Birth")
    gender = fields.Selection(string="Gender", selection=[
        ("female", "Female"),
        ("male", "Male")])
    Address = fields.Text(string="Address")
