from django.contrib import admin
from portfolio.models  import Image, Project, Biography

admin.site.register(Image)
admin.site.register(Biography)

class InlineImage(admin.TabularInline):
    model = Image

class ProjectAdmin(admin.ModelAdmin):
    inlines = [InlineImage]

admin.site.register(Project, ProjectAdmin)


# Register your models here.
