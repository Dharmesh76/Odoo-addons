from odoo import fields, api, models


class Category(models.Model):
    _name = 'fields.category'
    _description = 'field category'

    name = fields.Char(string='Name')