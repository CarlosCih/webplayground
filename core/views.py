from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'core/home.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'message': '¡Bienvenido a la página de inicio! Esta es una vista basada en clases.'})

def sample(request):
    return render(request, 'core/sample.html')