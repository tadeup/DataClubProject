from django.shortcuts import render
from django.views import generic, View

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'home/index.html'

class AboutView(View):
    def get(self, request):
        context = {
            'jorge':"this is a context generated conent"
        }
        return render(request, 'home/about.html', context)