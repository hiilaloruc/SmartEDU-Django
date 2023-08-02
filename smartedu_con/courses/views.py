from django.shortcuts import render
from . models import Course, Category
# Create your views here.

def course_list(request):
    courses = Course.objects.all()
    #create a context variable to send some datas to the courses.html page.
    context = {
        'courses': courses.order_by('-date')
    }
    return render(request, 'courses.html',context)

def course_detail(request,category_slug,course_id):
    course = Course.objects.get(category__slug = category_slug, id = course_id)
    categories = Category.objects.all()
    context = {'course': course, 'categories': categories}
    return render(request, 'course.html', context)
