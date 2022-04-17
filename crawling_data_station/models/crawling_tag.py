# Copyright © 2021 Novobi, LLC
# See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class CrawlingTag(models.Model):
    _name = "crawling.tag"
    _order = 'sequence'

    sequence = fields.Integer(string='Sequence')
    tag = fields.Char(string='Name', required=True)
    class_attribute = fields.Char(string='Class')
    id_attribute = fields.Char(string='ID')
    specific_attribute = fields.Char(string='Attribute')
    is_store = fields.Boolean(string='Is Store?')
    is_product_cluster = fields.Boolean(string='Is Product Cluster?')
    is_product = fields.Boolean(string='Is Product?')
    is_price = fields.Boolean(string='Is Price?')
    crawling_station_id = fields.Many2one('crawling.station', string='Crawling Station')

    def mapped_path(self):
        return self.sorted(lambda s: s.sequence).mapped(lambda r: {
            'tag': r.tag,
            'class': r.class_attribute,
            'id': r.id_attribute,
            'attribute': r.specific_attribute,
        })
