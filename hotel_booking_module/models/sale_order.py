from odoo import fields, api, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    booking_ref = fields.Many2one('hotel.booking', string='Booking Ref')
