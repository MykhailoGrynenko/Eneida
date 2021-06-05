
from django.db import models
from django.utils import timezone
# from PIL import Image


class Category(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(default='', editable=True, max_length=100, null=False, blank=True)

    class Meta:
        verbose_name_plural = "categories"
        ordering = ['title']

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     from django.urls import reverse
    #     return reverse('audiobooks-categoryOne', args=[str(self.slug)])


class Audiobook(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)  # null=True
    youtube_code = models.CharField(max_length=20)
    # video_url = models.URLField(max_length=200, blank=True)
    # image = models.ImageField(default='default.jpg', upload_to='audiobook_pics')
    categories = models.ManyToManyField(Category, blank=True)
    pub_date = models.DateTimeField('date created')
    slug = models.SlugField(default='', editable=True, max_length=100, null=False, blank=True)
    show = models.BooleanField(default=True, null=True)

    def was_published(self):
        return self.pub_date >= timezone.now()

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     from django.urls import reverse
    #     return reverse('singleAudiobook', args=[str(self.slug)])

    # def save(self):
    #     super().save()
    #
    #     img = Image.open(self.image.path)
    #
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)