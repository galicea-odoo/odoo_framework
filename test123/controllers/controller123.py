# -*- coding: utf-8 -*-
import logging
import traceback

from odoo import SUPERUSER_ID
from odoo import http
from odoo.http import request
import werkzeug

_logger = logging.getLogger(__name__)



class controler123(http.Controller):


    @http.route('/test123/test1', type='http', auth='public')
    def test(self, **kw):
        return werkzeug.utils.redirect('/', 301)

    @http.route('/test123/test2', type='http', auth='none')
    def test2(self):
        result = '<html><body><table><tr><td>'
        result += '</td></tr><tr><td>aaaaaaaaaaaaaaa'
        result += '</td></tr></table></body></html>'
        return result


    @http.route('/test123/test3', type='http', auth="public", website=True)
    def test3(self):
        return request.render(
            'test123.test123t'
#            ,
#            {
#                'par': 'wartość',
#            }
            )


    @http.route('/test123/test4',auth='public', website=True)
    def test4(self,**kw):
        return http.request.render(
                    'test123.test123t')
