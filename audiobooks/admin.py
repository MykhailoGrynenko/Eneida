from django.contrib import admin

from .models import Category
from .models import Audiobook
# from .models import Video
dicti = {'а':'a','б':'b','в':'v','г':'h','д':'d','е':'e','є':'ie',
      'ж':'zh','з':'z','и':'y','ї':'i','й':'i','к':'k','л':'l','м':'m','н':'n',
      'о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'kh',
      'ц':'ts','ч':'ch','ш':'sh','щ':'shch','ъ':'','ы':'y','ь':'','э':'e',
      'ю':'iu','я':'ia', 'А':'A','Б':'B','В':'V','Г':'H','Д':'D','Е':'E','Є':'Ye',
      'Ж':'ZH','З':'Z','И':'Y','Ї':'Yi','Й':'Y','К':'K','Л':'L','М':'M','Н':'N',
      'О':'O','П':'P','Р':'R','С':'S','Т':'T','У':'U','Ф':'F','Х':'Kh',
      'Ц':'Ts','Ч':'Ch','Ш':'Sh','Щ':'Shch','Ъ':'','Ы':'y','Ь':'','Э':'E',
      'Ю':'Yu','Я':'Ya',',':'','?':'',' ':'-','~':'','!':'','@':'','#':'',
      '$':'','%':'','^':'','&':'','*':'','(':'',')':'','-':'','=':'','+':'',
      ':':'',';':'','<':'','>':'','\'':'','"':'','\\':'','/':'','№':'',
      '[':'',']':'','{':'','}':'','ґ':'g','Ґ':'G',
      '—':'', '0':'0', '1':'1', '2':'2', '3':'3', '4':'4', '5':'5',
        '6':'6', '7':'7', '8':'8', '9':'9'}
# admin.site.register(Category)
# admin.site.register(Audiobook)
# admin.site.register(Video)


def is_slug_unique(fixed_slug, class_model):
    return len(class_model.objects.filter(slug=fixed_slug)) == 0


# def IsUnique(fixed_slug):
#     return len(Audiobook.objects.filter(slug=fixed_slug)) == 0
#
#
# def IsUnique2(fixed_slug):
#     return len(Category.objects.filter(slug=fixed_slug)) == 0


def convert_to_slug(string):
    stri = ''
    for char in string:
        if char.lower() in "abcdefghijklmnopqrstuvwxyz":
            stri += char
        elif char in dicti:
            stri += dicti[char]
    return stri


class CatygoryAdmin(admin.ModelAdmin):
    fields = ['title', 'slug']
    # readonly_fields = ['slug']

    def save_model(self, request, obj, form, change):
        if 0 == len(obj.slug):
            obj.slug = convert_to_slug(obj.title)
            y = 0
            slug_copy = obj.slug
            while not is_slug_unique(obj.slug, Category):
                y += 1
                obj.slug = slug_copy + '-' + str(y)
        super(CatygoryAdmin, self).save_model(request, obj, form, change)


class AudiobookAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'categories', 'youtube_code', 'description', 'pub_date', 'show']

    def save_model(self, request, obj, form, change):
        if 0 == len(obj.slug):
            obj.slug = convert_to_slug(obj.title)
            y = 0
            slug_copy = obj.slug
            while not is_slug_unique(obj.slug, Audiobook):
                y += 1
                obj.slug = slug_copy + '-' + str(y)
        super(AudiobookAdmin, self).save_model(request, obj, form, change)


admin.site.register(Audiobook, AudiobookAdmin)
admin.site.register(Category, CatygoryAdmin)
