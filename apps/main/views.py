from django.shortcuts import render
from django.views import View


class MainView(View):

    def get(self, *args, **kwargs):
        return render(self.request, 'index.html')
