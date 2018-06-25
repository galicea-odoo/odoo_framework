# -*- coding: utf-8 -*-



from odoo import http, _
# zob. addons/website_event/controllers/main.py
from odoo.addons.website_event.controllers.main import WebsiteEventController
from odoo.http import request


class WebsiteEventFront4Controller(WebsiteEventController):

    @http.route(['/front4',], type='http', auth="public", website=True)
    def front4(self, **param):
        Event = request.env['event.event']
        events = Event.search([])
        values = {
            'events': events,
        }
        return request.render("front4.front0", values)



    @http.route(['/front4_modal'], type='json', auth="public", methods=['POST'], website=True)
    def front4_modal(self, **post):
        return request.env['ir.ui.view'].render_template("front4.modal_form", {})
