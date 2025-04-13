from typing import Required

from odoo import models, fields


class CollegeStudent(models.Model):
    _name = 'college.student'
    _description = 'student info'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "student_id"

    student_id = fields.Many2one(comodel_name="res.partner", string="Name", tracking=True, required=True, )
    age = fields.Integer(string="Age")
    dob = fields.Date(string="Date of Birth")
    gender = fields.Selection(string="Gender", selection=[
        ("female", "Female"),
        ("male", "Male")])
    address = fields.Text(string="Address")
    student_names = fields.Many2many(comodel_name="res.partner", string="Contacts")
    teacher_id = fields.Many2one(comodel_name="college.teacher", string="Teacher", tracking=True, required=True, )

    is_student_new = fields.Boolean("is student new")
    allotment_date = fields.Date("Allotment date")
    joining_date = fields.Date("Joining Date")
