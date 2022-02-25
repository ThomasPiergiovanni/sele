from django.views import View
from django.shortcuts import render
from django.core.serializers import serialize

from json import dumps

from collectivity.models.collectivity import Collectivity
from config.settings import MAPBOX_TOKEN
from information.forms.navbar_search_form import NavbarSearchForm


class HomeView(View):
    """Home view class.
    """
    def __init__(self):
        super().__init__()
        self.render = 'information/home.html'
        self.context = {
            'navbar_search_form': NavbarSearchForm(),
            'mapbox_url': self.__makejson(),
            'vector_layer': self.__getgeojson_from_model(),
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
        
    def __getgeojson_from_model(self):
        data_json = serialize(
            'geojson', 
            Collectivity.objects.filter(activity__exact='yes'),
            geometry_field='feat_geom',
            fields=('name','insee_code', 'activity')
        )
        return data_json

