from django.db import models


class ProjectGroup(models.Model):
    title = models.CharField(max_length=1024, blank=False)
    uri = models.SlugField(blank=False, null=False, unique=True)
    description = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.title


class Project(models.Model):
    uri = models.SlugField(blank=False, null=False, unique=True)
    title = models.CharField(max_length=1024, blank=False)
    url = models.URLField()
    description = models.TextField(blank=False, null=False)
    created = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)
    group = models.ForeignKey(to=ProjectGroup, related_name='projects')

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(to=Project, related_name='images')
    image = models.ImageField(upload_to='project_images', width_field='width', height_field='height')
