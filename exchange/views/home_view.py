from django.views import View
from django.shortcuts import render

from json import dumps

from config.settings import MAPBOX_TOKEN
from exchange.forms.navbar_search_form import NavbarSearchForm


class HomeView(View):
    """Home view class.
    """
    def __init__(self):
        super().__init__()
        self.render = 'exchange/home.html'
        self.context = {
            'navbar_search_form': NavbarSearchForm(),
            'mapbox_url': self.__makejson()
        }

    def get(self, request):
        """Home page view method on client get request.
        """
        return render(request, self.render, self.context)
    
    def __makejson(self):
        data = {
            'url': 'https://api.mapbox.com/styles/v1/thomaspiergiovanni/ckmm3'+
            'kryyu79j17ptmgsmg9c9/tiles/{z}/{x}/{y}?access_token=' +
            MAPBOX_TOKEN
        }
        data_json = dumps(data)
        return data_json

