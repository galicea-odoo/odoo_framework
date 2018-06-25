# -*- coding: utf-8 -*-
from odoo import http

# class Amove(http.Controller):
#     @http.route('/amove/amove/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/amove/amove/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('amove.listing', {
#             'root': '/amove/amove',
#             'objects': http.request.env['amove.amove'].search([]),
#         })

#     @http.route('/amove/amove/objects/<model("amove.amove"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('amove.object', {
#             'object': obj
#         })