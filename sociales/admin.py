from django.contrib import admin
from .models import Social
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class SocialResource(resources.ModelResource):
    class Meta:
        model = Social
        export_order = ('id', 'created')
# Register your models here.
class SocialAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    readonly_field=('created', 'updated')
    list_display = ('key', 'name', 'link')

admin.site.register(Social, SocialAdmin)

