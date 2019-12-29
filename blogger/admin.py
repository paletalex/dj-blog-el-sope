from django.contrib import admin
from .models import Post, Category, Tag
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class PostResource(resources.ModelResource):
    class Meta:
        model = Post
        export_order = ('id', 'created')

class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category
        export_order = ('id', 'created')

class TagResource(resources.ModelResource):
    class Meta:
        model = Tag
        export_order = ('id', 'created')
# Register your models here.
class PostAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'published', 'author')
    date_hierarchy = 'published'
    
    prepopulated_fields = {'slug': ('title',)}
    class Media:
        css = {
            'all': ('blogger/css/custom_ckeditor.css',)
        }
class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class TagAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)