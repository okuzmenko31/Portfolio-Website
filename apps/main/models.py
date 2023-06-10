from django.db import models


class Skills(models.Model):
    name = models.CharField(max_length=80, verbose_name='Skill name')

    class Meta:
        verbose_name = 'skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return f'Skill: {self.name}'


class AboutMe(models.Model):
    full_name = models.CharField(max_length=100,
                                 verbose_name='Full Name')
    short_info = models.TextField(max_length=3000,
                                  verbose_name='Short text about me',
                                  blank=True)
    skills = models.ManyToManyField(Skills, related_name='skills')

    class Meta:
        verbose_name = 'about'
        verbose_name_plural = 'About me'

    def __str__(self):
        return f'About {self.full_name}'


class AboutMeFullTextParts(models.Model):
    text = models.TextField(verbose_name='Part text of About me info')
    me = models.ForeignKey(AboutMe,
                           on_delete=models.CASCADE,
                           verbose_name='About me instance',
                           related_name='full_text_parts')

    class Meta:
        verbose_name = 'part'
        verbose_name_plural = 'About me text parts'

    def __str__(self):
        return f'About info text part of: {self.me.full_name}'
