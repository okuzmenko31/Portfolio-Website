from django.contrib import admin
from .models import Skills, AboutMe, AboutMeFullTextParts, Technologies, Projects, ProjectOverviewTextParts


@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    pass


class AboutMeFullTextPartsTabularInline(admin.TabularInline):
    model = AboutMeFullTextParts
    extra = 3


class ProjectOverviewTextPartsTabularInline(admin.TabularInline):
    model = ProjectOverviewTextParts
    extra = 3


@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    inlines = [AboutMeFullTextPartsTabularInline]


@admin.register(Technologies)
class TechnologiesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['id', 'name']


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'link']
    list_display_links = ['id', 'name', 'link']
    search_fields = ['id', 'name', 'link']
    inlines = [ProjectOverviewTextPartsTabularInline]
