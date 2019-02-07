from django.contrib.sitemaps import Sitemap
from .models import Drug, Liquor


class DrugSitemap(Sitemap):

    changefreq = 'always'

    def items(self):
        return Drug.objects.all()


class LiquorSitemap(Sitemap):

    changefreq = 'always'

    def items(self):
        return Liquor.objects.all()


class ListSitemap(Sitemap):

    changefreq = 'always'

    def items(self):
        return ['seo_list']

    def location(self, item):
        return reversed(item)