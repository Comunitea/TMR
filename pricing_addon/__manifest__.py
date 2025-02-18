{
    'name': 'Pricing Module',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Module to calculate and store product prices for each pricelist',
    'description': """
        This module calculates the prices of all products for each pricelist and stores them in a table, recording any modifications and the date of those modifications.
    """,
    'depends': ['product', 'sale'],
    'data': [
        'data/ir_cron.xml',
        'views/product_pricing_views.xml',
        'views/product_template_views.xml',
    ],
    'installable': True,
    'application': False,
}
