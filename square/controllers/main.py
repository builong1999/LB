
from odoo import http
from odoo.http import request


class OnboardingController(http.Controller):

    @http.route(['/square/logs'], type='json', cors="*", method=["GET", "POST"],  auth="public")
    def log_square(self, **kwargs):
        print(kwargs)
        print(request.params)
        return {
            "status": 200
        }