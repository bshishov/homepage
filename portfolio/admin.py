from django.contrib import admin
from django.forms import ModelForm
from pagedown.widgets import AdminPagedownWidget
from .models import *

from adminsortable.admin import SortableStackedInline, SortableAdmin
from sorl.thumbnail.admin import AdminImageMixin
from sorl.thumbnail import get_thumbnail


def admin_thumbnail_html(image):
    if image:
        thumbnail_format = '100x100'
        try:
            thumb = get_thumbnail(image, thumbnail_format, crop='center')

            return '<img src="%s" width="%s" height="%s"/>' \
                   % (thumb.url, thumb.width, thumb.height)
        except Exception as err:
            print(err)
    return ''


@admin.register(Project)
class AdminProject(admin.ModelAdmin):
    class AdminProjectForm(ModelForm):
        class Meta:
            fields = '__all__'
            model = Project
            widgets = {
                'description': AdminPagedownWidget,
            }

    class ProjectImageInline(AdminImageMixin, admin.TabularInline):
        model = ProjectImage
        extra = 0

    form = AdminProjectForm
    list_display = ('thumbnail', 'title', 'uri', 'group', 'created', 'active',)
    list_filter = ('active', 'group',)
    exclude = ()
    search_fields = ['title',]
    inlines = [ProjectImageInline, ]

    def thumbnail(self, obj):
        return admin_thumbnail_html(obj.get_main_image().image)

    thumbnail.allow_tags = True


@admin.register(ProjectGroup)
class AdminProjectGroup(admin.ModelAdmin):
    class AdminProjectGroupForm(ModelForm):
        class Meta:
            fields = '__all__'
            model = ProjectGroup
            widgets = {
                'description': AdminPagedownWidget,
            }

    form = AdminProjectGroupForm
    list_display = ('title', 'uri',)
    list_filter = ()
    exclude = ()
    search_fields = ['title', ]
    inlines = []


@admin.register(ProjectImage)
class AdminProjectImage(admin.ModelAdmin):
    list_display = ('thumbnail', 'title', 'image',)
    list_filter = ()
    exclude = ()
    search_fields = ['title']
    inlines = []

    def thumbnail(self, obj):
        return admin_thumbnail_html(obj.image)

    thumbnail.allow_tags = True
