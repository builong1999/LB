from odoo import api, fields, models, _


class JiraProject(models.Model):
    _name = "jira.project"
    _description = "JIRA Project"
    _order = 'pin desc, sequence asc, create_date desc'

    pin = fields.Boolean(string='Pin')
    sequence = fields.Integer(string='Sequence')
    project_name = fields.Char(string='Name', required=True)
    project_key = fields.Char(string='Project Key')
    allowed_user_ids = fields.Many2many('res.users', string='Allowed Users')
    allowed_group_ids = fields.Many2many('res.groups', string='Allowed Groups')
