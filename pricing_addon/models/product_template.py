import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    pricing_count = fields.Integer(string='Pricing Count', compute='_compute_pricing_count')

    def _compute_pricing_count(self):
        for template in self:
            template.pricing_count = self.env['product.pricelist.pricing'].search_count([('product_id.product_tmpl_id', '=', template.id)])

    def action_view_pricing(self):
        self.ensure_one()
        action = self.env.ref('rumar_pricing_module.action_product_pricing').read()[0]
        action['domain'] = [('product_id.product_tmpl_id', '=', self.id)]
        return action

    def action_calculate_pricing(self):
        self.ensure_one()
        for variant in self.product_variant_ids:
            self.env['product.pricelist.pricing'].calculate_all_prices(product_id=variant.id)
        return self.action_view_pricing()
