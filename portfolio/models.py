from django.db import models
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail import ImageField


class Profile(models.Model):
    uri = models.SlugField(unique=True)
    full_name = models.CharField(max_length=1024)
    about = models.TextField(blank=True)
    bio = models.TextField(blank=True)
    image = ImageField(upload_to='portfolio/images/profile')

    def __str__(self):
        return self.full_name


class ProfileContactManager(models.Manager):
    def visible(self):
        return self.get_queryset().filter(visible=True)


class ProfileContact(models.Model):
    objects = ProfileContactManager()

    profile = models.ForeignKey(to=Profile, related_name='contact')
    caption = models.CharField(max_length=256)
    link = models.CharField(max_length=1024, blank=True)
    icon = models.CharField(max_length=256)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    visible = models.BooleanField(default=True)

    class Meta(object):
        ordering = ('order',)

    @property
    def verbose(self):
        url = self.link
        url = url.replace('http://', '')
        url = url.replace('https://', '')
        url = url.replace('mailto:', '')
        return url


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-managed "created" and
    "modified" fields, borrowed from django_extensions.
    """
    created = models.DateTimeField(_('created'), auto_now_add=True)
    modified = models.DateTimeField(_('modified'), auto_now=True)

    class Meta:
        abstract = True


class Tag(models.Model):
    name = models.CharField(max_length=100)


class ProjectGroup(models.Model):
    title = models.CharField(max_length=1024)
    uri = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ('order',)

    def __str__(self):
        return self.title


class ProjectManager(models.Manager):
    def active(self):
        return self.get_queryset().filter(active=True)


class Project(TimeStampedModel):
    objects = ProjectManager()

    uri = models.SlugField(unique=True)
    title = models.CharField(max_length=1024)
    url = models.URLField(blank=True)
    short_description = models.CharField(max_length=1024, blank=True)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=False)
    group = models.ForeignKey(to=ProjectGroup, related_name='projects')
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    tags = models.ManyToManyField(Tag, blank=True, related_name='projects')

    class Meta(object):
        ordering = ('order',)

    def __str__(self):
        return self.title

    def get_main_image(self):
        images = self.images.all()
        try:
            return images[0]
        except IndexError:
            return None

    @property
    def main_image(self):
        return self.get_main_image()


class ProjectImage(models.Model):
    project = models.ForeignKey(to=Project, related_name='images')

    title = models.CharField(_('title'), max_length=255, blank=True)
    image = ImageField(upload_to='portfolio/images')
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ('order',)


class ArticleManager(models.Manager):
    def active(self):
        return self.get_queryset().filter(active=True)


class ArticleCategory(models.Model):
    uri = models.SlugField(unique=True)
    title = models.CharField(_('title'), max_length=255, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Article(TimeStampedModel):
    objects = ArticleManager()

    uri = models.SlugField(unique=True)
    title = models.CharField(_('title'), max_length=255, blank=True)
    group = models.ForeignKey(to=ProjectGroup, related_name='articles', blank=True, null=True)
    categories = models.ManyToManyField(ArticleCategory, blank=True, related_name='articles')
    cut = models.TextField(blank=True)
    text = models.TextField(blank=True)
    active = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True, related_name='articles')

    class Meta(object):
        ordering = ('-created',)


class ArticleAttachmentManager(models.Manager):
    def visible(self):
        return self.get_queryset().filter(visible=True)


class ArticleAttachment(models.Model):
    objects = ArticleAttachmentManager()

    project = models.ForeignKey(to=Article, related_name='attachments')
    title = models.CharField(_('title'), max_length=255, blank=True)
    file = models.FileField(upload_to='portfolio/blog/files')
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    visible = models.BooleanField(default=False)

    class Meta(object):
        ordering = ('order',)


