# -*- coding: utf-8 -*-


from odoo import http
from odoo.http import request

class Front00Controller(http.Controller):

    @http.route(['/front0', '/front0/p/<int:page>'], type='http', auth="public", website=True)
    def events(self, p=1, **param):
        Event = request.env['event.event']
        events = Event.search([])
        values = {
            'events': events,
        }
        return request.render("front0.front0", values)
