# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

import logging
_logger = logging.getLogger(__name__)

class PaymentTransacionCecaController(http.Controller):

    @http.route(['/payment_transaction/ceca/action_run'], type='http', auth='public', methods=['GET'], website=True)
    def payment_transaction_ceca_action_run(self, **post):
        _logger.info('payment_transaction_ceca_action_run (controller)')
        request.env['payment.transaction'].sudo().cron_sqs_ceca_action_run()
        return request.render('website.404')    