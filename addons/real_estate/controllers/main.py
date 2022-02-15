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

    @http.route('/qweb_directives', auth="user")
    def qweb_directives(self, **kw):
        propertys = request.env['estate.property'].search([])
        return request.render("real_estate.qweb_template_example", {
            'propertys' : propertys,
            'colors' : {
                1 : 'green',
                2 : 'blue',
                3 : 'red',
                4 : 'yellow',
            }
        })

    @http.route('/test_tcall', auth="user")
    def test_tcall(self, **kw):
        return request.render("real_estate.test_tcall",{})

    @http.route('/web_page', auth="user", website=True)
    def web_page(self, **kw):
        propertys = request.env['estate.property'].search([])
        return request.render("real_estate.web_page", {
            'propertys' : propertys,
            'colors' : {
                1 : 'green',
                2 : 'blue',
                3 : 'red',
                4 : 'yellow',
            }
        })

    @http.route('/property_details/<model("estate.property"):property>', auth="user", website=True)
    def property_details(self, property=None, **kw):
        return request.render("real_estate.property_details", {
            'property' : property,
        })