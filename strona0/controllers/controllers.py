# -*- coding: utf-8 -*-
from odoo import http

class Stroniczka(http.Controller):

  @http.route('/stroniczka',auth='public', website=True)
  def index(self,**kw):
    return http.request.render('strona0.strona0')