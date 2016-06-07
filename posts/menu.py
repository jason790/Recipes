from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from cms.menu_bases import CMSAttachMenu
from menus.base import Menu, NavigationNode
from menus.menu_pool import menu_pool

from .models import Post

class PostsMenu(CMSAttachMenu):
    name = _("Posts Menu") # give the menu a name, this is required.

    def get_nodes(self, request):
        """
        This method is used to build the menu tree.
        """

        nodes = []
        for post in Post.objects.all():
            # the menu tree consists of NavigationNode instances
            # Each NavigationNode takes a label as its first argument, a URL as
            # its second argument and a (for this tree) unique id as its third
            # argument.
            node = NavigationNode(
                post.title,
                reverse('show', args=(post.id, )),
                blog.id
            )
            nodes.append(node)
        return nodes

menu_pool.register_menu(PostsMenu)
