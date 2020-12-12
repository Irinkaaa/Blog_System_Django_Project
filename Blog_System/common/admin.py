from django.contrib import admin
from Blog_System.common.models import BlogSystemSettings


class BlogSystemSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False


admin.site.register(BlogSystemSettings, BlogSystemSettingsAdmin)
