# -*- coding: utf-8 -*-


from odoo import models, fields, api, SUPERUSER_ID
from odoo.tools.translate import _
import logging

_logger = logging.getLogger(__name__)

class Demo1Model(models.Model):
    _name = 'demo.demo1ex'

    name = fields.Char('Nazwa z demo1ex', required=True)
    link_dem2ex = fields.Many2one(comodel_name='demo.demo2ex', string='Dla relacji one2many')

class Demo1Model(models.Model):
    _name = 'demo.demo2ex'

    name = fields.Char('Nazwa 2', required=True)
    pole_one2many = fields.One2many(comodel_name='demo.demo1ex', inverse_name = 'link_dem2ex', 
                    string='Pole one2many (zbior rekordow z demo1ex)', copy=True)
    pole_many2one = fields.Many2one(comodel_name='demo.demo1ex', 
                    string='Many2one - moze wskazywac na 1 rekord z demo1ex')
    pole_many2many = fields.Many2many(comodel_name='demo.demo1ex', 
                    string='many2many - relacje miedzy tabelami')
    pole_many2many_r = fields.Many2many(comodel_name='demo.demo1ex', relation='deno1demo2ex', 
                    string='many2many nazwane')
