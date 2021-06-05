from django.urls import path
# from . import views
from .views import allAudiobooks, category_items, singleAudiobook, allCategories
# from .sitemaps import AudiobookSitemap, CategorySitemap
# from django.contrib.sitemaps.views import sitemap
# from django.conf import settings
# from django.conf.urls.static import static

# sitemaps = {
#     'Audiobooks': AudiobookSitemap,
#     'Categories': CategorySitemap
# }

urlpatterns = [
    # path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('', allAudiobooks, name='allAudiobooks'),
    #path('categories/<slug:slug>', views.category_items, name='audiobooks-categoryOne'),
    #path('<slug:slug>', views.category_items, name='audiobooks-categoryOne'),
    path('categories', allCategories, name='allCategories'),
    path('categories/<slug:category_slug>', category_items, name='audiobooks-categoryOne'),
    path('<slug:slug>', singleAudiobook, name='singleAudiobook'),


 #   path('audiobook/>', views.category_items, name='audiobooks-categoryOne'),
   # path('categoryTwo/', views.categoryTwo, name='categoryTwo'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
