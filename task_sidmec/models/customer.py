from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.osv import expression


class TaskCustomer(models.Model):
    _name = "task.customer"
    _rec_name = "customer_id"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    customer_id = fields.Many2one(comodel_name="res.partner", domain=[("email", "!=", False), ("phone", "!=", False)],
                                  string="Name",
                                  tracking=True, required=True)
    age = fields.Integer("Age")
    email = fields.Char(string="email")
    phone = fields.Integer(string="Phone", compute="compute_phone")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('done', 'Completed'),
    ], default='draft', string="Status")
    image_1920 = fields.Binary("image")

    user_id = fields.Many2one("res.users", "user")
    company_id = fields.Many2one("res.company", "Company")

    # Task-1  send email
    def send_email(self):
        for rec in self:
            # print('hlo')

            template = self.env.ref("task_sidmec.mail_template_customer_confirm")
            ctx = {
                'default_model': 'task.customer',
                'default_res_ids': self.ids,
                'default_composition_mode': 'comment',
                'default_use_template': True,
                # 'default_email_layout_xmlid': 'task_sidmec.mail_template_customer_confirm',
                # 'email_notification_allow_footer': True,
                'default_template_id': template.id,
                # 'proforma': self.env.context.get('proforma', False),
            }
            action = {
                'type': 'ir.actions.act_window',
                'view_mode': 'form',
                'res_model': 'mail.compose.message',
                'views': [(False, 'form')],
                'view_id': False,
                'target': 'new',
                'context': ctx,
            }
            template.send_mail(rec.id, force_send=True)
            return action

    # user and company from env
    def compute_user_company(self):
        for rec in self:
            rec.user_id = self.env.user
            rec.company_id = self.env.user.company_id.id

    # Task-2  onchange method to autofill email
    @api.onchange("customer_id")
    def onchange_customer_name(self):
        for i in self:
            print(i)
            i.email = i.customer_id.email

    # Task-3 compute method to autofill phone
    def compute_phone(self):
        for i in self:
            i.phone = i.customer_id.phone

    # Task-4 @api.constrains to Validate Data on Save like age > 0
    @api.constrains("age")
    def check_age(self):
        for i in self:
            if i.age < 0:
                raise ValidationError("Age must be greater than 0")

    # Task-5


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        args = []
        domain = []
        if name:
            domain = expression.OR([
                [('name', operator, name)],
                [('phone', operator, name)],
                [('email', operator, name)],
            ])
        records = self.search(expression.AND([args, domain]), limit=limit)
        return [(rec.id, f"{rec.name}") for rec in self.browse(records.ids)]

