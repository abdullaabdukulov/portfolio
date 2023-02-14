from django.contrib import admin
from .models import Repo, RepoType, Skill, Education, Experience


@admin.register(RepoType)
class RepoTypeAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Repo)
class RepoAdmin(admin.ModelAdmin):
    list_display = ['repo_type', 'image', 'name', 'created_at', 'updated_at']
    list_filter = ['repo_type', 'created_at']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = ({'slug': ('name',)})


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['name', 'desc', 'date', 'url', 'created_at', 'updated_at']


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['name', 'desc', 'date', 'url', 'created_at', 'updated_at']
