from django.shortcuts import render
from django.views import View
from .services import get_today_year
from .models import AboutMe


class MainView(View):

    def get(self, *args, **kwargs):
        try:
            me = AboutMe.objects.get(id=1)
        except AboutMe.DoesNotExist:
            return render(self.request, 'index.html')
        today_year = get_today_year()
        site_url = '127.0.0.1:8000'
        context = {
            'today_year': today_year,
            'okuzmenko_url': site_url,
            'me': me
        }
        return render(self.request, template_name='index.html', context=context)
