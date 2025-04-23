from odoo import models, fields, api
from datetime import date
from odoo.exceptions import ValidationError

class CollegeStudent(models.Model):
    _name = 'college.student'
    _description = 'student info'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "student_id"


    name = fields.Char("student sequence", default="New")
    student_id = fields.Many2one(comodel_name="res.partner", domain=[("email", "!=", False)], string="Name",
                                 tracking=True, required=True)
    email = fields.Char(string="email")
    mobile = fields.Char(related="student_id.mobile", string="Mobile")
    age = fields.Integer(string="Age")
    dob = fields.Date(string="Date of Birth")
    gender = fields.Selection(string="Gender", selection=[
        ("female", "Female"),
        ("male", "Male")])
    address = fields.Text(string="Address")
    student_names = fields.Many2many(comodel_name="res.partner", string="Contacts")
    teacher_id = fields.Many2one(comodel_name="college.teacher", string="Teacher", tracking=True)

    is_student_new = fields.Boolean("is student new")
    allotment_date = fields.Date("Allotment date")
    joining_date = fields.Date("Joining Date")

    student_lines = fields.One2many("college.student.line", "student", "Order lines")
    student_options = fields.One2many("college.student.option", "student1", "Optional Products")

    user_id = fields.Many2one("res.users", "user")
    company_id = fields.Many2one("res.company", "Company")
    # status bar
    status = fields.Selection([("alloted", "Alloted"), ("joined", "Joined")], "status", default='alloted',
                              compute="student_joining")
    image_1920 = fields.Binary("image")

    # email Constraints
    @api.constrains('email')
    def _check_email(self):
        for record in self:
            if record.email:
                if not record.email.lower().endswith('@gmail.com'):
                    raise ValidationError("Email must end with @gmail.com")

    # onchange method
    # @api.onchange("student_id")
    # def onchange_student_name(self):
    #     for rec in self:
    #         print(rec)
    #         rec.email = rec.student_id.email

    # COMPUTE METHOD
    # def compute_student_email(self):
    #     for rec in self:
    #         rec.email = rec.student_id.email

    # users and companies fetch
    # def compute_user_company(self):
    #     for rec in self:
    #         rec.user_id = self.env.user
    #         rec.company_id = self.env.user.company_id.id

    # add send email in header check student_confirm_mail and add button in header
    def send_email(self):
        for rec in self:
            template = self.env.ref("student_management.mail_template_student_confirm")
            template.send_mail(rec.id, force_send=True)

    #         SMART Button and add button in xml file in sheet and add list view in view_student_lines.xml
    def view_student_lines(self):
        self.ensure_one()
        return {
            'name': "view student joining",
            'view_mode': 'list',
            'res_model': 'college.student.line',
            'domain': [('student', '=', self.id)],
            'type': 'ir.actions.act_window',
        }

    # status bar automatic action add field in header
    def student_joining(self):
        today = date.today()
        for i in self:
            if i.joining_date and today > i.joining_date and i.allotment_date < i.joining_date:
                i.status = "joined"
            else:
                i.status = "alloted"
    # Create Method
    def create(self, vals):
        vals["user_id"] = self.env.user.id
        vals["company_id"] = self.env.user.company_id.id
        vals["name"] = self.env['ir.sequence'].next_by_code('college.student')
        return super(CollegeStudent, self).create(vals)


class collegeStudentLines(models.Model):
    _name = "college.student.line"

    book_id = fields.Many2one("product.product", "product Name")
    qty = fields.Integer("qty")
    unit_price = fields.Float(string="unit_price", compute="compute_student_unit_price")
    sub_total = fields.Float(string="subtotal", compute="subtotal")
    student = fields.Many2one("college.student", "student")

    def compute_student_unit_price(self):
        for i in self:
            i.unit_price = i.book_id.lst_price

    def subtotal(self):
        for i in self:
            i.sub_total = i.qty * i.unit_price


class collegeStudentOption(models.Model):
    _name = "college.student.option"

    book_id = fields.Many2one("product.product", "product Name")
    qty = fields.Integer("qty")
    unit_price = fields.Float(string="unit_price", compute="compute_student_unit_price")
    sub_total = fields.Float(string="subtotal", compute="subtotal")
    student1 = fields.Many2one("college.student", "student")

    def compute_student_unit_price(self):
        for i in self:
            i.unit_price = i.book_id.lst_price

    def subtotal(self):
        for i in self:
            i.sub_total = i.qty * i.unit_price
