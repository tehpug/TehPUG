from django.contrib.sitemaps import GenericSitemap

from news.models import News
from faq.models import FAQ
from page.models import FirstPage

news = {
    'queryset': News.objects.all(),
    'date_field': 'date',
}

faq = {
    'queryset': FAQ.objects.all(),
    'date_field': 'date',
}

first_page = {
    'queryset': FirstPage.objects.all(),
    'date_field': 'date',
}

sitemaps = {
    'first_page': GenericSitemap(first_page, priority=0.9),
    'news': GenericSitemap(news, priority=0.7),
    'faq': GenericSitemap(faq, priority=0.5),
}
