import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)

class ProductPricelistPricing(models.Model):
    _name = 'product.pricelist.pricing'
    _description = 'Product Pricelist Pricing'

    product_id = fields.Many2one('product.product', string='Product', required=True)
    price = fields.Float(string='Price', required=True)
    pricelist_id = fields.Many2one('product.pricelist', string='Pricelist', required=True)
    modification_date = fields.Datetime(string='Modification Date')
    changed = fields.Boolean(string='Modified', default=False)

    @api.model
    def calculate_all_prices(self, product_id=None, pricelist_id=None):
        _logger.info('Starting price calculation for products and pricelists.')

        if product_id:
            products = self.env['product.product'].browse([product_id])
        else:
            products = self.env['product.product'].search([])

        if pricelist_id:
            pricelists = self.env['product.pricelist'].browse([pricelist_id])
        else:
            pricelists = self.env['product.pricelist'].search([])

        for product in products:
            for pricelist in pricelists:
                price = pricelist.get_product_price(product, 1.0, False)
                existing_record = self.search([('product_id', '=', product.id), ('pricelist_id', '=', pricelist.id)], limit=1)
                if price != 0:
                    if existing_record:
                        if existing_record.price != price:
                            _logger.info(f'Updating price for product {product.id} in pricelist {pricelist.id} from {existing_record.price} to {price}.')
                            existing_record.write({
                                'price': price,
                                'modification_date': fields.Datetime.now(),
                                'changed': True
                            })
                    else:
                        _logger.info(f'Creating new price record for product {product.id} in pricelist {pricelist.id} with price {price}.')
                        self.create({
                            'product_id': product.id,
                            'price': price,
                            'pricelist_id': pricelist.id,
                            'modification_date': fields.Datetime.now(),
                            'changed': True
                        })
        _logger.info('Finished price calculation for products and pricelists.')
