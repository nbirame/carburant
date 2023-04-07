# -*- coding: utf-8 -*-
# from odoo import http


# class Caburant(http.Controller):
#     @http.route('/caburant/caburant', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/caburant/caburant/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('caburant.listing', {
#             'root': '/caburant/caburant',
#             'objects': http.request.env['caburant.caburant'].search([]),
#         })

#     @http.route('/caburant/caburant/objects/<model("caburant.caburant"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('caburant.object', {
#             'object': obj
#         })
