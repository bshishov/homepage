from django.contrib import admin
from django.forms import ModelForm


from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminMixin
from sorl.thumbnail.admin import AdminImageMixin
from sorl.thumbnail import get_thumbnail

from . import models


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


@admin.register(models.Project)
class AdminProject(SortableAdminMixin, admin.ModelAdmin):
    class AdminProjectSmallForm(ModelForm):
        class Meta:
            fields = ('title',)
            model = models.Project

    class AdminProjectForm(ModelForm):
        class Meta:
            fields = '__all__'
            model = models.Project
            widgets = {}

    class ProjectImageInline(SortableInlineAdminMixin, AdminImageMixin, admin.TabularInline):
        model = models.ProjectImage
        extra = 0

    form = AdminProjectForm
    list_display = ('title', 'thumbnail', 'uri', 'group', 'created', 'active',)
    list_filter = ('active', 'group',)
    exclude = ()
    search_fields = ['title', ]
    inlines = [ProjectImageInline, ]

    def thumbnail(self, obj):
        main_image = obj.get_main_image()
        if main_image:
            return admin_thumbnail_html(main_image.image)
        return None

    thumbnail.allow_tags = True


@admin.register(models.ProjectGroup)
class AdminProjectGroup(admin.ModelAdmin):
    class AdminProjectGroupForm(ModelForm):
        class Meta:
            fields = '__all__'
            model = models.ProjectGroup
            widgets = {}

    class ProjectInline(SortableInlineAdminMixin, admin.TabularInline):
        model = models.Project
        extra = 0
        form = AdminProject.AdminProjectSmallForm
        readonly_fields = ('title',)

    form = AdminProjectGroupForm
    list_display = ('title', 'uri',)
    list_filter = ()
    exclude = ()
    search_fields = ['title', ]
    inlines = [ProjectInline, ]


@admin.register(models.ProjectImage)
class AdminProjectImage(admin.ModelAdmin):
    list_display = ('thumbnail', 'title', 'image',)
    list_filter = ()
    exclude = ()
    search_fields = ['title']
    inlines = []

    def thumbnail(self, obj):
        return admin_thumbnail_html(obj.image)

    thumbnail.allow_tags = True


@admin.register(models.Profile)
class AdminProfile(admin.ModelAdmin):
    class AdminProfileForm(ModelForm):
        class Meta:
            fields = '__all__'
            model = models.Project
            widgets = {}

    class ProfileContactInline(SortableInlineAdminMixin, admin.TabularInline):
        model = models.ProfileContact
        extra = 0

    form = AdminProfileForm
    inlines = [ProfileContactInline, ]


@admin.register(models.Article)
class AdminArticle(admin.ModelAdmin):
    class AdminArticleSmallForm(ModelForm):
        class Meta:
            fields = ('title',)
            model = models.Article

    class AdminArticleForm(ModelForm):
        class Meta:
            fields = '__all__'
            model = models.Article
            widgets = {}

    class ArticleAttachmentInline(admin.TabularInline):
        model = models.ArticleAttachment
        extra = 0

    form = AdminArticleForm
    list_display = ('title', 'uri', 'group', 'categories_list', 'created', 'active',)
    list_filter = ('active', 'group',)
    exclude = ()
    search_fields = ['title', ]
    inlines = [ArticleAttachmentInline, ]

    def categories_list(self, obj):
        return ', '.join([str(cat) for cat in obj.categories.all()])


admin.site.register(models.ArticleCategory)
admin.site.register(models.Tag)
