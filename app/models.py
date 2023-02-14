from django.db import models


class RepoType(models.Model):
    name = models.CharField(max_length=250)


    class Meta:
        verbose_name = 'Repo Type'
        verbose_name_plural = 'Repo Types'

    def __str__(self):
        return self.name


class Repo(models.Model):
    repo_type = models.ForeignKey(RepoType, related_name='types', on_delete=models.CASCADE)
    repo_url = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='repos')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Education(models.Model):
    name = models.CharField(max_length=250)
    date = models.CharField(max_length=250)
    desc = models.TextField(blank=True, null=True)
    url = models.URLField(help_text='address url', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Experience(models.Model):
    name = models.CharField(max_length=250)
    date = models.CharField(max_length=250)
    desc = models.TextField()
    url = models.URLField(help_text='address url', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
