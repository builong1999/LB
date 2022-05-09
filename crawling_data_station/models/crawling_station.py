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
    product_cluster_path_ids = fields.One2many('crawling.tag', 'crawling_station_id', string='Product Cluster Paths')
    product_path_ids = fields.One2many('crawling.tag', 'crawling_station_id', string='Product Name Paths')
    price_path_ids = fields.One2many('crawling.tag', 'crawling_station_id', string='Price Paths')

    @api.model
    def _get_html_path(self, domain):
        suitable_domain = self.search([('domain', '=', domain)], order='write_date desc', limit=1)

        if suitable_domain:
            return {
                'store_path': suitable_domain.store_path_ids.filtered(lambda r: r.is_store).mapped_path(),
                'product_cluster_path': suitable_domain.product_cluster_path_ids.filtered(
                    lambda r: r.is_product_cluster).mapped_path(),
                'product_path': suitable_domain.store_path_ids.filtered(lambda r: r.is_product).mapped_path(),
                'price_path': suitable_domain.store_path_ids.filtered(lambda r: r.is_price).mapped_path(),
            }
        return True

    @api.model
    def get_html_path(self, url):
        domain = urlparse(url).netloc
        paths = self._get_html_path(domain)
        return paths

    def _get_store_name(self, soup, paths):
        store_path_tags = paths['store_path']
        store_clusters = []
        for cluster in store_path_tags:
            clusters = soup.find_all(cluster['tag'], cluster)
            store_clusters.append(clusters.getText())
        return store_clusters

    def _get_product_and_price(self, soup, paths):
        product_cluster_tags = paths['product_cluster_path']
        product_tags = paths['product_path']
        price_tags = paths['price_path']

        product_clusters = []
        product_and_price = []

        for cluster in product_cluster_tags:
            clusters = soup.findAll(cluster.tag, cluster)
            product_clusters.extend(clusters)

        return False

    @api.model
    def _get_data(self, url):
        paths = self.get_html_path(url)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        if paths.get('store_path', False):
            store_name = self._get_store_name(soup, paths)
        if paths.get('product_cluster_path', False) \
                and paths.get('product_path', False) \
                and paths.get('price_path', False):
            products = self._get_product_and_price(soup, paths)

    @api.model
    def get_data(self, url):
        return self._get_data(url)
