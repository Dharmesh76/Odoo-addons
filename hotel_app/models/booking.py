from odoo import fields, api, models


class HotelBooking(models.Model):
    _name = 'hotel_app.booking'
    _description = 'Hotel Booking'

    booking_ref = fields.Char(default='New')
    customer_id = fields.Many2one('res.partner', string='Customer')

