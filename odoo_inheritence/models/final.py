from odoo import fields, api, models


class Final(models.Model):
    _name = 'final'
    _description = 'Final'

    trial1 = fields.Char('trail1')
    trial2 = fields.Char('trail2')
    trial3 = fields.Char('trail3')
