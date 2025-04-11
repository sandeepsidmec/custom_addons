from odoo import models, fields

class CollegeTeacher(models.Model):
    _name = 'college.teacher'
    _description = 'Teacher info'

    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")
    dob = fields.Date(string="Date of Birth")
    gender = fields.Selection(string="Gender",selection=[
        ("female","Female"),
        ("male","Male")])
    Address = fields.Text(string="Address")
    subject = fields.Char(string="Subject")
