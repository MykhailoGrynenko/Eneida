from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.template import loader
from .models import Category, Audiobook
from django.http import HttpResponse, JsonResponse
from django.views.generic import DetailView


def allAudiobooks(request):
    audiobooks_list = Audiobook.objects.all()
    # paginator = Paginator(audiobooks_list, 2)
    # page = request.GET.get('page')
    # try:
    #     page_obj = paginator.page(page)
    # except PageNotAnInteger:
    #     page_obj = paginator.page(1)
    # except EmptyPage:
    #     page_obj = paginator.page(paginator.num_pages)
    context = {
        'Category': Category.objects.all(),
        'Audiobook': pagination(request, audiobooks_list)
    }
    return render(request, 'allAudiobooks.html', context)

  #  audios = Audiobook.objects.filter(categories__id=category_id)

def allCategories(request):
    categories_list = Category.objects.all()
    # paginator = Paginator(categories_list, 2)
    # page = request.GET.get('page')
    # try:
    #     page_obj = paginator.page(page)
    # except PageNotAnInteger:
    #     page_obj = paginator.page(1)
    # except EmptyPage:
    #     page_obj = paginator.page(paginator.num_pages)
    context = {
        # 'Audiobook': Audiobook.objects.all(),
        'Category': pagination(request, categories_list),
    }
    return render(request, 'allCategories1.html', context)


def pagination(request, pagination_list, items_on_page=2):
    paginator = Paginator(pagination_list, items_on_page)
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return page_obj


def category_items(request, category_slug):
    audiobooks_list = Audiobook.objects.filter(categories__slug=category_slug)
    # paginator = Paginator(audiobooks_list, 2)
    # page = request.GET.get('page')
    # try:
    #     page_obj = paginator.page(page)
    # except PageNotAnInteger:
    #     page_obj = paginator.page(1)
    # except EmptyPage:
    #     page_obj = paginator.page(paginator.num_pages)
    context = {
        'Audiobook': pagination(request, audiobooks_list),
        'Category': Category.objects.all()
    }
    return render(request, 'allAudiobooks.html', context)


def singleAudiobook(request, slug):
    context = {
        'Audiobook': Audiobook.objects.filter(slug=slug),
        'Category': Category.objects.all()
    }
    return render(request, 'singleAudiobook.html', context)


#def index(request):
 #   template = loader.get_template('audiobooks/index.html')
    #return HttpResponse("Hello, world. You're at the audiobooks index.")
    #return HttpResponse(template.render(request))
  #  return HttpResponse(template.render({}, request))

#def index(request):
#    template = loader.get_template('audiobooks/index.html')
    #return HttpResponse("Hello, world. You're at the audiobooks index.")
    #return HttpResponse(template.render(request))
#    return JsonResponse(template.render({}, request))

#def index2(request):
 #   return JsonResponse({'status': 'ok'})