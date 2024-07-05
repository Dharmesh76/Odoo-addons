from odoo import fields, api, models
import datetime


class SchoolStudents(models.Model):
    _name = 'school.students'
    _description = 'School Student'

    image = fields.Binary(string='Image')
    name = fields.Char(string='Name')
    date_of_birth = fields.Date(string='Date of Birth')
    age = fields.Integer(compute='_compute_age', string='Age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    street1 = fields.Char(string='Street1')
    street2 = fields.Char(string='Street2')
    city = fields.Char(string='City')
    country_id = fields.Many2one('res.country', string='Country')
    state_id = fields.Many2one('res.country.state', domain="[('country_id', '=?', country_id)]")
    zip = fields.Char(string='Zip')
    html = fields.Html(string='Html')

    @api.depends('date_of_birth')
    def _compute_age(self):
        current_year = datetime.date.today().year
        for rec in self:
            rec.age = 0
            if rec.date_of_birth:
                rec.age = current_year - rec.date_of_birth.year
