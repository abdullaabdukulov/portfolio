# Generated by Django 4.1.6 on 2023-02-15 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_education_created_at_education_updated_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('portfolio_url', models.URLField(blank=True, null=True)),
                ('job', models.CharField(max_length=250)),
                ('desc', models.TextField()),
            ],
        ),
    ]
