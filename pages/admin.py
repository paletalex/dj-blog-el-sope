from django.contrib import admin
from .models import Page
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class PageResource(resources.ModelResource):
    class Meta:
        model = Page
        export_order = ('id', 'created')
# Register your models here.
class PageAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ['title', 'content']

admin.site.register(Page, PageAdmin)