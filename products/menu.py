from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from cms.menu_bases import CMSAttachMenu
from menus.base import Menu, NavigationNode
from menus.menu_pool import menu_pool

from .models import Product

class ProductsMenu(CMSAttachMenu):
    name = _('Products Menu')

    def get_nodes(self, request):
        """
        This methos builds the menu tree
        """

        nodes = []

        return nodes

menu_pool.register_menu(ProductsMenu)
