from odoo import api, fields, models, _


class JiraProject(models.Model):
    _name = "jira.project"
    _description = "JIRA Project"
    _order = 'pin desc, sequence asc, create_date desc'

    pin = fields.Boolean(string='Pin')
    sequence = fields.Integer(string='Sequence')
    ticket_name = fields.Char(string='Name', required=True)
    ticket_key = fields.Char(string='Project Key')
    ticket_url = fields.Char(string='JIRA Ticket')
    time_log_ids = fields.One2many('jira.time.log', 'ticket_id', string='Log Times')
    start_time = fields.Datetime(string='Start Time')
    story_point = fields.Integer(string='Story Point')

