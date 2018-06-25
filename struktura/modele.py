from odoo import fields, models


class DemoModel1(models.Model):
    _name = 'demo1.model'

    pole1 = fields.Char(string="Pierwsze pole")

class DemoModel2(models.Model):
    _inherit = 'demo1.model'

    pole2 = fields.Char(string="Pole dodane")
