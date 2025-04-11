from odoo import models,fields

class college_courses(models.Model):
    _name = "college.courses"

    course_name = fields.Char("Course Name")
    course_fee = fields.Integer("Course Fee")