# Generated by Django 4.2.2 on 2023-06-10 17:22

import apps.main.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_aboutme_text_aboutmefulltextparts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Technologies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Technology name')),
            ],
            options={
                'verbose_name': 'technology',
                'verbose_name_plural': 'technologies',
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Project name')),
                ('short_description', models.TextField(max_length=3000, verbose_name='Project short description')),
                ('cover_photo', models.ImageField(upload_to=apps.main.models.projects_image_upload_path, verbose_name='Project cover photo')),
                ('link', models.URLField(verbose_name='Project link')),
                ('technologies_stack', models.ManyToManyField(related_name='technologies', to='main.technologies', verbose_name='Stack of technologies')),
            ],
            options={
                'verbose_name': 'project',
                'verbose_name_plural': 'Projects',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ProjectOverviewTextParts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Part text of Project overview')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_overview_parts', to='main.aboutme', verbose_name='Project instance')),
            ],
            options={
                'verbose_name': 'part',
                'verbose_name_plural': 'Project overview parts',
            },
        ),
    ]
