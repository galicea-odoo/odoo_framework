# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class MasterModel(models.Model):
    _name = 'demo.form.master'
    _description = 'master'


    opis = fields.Char('Opis')

    details_ids = fields.One2many('demo.form.details', 'master_id', 'Parametry')

class DetailModel(models.Model):
    _name = 'demo.form.details'
    _description = 'details'

    master_id = fields.Many2one('demo.form.master', 'Nadrzędny', ondelete='cascade', index=True)
    parametr = fields.Char('Parametry')

