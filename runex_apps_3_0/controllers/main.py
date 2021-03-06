# -*- coding: utf-8 -*-
# Copyright 2017 Sergio Teruel <sergio.teruel@tecnativa.com>
# Copyright 2017 David Vidal <david.vidal@tecnativa.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from openerp import http
from openerp.http import request
from openerp.addons.website_sale.controllers.main import website_sale


class SendQuotation(website_sale):
    """
    Class that make posible function of Confirm order btn btn-succes bottom.
    """
    # @http.route('/shop/confirm_order', type='http', auth="public", website=True)
    # def confirm_order(self, **post):
    #     """
    #     Method that put the order into the 'Quotation sent' state.
    #     """
    #     context = request.context
    #     order = request.website.sale_get_order(context=context)
    #     result = order.force_quotation_send()
    #     if result:
    #         # Clean context and session, then redirect to the confirmation page
    #         request.website.sale_reset(context=context)
    #         return request.redirect('/shop/confirmation')
    #     else:
    #         return request.redirect('/shop/confirmation')

    @http.route(['/shop/cart/update_main'], type='http', auth="public", methods=['POST'], website=True)
    def cart_update(self, product_id, add_qty=1, set_qty=0, **kw):
        cr, uid, context = request.cr, request.uid, request.context
        request.website.sale_get_order(force_create=1)._cart_update(product_id=int(product_id), add_qty=float(add_qty), set_qty=float(set_qty))
        order = request.website.sale_get_order(force_create=1)
        template = request.render('runex_add_to_cart_view.dropdown_cart', {'website_sale_order': order}).render()
        return template

class ProductController(http.Controller):
    """ The summary line for a class docstring should fit on one line.

        Routes:
          /some_url: url description
    """

    @http.route(['/shop/get_product_data'], type='json', auth="public", website=True)
    def get_desc(self, product_id, **kw):
        product_obj = request.env['product.template']
        product = product_obj.browse(product_id)
        print product.product_variant_ids[0]
        return {
            'id': product.id,
            'variant_id': product.product_variant_ids[0].id,
            'name': product.name,
            'price': product.list_price,
            'description_sale': product.description_sale,
            'number_of_variant': product.product_variant_count
            }
