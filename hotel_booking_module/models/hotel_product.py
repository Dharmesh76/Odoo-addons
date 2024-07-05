from odoo import fields, api, models


class HotelProduct(models.Model):
    _name = 'hotel.product'
    _description = 'Hotel Product'
    _inherits = {'product.product': 'product_id'}

    @api.model
    def default_get(self, fields_list):
        res = super(HotelProduct, self).default_get(fields_list)
        res['currency_id'] = self.env.company.currency_id
        return res

    product_id = fields.Many2one('product.product', 'Product', required=True, ondelete='cascade')
