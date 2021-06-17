from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
# from django.template import loader
from .models import Category, Audiobook, Series
# from django.http import HttpResponse, JsonResponse
# from django.views.generic import DetailView


def pagination(request, pagination_list, items_on_page=3):
    paginator = Paginator(pagination_list, items_on_page)
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return page_obj


def allSeries(request):
    series_list = Series.objects.all()
    context = {
        'Category': Category.objects.all(),
        'Series': pagination(request, series_list)
    }
    return render(request, 'allSeries.html', context)

def allAudiobooks(request, series_slug):
    audiobooks_list = Audiobook.objects.filter(series__slug=series_slug)
    context = {
        'Category': Category.objects.all(),
        'Audiobook': audiobooks_list
        # 'Audiobook': pagination(request, audiobooks_list)
    }
    return render(request, 'allAudiobooks.html', context)

  #  audios = Audiobook.objects.filter(categories__id=category_id)

def allCategories(request):
    categories_list = Category.objects.all()
    context = {
        # 'Audiobook': Audiobook.objects.all(),
        'Category': pagination(request, categories_list),
    }
    return render(request, 'allCategories1.html', context)


def category_items(request, category_slug):
    series_list = Series.objects.filter(categories__slug=category_slug)
    context = {
        'Series': pagination(request, series_list),
        'Category': Category.objects.all()
    }
    return render(request, 'allSeries.html', context)


def singleAudiobook(request, slug):
    context = {
        'Audiobook': Audiobook.objects.filter(slug=slug),
        'Category': Category.objects.all()
    }
    return render(request, 'singleAudiobook.html', context)