# Generated by Django 4.2.2 on 2023-06-10 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_aboutme_short_info_alter_aboutme_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutme',
            name='text',
        ),
        migrations.CreateModel(
            name='AboutMeFullTextParts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Part text of About me info')),
                ('me', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='full_text_parts', to='main.aboutme', verbose_name='About me instance')),
            ],
            options={
                'verbose_name': 'part',
                'verbose_name_plural': 'About me text parts',
            },
        ),
    ]