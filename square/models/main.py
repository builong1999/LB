
from odoo import api, fields, models, _
from odoo.osv import expression
from odoo.exceptions import UserError, ValidationError


class SquareLog(models.Model):
    _name = "square.log"
    _description = "Square Logs"
    
    name = fields.Date(string='Name')
    body = fields.Text(string='Body')
