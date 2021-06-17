
from django.db import models



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


class Series(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(default='', editable=True, max_length=100, null=False, blank=True)
    categories = models.ManyToManyField(Category, blank=True)
    description = models.TextField(blank=True)  # null=True

    class Meta:
        verbose_name_plural = "series"
        ordering = ['title']

    def __str__(self):
        return self.title


class Audiobook(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)  # null=True
    youtube_code = models.CharField(max_length=20)
    slug = models.SlugField(default='', editable=True, max_length=100, null=False, blank=True)
    series = models.ForeignKey(Series, on_delete=models.CASCADE)

    # def was_published(self):
    #     return self.pub_date >= timezone.now()

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