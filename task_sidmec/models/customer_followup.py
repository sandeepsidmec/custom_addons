from odoo import models, fields, api
from datetime import date

class CustomerFollowup(models.Model):
    _name = 'customer.followup'
    _description = 'Customer Follow-up'

    name = fields.Char(string="Subject", required=True)
    user_id = fields.Many2one('res.users', string="Salesperson", required=True)
    followup_date = fields.Date(string="Follow-up Date", required=True)
    notes = fields.Text(string="Notes")

    @api.model
    def default_get(self, fields_list):
        # Call parent to get default values
        defaults = super().default_get(fields_list)

        if 'user_id' in fields_list:
            defaults['user_id'] = self.env.user

        if 'followup_date' in fields_list:
            defaults['followup_date'] = date.today()

        return defaults
