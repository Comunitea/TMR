from odoo.tests.common import TransactionCase
from odoo import fields
from ..models.product_pricing import ProductPricelistPricing

# filepath: /home/santi/odoo/tmr_src/addons/rumar_pricing_module/models/test_product_pricing.py

class TestProductPricelistPricing(TransactionCase):

    def setUp(self):
        super(TestProductPricelistPricing, self).setUp()
        self.product = self.env['product.product'].create({'name': 'Test Product'})
        self.pricelist = self.env['product.pricelist'].create({'name': 'Test Pricelist'})
        self.pricing_model = self.env['product.pricelist.pricing']

    def test_calculate_all_prices_specific_product_pricelist(self):
        self.pricelist.write({'item_ids': [(0, 0, {'applied_on': '0_product_variant', 'product_id': self.product.id, 'fixed_price': 100.0})]})
        self.pricing_model.calculate_all_prices(product_id=self.product.id, pricelist_id=self.pricelist.id)
        pricing_record = self.pricing_model.search([('product_id', '=', self.product.id), ('pricelist_id', '=', self.pricelist.id)], limit=1)
        self.assertEqual(pricing_record.price, 100.0)

    def test_calculate_all_prices_all_products_pricelists(self):
        product2 = self.env['product.product'].create({'name': 'Test Product 2'})
        pricelist2 = self.env['product.pricelist'].create({'name': 'Test Pricelist 2'})
        self.pricelist.write({'item_ids': [(0, 0, {'applied_on': '0_product_variant', 'product_id': self.product.id, 'fixed_price': 100.0})]})
        pricelist2.write({'item_ids': [(0, 0, {'applied_on': '0_product_variant', 'product_id': product2.id, 'fixed_price': 200.0})]})
        self.pricing_model.calculate_all_prices()
        pricing_record1 = self.pricing_model.search([('product_id', '=', self.product.id), ('pricelist_id', '=', self.pricelist.id)], limit=1)
        pricing_record2 = self.pricing_model.search([('product_id', '=', product2.id), ('pricelist_id', '=', pricelist2.id)], limit=1)
        self.assertEqual(pricing_record1.price, 100.0)
        self.assertEqual(pricing_record2.price, 200.0)

    def test_price_update(self):
        self.pricelist.write({'item_ids': [(0, 0, {'applied_on': '0_product_variant', 'product_id': self.product.id, 'fixed_price': 100.0})]})
        self.pricing_model.calculate_all_prices(product_id=self.product.id, pricelist_id=self.pricelist.id)
        self.pricelist.item_ids.write({'fixed_price': 150.0})
        self.pricing_model.calculate_all_prices(product_id=self.product.id, pricelist_id=self.pricelist.id)
        pricing_record = self.pricing_model.search([('product_id', '=', self.product.id), ('pricelist_id', '=', self.pricelist.id)], limit=1)
        self.assertEqual(pricing_record.price, 150.0)
        self.assertTrue(pricing_record.changed)

    def test_create_new_price_record(self):
        self.pricelist.write({'item_ids': [(0, 0, {'applied_on': '0_product_variant', 'product_id': self.product.id, 'fixed_price': 100.0})]})
        self.pricing_model.calculate_all_prices(product_id=self.product.id, pricelist_id=self.pricelist.id)
        pricing_record = self.pricing_model.search([('product_id', '=', self.product.id), ('pricelist_id', '=', self.pricelist.id)], limit=1)
        self.assertEqual(pricing_record.price, 100.0)
        self.assertFalse(pricing_record.changed)