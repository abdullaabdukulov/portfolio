# Generated by Django 4.1.6 on 2023-02-14 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_skill'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('date', models.CharField(max_length=250)),
                ('desc', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('date', models.CharField(max_length=250)),
                ('desc', models.TextField()),
                ('url', models.URLField(blank=True, help_text='address url', null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='repo',
            name='repo_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]