from django.db import models
from taggit.managers import TaggableManager


class Datum(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True


class Anime(Datum):
    title  = models.CharField(max_length=384, unique=True)
    year   = models.PositiveIntegerField()
    rating = models.CharField(max_length=3)
    genres = TaggableManager()
    banned = models.BooleanField(default=False)
    ban_reason = models.TextField(default="Доступен к просмотру", blank=True)
    bypass_method = models.TextField(default="Доступен к просмотру", null=True)

    def __str__(self):
        return "{} ({}г) [{}]".format(self.title, self.year, self.rating)

    def get_row_css_class(self):
        if self.banned:
            return "blocked-anime"
        else:
            return "open-anime"


class Announcement(Datum):
    content = models.TextField()
    styles = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.content

    def safe_content(self):
        if self.styles:
            return '<div class="shadow-sm alert text-center fw-900 text-uppercase" style="{}">{}</div>'.format(self.styles, self.content)
        else:
            return '<div class="shadow-sm alert osekter-brown text-center text-white fw-900 text-uppercase">{}</div>'.format(self.content)


class Suggestion(Datum):
    title = models.CharField(max_length=384, unique=True)
    animelink = models.URLField(max_length=512)
    client_ip = models.CharField(max_length=32)

    def __str__(self):
        return self.title