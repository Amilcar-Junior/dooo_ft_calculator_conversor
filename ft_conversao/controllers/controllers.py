# -*- coding: utf-8 -*-
# from odoo import http


# class Custons-addons/ftConversão(http.Controller):
#     @http.route('/custons-addons/ft_conversão/custons-addons/ft_conversão', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custons-addons/ft_conversão/custons-addons/ft_conversão/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custons-addons/ft_conversão.listing', {
#             'root': '/custons-addons/ft_conversão/custons-addons/ft_conversão',
#             'objects': http.request.env['custons-addons/ft_conversão.custons-addons/ft_conversão'].search([]),
#         })

#     @http.route('/custons-addons/ft_conversão/custons-addons/ft_conversão/objects/<model("custons-addons/ft_conversão.custons-addons/ft_conversão"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custons-addons/ft_conversão.object', {
#             'object': obj
#         })
