from datetime import datetime
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError
import base64


class ShipmentDocument(models.Model):
    _name = 'shipment.document'
    _description = 'Shipment Document'
    _order = 'name desc'

    name = fields.Char(string='Document Reference', required=True, copy=False, readonly=True, default='New')
    date = fields.Date(string='Date', default=fields.Date.context_today)
    description = fields.Text(string='Description')

    file = fields.Binary(string="Document File", required=True, attachment=True)
    filename = fields.Char(string="Filename", required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('done', 'Completed'),
    ], default='draft', string="Status", compute="compute_complete")

    # shipment_id = fields.Many2one('shipment.order', string="Related Shipment", required=True)

    # pdf extension
    @api.constrains('filename')
    def _check_pdf_extension(self):
        for rec in self:
            if rec.filename and not rec.filename.lower().endswith('.pdf'):
                raise ValidationError(_("Only PDF documents are allowed."))

    def compute_complete(self):
        for i in self:
            if i.file:
                i.state = "done"

    # 2. document with a reference to the shipment.
    def unlink(self):
        for i in self:
            if i.state == 'done':
                raise UserError(_("You cannot delete a document linked to a completed shipment."))
        return super().unlink()

    # unique document reference
    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('shipment.document')
        return super(ShipmentDocument, self).create(vals)
