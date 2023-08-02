from django.shortcuts import render
from . models import Course
# Create your views here.

def course_list(request):
    courses = Course.objects.all()
    #create a context variable to send some datas to the courses.html page.
    context = {
        'courses': courses.order_by('-date')
    }
    return render(request, 'courses.html',context)