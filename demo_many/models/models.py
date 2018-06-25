# -*- coding: utf-8 -*-

import base64
import json
import os
import subprocess
import urllib
import urlparse
import distutils
import logging

from odoo import models, fields, api, SUPERUSER_ID
from odoo.tools import config
from odoo.exceptions import AccessError, ValidationError, UserError
from odoo.tools.translate import _

import logging

_logger = logging.getLogger(__name__)



class DemoModel(models.Model):
    _name = 'demo.mdemo'

    sel = fields.Char('Wzór', default='')
    partners = fields.Many2many(   comodel_name = 'res.partner',
                                   compute='_compute_ids',
                                   string='Wybrane konta',
               )

    @api.one
    @api.depends('sel')
    def _compute_ids(self):
        values = self.env['res.partner'].search([('name','like',self.sel)])
        self.partners=values.ids
