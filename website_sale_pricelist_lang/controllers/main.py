# -*- coding: utf-8 -*-
from openerp.http import request
from openerp.addons.website_sale.controllers.main import website_sale, QueryURL
import logging
_logger = logging.getLogger(__name__)



class WebsiteSalePriceList(website_sale):

    def get_pricelist(self):
        return request.env.user.sudo().partner_id.property_product_pricelist

