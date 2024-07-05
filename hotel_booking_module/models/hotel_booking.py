from odoo import fields, api, models, _
from odoo.exceptions import ValidationError


class HotelBooking(models.Model):
    _name = 'hotel.booking'
    _description = 'Hotel Booking'
    _rec_name = 'booking_ref'

    @api.model
    def default_get(self, fields_list):
        res = super(HotelBooking, self).default_get(fields_list)
        res['user_id'] = self.env.uid
        # res['currency_id'] = self.env.company.currency_id
        return res

    booking_ref = fields.Char(default='New')
    partner_id = fields.Many2one('res.partner', string='Customer')
    date = fields.Date(string='Date', default=fields.date.today())
    checkin_date_time = fields.Datetime(string='Checkin')
    checkout_date_time = fields.Datetime(string='Checkout')
    sale_order_id = fields.Many2one('sale.order', 'Sale Order')
    user_id = fields.Many2one('res.users', string='Responsible')
    product_line_ids = fields.One2many('product.line', 'booking_id')

    currency_id = fields.Many2one('res.currency')
    untaxed_amount = fields.Monetary(string='Total Untaxed Amount', compute='_compute_untaxed_amount')
    taxed_amount = fields.Monetary(string='Total Tax Amount', compute='_compute_taxed_amount')
    total_amount = fields.Monetary(string='Total Amount', compute='_compute_total_amount')
    is_sale_order_created = fields.Boolean(default=False)

    @api.model_create_multi
    def create(self, vals_list):
        for rec in vals_list:
            rec['booking_ref'] = self.env['ir.sequence'].next_by_code('hotel.booking.sequence')
        return super(HotelBooking, self).create(vals_list)

    @api.depends('product_line_ids')
    def _compute_untaxed_amount(self):
        self.untaxed_amount = 0
        for rec in self.product_line_ids:
            self.untaxed_amount += rec.subtotal

    @api.depends('product_line_ids')
    def _compute_taxed_amount(self):
        self.taxed_amount = 0
        for rec in self.product_line_ids:
            tax_per = 0
            for tax in rec.tax_ids:
                tax_per += tax.amount
            if tax_per:
                self.taxed_amount += rec.subtotal * tax_per / 100

    @api.depends('product_line_ids')
    def _compute_total_amount(self):
        self.total_amount = self.untaxed_amount + self.taxed_amount

    def action_create_sale_order(self):
        if not self.product_line_ids:
            raise ValidationError(_('Please Select Product Line'))

        # create sale order
        sale_order = self.env['sale.order'].sudo().create({
            'partner_id': self.partner_id.id,
            'booking_ref': self.id
        })
        # creating order lines
        for rec in self.product_line_ids:
            product_exists = self.env['sale.order.line'].sudo().search([('order_id', '=', sale_order.id), ('product_id', '=', rec.product_id.product_id.id)]).exist()
            print(product_exists)
            if product_exists:
                print('available')
            else:
                self.env['sale.order.line'].sudo().create({
                    'order_id': sale_order.id,
                    'product_template_id': rec.product_id.product_id.product_tmpl_id.id,
                    'product_id': rec.product_id.product_id.id,
                    'name': rec.product_id.name,
                    'product_uom_qty': rec.product_qty,
                    'price_unit': rec.price_unit,
                    'tax_id': rec.tax_ids,
                    'product_uom': rec.product_id.uom_id.id

            })

        self.is_sale_order_created = True
        self.sale_order_id = sale_order.id
        return {
            'type': 'ir.actions.act_window',
            'name': 'Sale Order',
            'res_model': 'sale.order',
            'view_mode': 'form',
            'res_id': sale_order.id,
        }
