# -*- coding: utf-8 -*-
# © 2018 RWSdigital (https://www.rwsdigital.com)
#   @author Antonio Russo <antonio.r@rwsdigital.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models
from openerp.addons import decimal_precision as dp
from openerp.tools.float_utils import float_round


class ProductProduct(models.Model):
    _inherit = "product.product"

    @api.depends('stock_quant_ids', 'stock_move_ids')
    def _compute_quantities(self):
        res = self._compute_quantities_dict(self._context.get('lot_id'), self._context.get('owner_id'), self._context.get('package_id'), self._context.get('from_date'), self._context.get('to_date'))
        for product in self:
            product_qty_available = res[product.id]['qty_available']
            product.qty_available = product_qty_available
            if product_qty_available != product.qty_available_fast:
                product.write({'qty_available_fast':product_qty_available})
            product.incoming_qty = res[product.id]['incoming_qty']
            product.outgoing_qty = res[product.id]['outgoing_qty']
            product.virtual_available = res[product.id]['virtual_available']

    qty_available_fast = fields.Float(
        'Quantity On Hand (Fast Search)',
        digits=dp.get_precision('Product Unit of Measure'),
        )

class ProductTemplate(models.Model):
    _inherit = "product.template"

    def _compute_quantities(self):
        res = self._compute_quantities_dict()
        for template in self:
            product_qty_available = res[template.id]['qty_available']
            template.qty_available = product_qty_available
            if product_qty_available != template.qty_available_fast:
                template.write({'qty_available_fast':product_qty_available})
            template.virtual_available = res[template.id]['virtual_available']
            template.incoming_qty = res[template.id]['incoming_qty']
            template.outgoing_qty = res[template.id]['outgoing_qty']

    qty_available_fast = fields.Float(
        'Quantity On Hand (Fast Search)',
        digits=dp.get_precision('Product Unit of Measure'),
        )