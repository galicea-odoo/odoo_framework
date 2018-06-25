from odoo import fields, models, api,_
from odoo.exceptions import ValidationError, Warning
import logging

_logger = logging.getLogger(__name__)


class Dekoratory(models.Model):
    _name = 'test123.tabela123'

    kolumna = fields.Char(string="opis.....")
    wartosc = fields.Float(string="wartosc...")
    tysiace = fields.Float(string="w tysiacach",compute='compute_tys')

    @api.depends('wartosc')
    def compute_tys(self):
      self.tysiace = float(self.wartosc) / 1000

    cena = fields.Float('Cena')
    upust = fields.Float('Upust')

# <field name="cena" on_change="on_change_cena0(cena,upust)"/>
# <field name="upust" on_change="on_change_cena0(cena,upust)"/>
# bez dekoratora:
    def on_change_cena0(self,cena,upust):
      total = cena - upust
      res = {
              'value': {
              'wartosc': total
              }
            }
      return res

    wartosc1 = fields.Float(string="wartosc1")
    cena1 = fields.Float(string='Cena1')
    upust1 = fields.Float(string='Upust1')

# z dekoratorem (nie potrzebne on_change w XML)
    @api.onchange('cena1','upust1')
    def on_change_cena(self):
      if self.cena1<self.upust1:
        return {
        'warning': {
           'title': _('Warning!'),
           'message': _('Price must be > discount'),
           },
        }
      self.wartosc1 = self.cena1 - self.upust1

    cena2 = fields.Float(string='Cena2')

    @api.multi
    @api.constrains('cena2')
    def _on_cena_nieujemna(self):
#        self.ensure_one()
      _logger.warning('Cena  =  (%s).' % self.cena2)
      for item in self:
        if item.cena2<0.0:
          raise Warning(_('Error! Price must be >0.'))
        
  