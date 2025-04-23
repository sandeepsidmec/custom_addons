from email.policy import default

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re
from datetime import datetime,date


class ResPartner(models.Model):
    _inherit = 'res.partner'

    gst_number = fields.Char(string="GST Number", size=15)
    customer_code = fields.Char(string="Customer Code", readonly=True, copy=False, default="new")

    date_of_birth = fields.Date(string="Date of Birth")
    age = fields.Integer(string="Age", compute="_compute_age", store=True)

    # Add GST number to res.partner in contacts
    @api.constrains('gst_number')
    def _check_gst_number(self):
        gst_regex = r'^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[1-9A-Z]{1}Z[0-9A-Z]{1}$'
        for partner in self:
            gst = partner.gst_number
            if gst:
                if len(gst) != 15:
                    raise ValidationError("GST Number must be exactly 15 characters long.")
                if not re.match(gst_regex, gst):
                    raise ValidationError("Invalid GST Number format.")

    # Add Customer Code to res.partner in contacts
    @api.model
    def create(self, vals):
        vals['customer_code'] = self.env['ir.sequence'].next_by_code('res.partner')
        return super(ResPartner, self).create(vals)


    # calculate age from date od birth
    @api.depends('date_of_birth')
    def _compute_age(self):
        today = date.today()
        for i in self:
            if i.date_of_birth:
                i.age = today.year - i.date_of_birth.year
            else:
                i.age = 0
