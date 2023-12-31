from django.shortcuts import render
#from django.http import HttpResponse
from django.views.generic import TemplateView
from courses.models import Course

""" # Create your views here.
def index(request):
    #return HttpResponse('<h1>INDEX RESPONSE of Hilal</h1>' )
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')
 """
class AboutView(TemplateView):
    template_name = "about.html"

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.filter(available = True).order_by('-date')[:2]
        context['total_course'] = Course.objects.filter(available = True).count()
        
        return context
