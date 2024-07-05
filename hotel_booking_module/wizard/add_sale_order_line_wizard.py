from odoo import models, api, fields


class OrderLineWizard(models.TransientModel):
    _name = 'order.line.wizard'
    _description = 'Order Line Wizard'

    @api.model
    def default_get(self, fields_list):
        res = super(OrderLineWizard, self).default_get(fields_list)
        res['currency_id'] = self.env.company.currency_id.id
        print(self.env.company.currency_id)
        return res

    product_id = fields.Many2one('hotel.product', 'Product')
    product_qty = fields.Float(string='Quantity')
    price_unit = fields.Float(related='product_id.list_price', string='Price')
    tax_ids = fields.Many2many('account.tax', 'wizard_product_account_tax_rel',
                               'wizard_rec_id',
                               'tax_id')
    currency_id = fields.Many2one('res.currency')
    subtotal = fields.Monetary(string='Subtotal', compute='_compute_price_subtotal')

    @api.depends('product_qty', 'tax_ids', 'price_unit')
    def _compute_price_subtotal(self):
        for rec in self:
            rec.subtotal = 0
            rec.subtotal = rec.price_unit * rec.product_qty

    def action_add_line(self):
        booking_id = self.env['hotel.booking'].browse(self.env.context.get('active_id'))
        booking_id.product_line_ids.create({
            'product_id': self.product_id.id,
            'product_qty': self.product_qty,
            'booking_id': booking_id.id,
            'price_unit': self.price_unit,
            'tax_ids': self.tax_ids,
            'subtotal': self.subtotal
        })
        self.env['sale.order.line'].sudo().create({
            'order_id': booking_id.sale_order_id.id,
            'product_template_id': self.product_id.product_id.product_tmpl_id.id,
            'product_id': self.product_id.product_id.id,
            'name': self.product_id.name,
            'product_uom_qty': self.product_qty,
            'price_unit': self.price_unit,
            'tax_id': self.tax_ids,
            'product_uom': self.product_id.uom_id.id
        })



