from django.db import models
from adminsortable.models import Sortable
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail import ImageField


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-managed "created" and
    "modified" fields, borrowed from django_extensions.
    """
    created = models.DateTimeField(_('created'), auto_now_add=True)
    modified = models.DateTimeField(_('modified'), auto_now=True)

    class Meta:
        abstract = True


class ProjectGroup(Sortable):
    title = models.CharField(max_length=1024)
    uri = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Project(Sortable, TimeStampedModel):
    uri = models.SlugField(unique=True)
    title = models.CharField(max_length=1024)
    url = models.URLField(blank=True)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=False)
    group = models.ForeignKey(to=ProjectGroup, related_name='projects')

    def __str__(self):
        return self.title

    def get_main_image(self):
        images = self.images.all()
        try:
            return images[0]
        except IndexError:
            return None


class ProjectImage(Sortable):
    project = models.ForeignKey(to=Project, related_name='images')

    title = models.CharField(_('title'), max_length=255, blank=True)
    image = ImageField(upload_to='portfolio/images')
