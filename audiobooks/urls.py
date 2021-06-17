from django.urls import path
from .views import allAudiobooks, category_items, singleAudiobook, allCategories, allSeries
# from django.contrib.sitemaps.views import sitemap
# from django.conf import settings
# from django.conf.urls.static import static

# sitemaps = {
#     'Audiobooks': AudiobookSitemap,
#     'Categories': CategorySitemap
# }

urlpatterns = [
    # path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    path('categories/<slug:category_slug>', category_items, name='audiobooks-categoryOne'),
    path('categories', allCategories, name='allCategories'),
    path('Series/<slug:series_slug>', allAudiobooks, name='allAudiobooks'),
    path('<slug:slug>', singleAudiobook, name='singleAudiobook'),
    path('', allSeries, name='allSeries'),

]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
