from odoo import fields, models


class ObiektTabela123(models.Model):
    _name = 'test123.tabela123'

    kolumna = fields.Char(string="opis.....")
    kolumna_obl = fields.Float(compute='wartosc')


    def wartosc(self):
       self.kolumna_obl=20