from odoo import fields, api, models


class RoomBookingLines(models.Model):
    _name = 'hotel.room.booking.line'
    _description = 'Hotel Room Booking Lines'

    room