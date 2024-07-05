from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    refer_user = fields.Many2one('res.user', string='Refer User')
