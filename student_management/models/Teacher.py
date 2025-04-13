from odoo import models, fields

class CollegeTeacher(models.Model):
    _name = 'college.teacher'
    _description = 'Teacher info'
    _rec_name = 'name'

    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age")
    experience = fields.Integer(string="Experience")
    gender = fields.Selection(string="Gender",selection=[
        ("female","Female"),
        ("male","Male")])
    Address = fields.Text(string="Address")
    subject = fields.Char(string="Subject")
