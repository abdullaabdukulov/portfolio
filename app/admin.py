from django.contrib import admin
from .models import Repo, RepoType


@admin.register(RepoType)
class RepoTypeAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Repo)
class RepoAdmin(admin.ModelAdmin):
    list_display = ['repo_type', 'image', 'name', 'created_at', 'updated_at']
    list_filter = ['repo_type', 'created_at']

