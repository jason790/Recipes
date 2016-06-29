from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

from .menu import ProductsMenu

class ProductsApp(CMSApp):
    name = _('Products App')
    urls = ['products.urls']
    app_name = 'products'
    menus = [ProductsMenu, ]

apphook_pool.register(ProductsApp)
