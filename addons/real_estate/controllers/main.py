from odoo import http
from odoo.http import request

class RealEstate(http.Controller):
    
    @http.route('/hello',auth="public")
    def hello(self, **kw):
        return "hello world"

    @http.route('/hello_user', auth='user')
    def hello_user(self, **kw):
        return "hello %s" %(request.env.user.name)