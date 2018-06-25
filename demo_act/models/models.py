# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)


class Demo(models.Model):
    _name = "demo.act"

    @api.multi
    def otworz_partnera(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'res.partner',
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new',
        }
    

    @api.model
    def akcja_cron(self):
      _logger.exception("Wywolano akcje Crona - nie zaimplementowane!")
