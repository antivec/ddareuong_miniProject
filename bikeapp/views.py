from django.shortcuts import render
from django.views.generic.base import TemplateView

class MainpageView(TemplateView):
    template_name = 'bikeapp/index.html'
# Create your views here.
def index(request):
    return render(request, 'index.html')