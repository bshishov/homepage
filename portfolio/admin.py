from django.contrib import admin
from django.forms import ModelForm
from pagedown.widgets import AdminPagedownWidget
from .models import *

from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminMixin
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
class AdminProject(SortableAdminMixin, admin.ModelAdmin):
    class AdminProjectSmallForm(ModelForm):
        class Meta:
            fields = ('title',)
            model = Project

    class AdminProjectForm(ModelForm):
        class Meta:
            fields = '__all__'
            model = Project
            widgets = {
                'description': AdminPagedownWidget,
            }

    class ProjectImageInline(SortableInlineAdminMixin, AdminImageMixin, admin.TabularInline):
        model = ProjectImage
        extra = 0

    form = AdminProjectForm
    list_display = ('thumbnail', 'title', 'uri', 'group', 'created', 'active',)
    list_filter = ('active', 'group',)
    exclude = ()
    search_fields = ['title',]
    inlines = [ProjectImageInline, ]

    def thumbnail(self, obj):
        main_image = obj.get_main_image()
        if main_image:
            return admin_thumbnail_html(main_image.image)
        return None

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

    class ProjectInline(SortableInlineAdminMixin, admin.TabularInline):
        model = Project
        extra = 0
        form = AdminProject.AdminProjectSmallForm
        readonly_fields = ('title',)

    form = AdminProjectGroupForm
    list_display = ('title', 'uri',)
    list_filter = ()
    exclude = ()
    search_fields = ['title', ]
    inlines = [ProjectInline,]


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


@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    class AdminProfileForm(ModelForm):
        class Meta:
            fields = '__all__'
            model = Project
            widgets = {
                'about': AdminPagedownWidget,
                'bio': AdminPagedownWidget,
            }

    class ProfileContactInline(SortableInlineAdminMixin, admin.TabularInline):
        model = ProfileContact
        extra = 0

    form = AdminProfileForm
    inlines = [ProfileContactInline, ]
