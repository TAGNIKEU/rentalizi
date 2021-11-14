# -*- coding: utf-8 -*-
from odoo import http

# class Rentalizi(http.Controller):
#     @http.route('/rentalizi/rentalizi/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rentalizi/rentalizi/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rentalizi.listing', {
#             'root': '/rentalizi/rentalizi',
#             'objects': http.request.env['rentalizi.rentalizi'].search([]),
#         })

#     @http.route('/rentalizi/rentalizi/objects/<model("rentalizi.rentalizi"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rentalizi.object', {
#             'object': obj
#         })