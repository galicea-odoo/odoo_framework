# -*- coding: utf-8 -*-
from odoo import http

# class DemoAct(http.Controller):
#     @http.route('/demo_act/demo_act/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/demo_act/demo_act/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('demo_act.listing', {
#             'root': '/demo_act/demo_act',
#             'objects': http.request.env['demo_act.demo_act'].search([]),
#         })

#     @http.route('/demo_act/demo_act/objects/<model("demo_act.demo_act"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('demo_act.object', {
#             'object': obj
#         })