{
    'name': 'Hotel Booking',
    'version': '17.0.0.1',
    'summery': 'Hotel Booking App',
    'description': 'Hotel Booking App',
    'application': True,
    'autoinstall': False,
    'sequence': -100,
    'depends': ['mail', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'data/booking_sequence.xml',
        'wizard/order_line_wizard_view.xml',
        'views/hotel_booking_view.xml',
        'views/hotel_product_view.xml',
        'views/extended_sale_order_view.xml',
        'views/order_line_view.xml',
        'views/menu.xml'
    ],
    'demo': [],
    'installable': True,
    'category': 'Hotel Management',
    'licence': 'LGPL-3',
}