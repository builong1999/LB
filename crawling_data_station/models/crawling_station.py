# Copyright © 2021 Novobi, LLC
# See LICENSE file for full copyright and licensing details.
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup

from odoo import api, fields, models, _


class CrawlingStation(models.Model):
    _name = "crawling.station"

    name = fields.Char(string='Name', required=True)
    domain = fields.Char(string='Domain')
    currency_id = fields.Many2one('res.currency', string='Currency')
    store_path_ids = fields.One2many('crawling.tag', 'crawling_station_id', string='Store Paths')
    product_cluster_path_ids = fields.One2many('crawling.tag', 'crawling_station_id', string='Store Paths')
    product_path_ids = fields.One2many('crawling.tag', 'crawling_station_id', string='Store Paths')
    price_path_ids = fields.One2many('crawling.tag', 'crawling_station_id', string='Store Paths')

    @api.model
    def _get_html_path(self, domain):
        suitable_domain = self.search([('domain', '=', domain)], order='write_date desc', limit=1)

        if suitable_domain:
            return {
                'store_path': self.store_path_ids.mapped_path(),
                'product_cluster_path': self.product_cluster_path_ids.mapped_path(),
                'product_path': self.store_path_ids.mapped_path(),
                'price_path': self.store_path_ids.mapped_path(),
            }
        return True

    @api.model
    def get_html_path(self, url):
        domain = urlparse(url).netloc
        paths = self._get_html_path(domain)
        return paths

    @api.model
    def _get_data(self, url):
        paths = self.get_html_path(url)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'lxml')
        if paths.get('store_path', False):
            pass

    @api.model
    def get_data(self, url):
        return self._get_data(url)