from odoo import fields, api, models


class TrialField(models.Model):
    _name = 'trial.field'
    _description = 'Trial Field'

    name = fields.Char(string='Name')
    category = fields.Many2one('fields.category')
