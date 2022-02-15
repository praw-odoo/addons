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

    @http.route('/qweb_directives')
    def qweb_directives(self, **kw):
        propertys = request.env['estate.property'].search([])
        request.render("real_estate.qweb_template_example", {
            'propertys' : propertys,
            'colors' : {
                0 : 'green',
                1 : 'blue',
                2 : 'red',
                3 : 'yellow'
            }
        })