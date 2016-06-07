from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

from .menu import PostsMenu

class RecipesApp(CMSApp):
    name = _('Recipes App')
    urls = ['posts.urls']
    app_name = 'posts'
    menus = [PostsMenu, ]

apphook_pool.register(RecipesApp)
