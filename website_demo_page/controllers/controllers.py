# -*- coding: utf-8 -*-
from odoo import http


class Example(http.Controller):
    @http.route('/example', type='http', auth='public', website='True')
    def render_example_page(self):
        return http.request.render('website_demo_page.example_page', {})

# class WebsiteDemoPage(http.Controller):
#     @http.route('/website_demo_page/website_demo_page/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_demo_page/website_demo_page/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_demo_page.listing', {
#             'root': '/website_demo_page/website_demo_page',
#             'objects': http.request.env['website_demo_page.website_demo_page'].search([]),
#         })

#     @http.route('/website_demo_page/website_demo_page/objects/<model("website_demo_page.website_demo_page"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_demo_page.object', {
#             'object': obj
#         })
