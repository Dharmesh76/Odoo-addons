from odoo import api, models, fields


class HotelRoom(models.Model):
    _name = 'hotel.room'
    _description = 'Hotel Room'

    room_no = fields.Integer(string='Room Booking')

