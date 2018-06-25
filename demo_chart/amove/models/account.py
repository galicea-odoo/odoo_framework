# -*- coding: utf-8 -*-

from odoo import models, api, fields

import pprint
import logging

_logger = logging.getLogger(__name__)

class AccountMove(models.Model):
    _inherit = "account.move"


    @api.multi
    def write(self, vals):
        _logger.info('move write: %s', pprint.pformat(vals))
        res = super(AccountMove, self).write(vals)

    @api.multi
    def button_cancel(self):
        _logger.info('move button_cancel: %s', pprint.pformat(self))
        super(AccountMove, self).button_cancel()



class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    @api.multi
    def write(self, vals):
        _logger.info('move line write: %s', pprint.pformat(vals))
        return super(AccountMoveLine, self).write(vals)


class AccountJournal(models.Model):
    _inherit = "account.journal"

    @api.multi
    def write(self, vals):
        _logger.info('journal write: %s', pprint.pformat(vals))
        return super(AccountJournal, self).write(vals)

    @api.model
    def create(self, vals):
        _logger.info('journal create: %s', pprint.pformat(vals))
