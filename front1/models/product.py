# -*- coding: utf-8 -*-

from odoo import fields, models


# powiązanie produtów z biletami
class Product(models.Model):
    _inherit = 'product.product'

    event_ticket_ids = fields.One2many('event.event.ticket', 'product_id', string='Event Tickets')
