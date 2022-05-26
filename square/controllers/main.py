
from odoo import http
from odoo.http import request


class OnboardingController(http.Controller):

    @http.route(['/square/logs'], type='http', auth="public")
    def log_square(self, **kwargs):
        print(kwargs)