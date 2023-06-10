from django.contrib import admin
from .models import Skills, AboutMe, AboutMeFullTextParts


@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    pass


class AboutMeFullTextPartsTabularInline(admin.TabularInline):
    model = AboutMeFullTextParts
    extra = 3


@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    inlines = [AboutMeFullTextPartsTabularInline]
