from django.views import View
from django.shortcuts import render



class HomeView(View):
    """Home view class.
    """
    def __init__(self):
        super().__init__()
        self.render = 'exchange/home.html'
        self.context =  None

    def get(self, request):
        """Home page view method on client get request.
        """
        return render(request, self.render, self.context)
