from odoo import fields, api, models


class TodoList(models.Model):
    _name = 'owl.todo.list'

    name = fields.Char(string='Task Name')
    color = fields.Integer(string='Color')
    is_completed = fields.Boolean(string='Completed')
