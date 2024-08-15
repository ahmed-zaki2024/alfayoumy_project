from odoo import models, fields, api


class PosOrder(models.Model):
    _inherit = 'pos.order'

    state = fields.Selection(
        [('draft', 'New'), ('cancel', 'Cancelled'), ('paid', 'Paid'), ('done', 'Posted'), ('invoiced', 'Invoiced')],
        'Status', readonly=True, copy=False, default='draft', index=True)

    def action_payment(self):
        for rec in self:
            if rec.state != 'paid':
                rec.state = 'paid'
