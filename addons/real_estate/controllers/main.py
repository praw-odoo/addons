from odoo import http
from odoo.http import request

class RealEstate(http.Controller):
    
    @http.route('/hello',auth="public")
    def hello(self, **kw):
        return "hello world"

    @http.route('/hello_user', auth='user')
    def hello_user(self, **kw):
        return "hello %s" %(request.env.user.name)

    @http.route('/my_template', auth="public")
    def my_template(self, **kw):
        return request.render("real_estate.my_template", {})

    @http.route('/my_template_user', auth="user")
    def my_template_user(self, **kw):
        return request.render("real_estate.my_template_user", {
            'name' : request.env.user.name
        })