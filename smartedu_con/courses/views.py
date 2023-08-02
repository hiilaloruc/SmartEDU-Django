from django.shortcuts import render
from . models import Course, Category,Tag
# Create your views here.

def course_list(request):
    courses = Course.objects.all()
    tags = Tag.objects.all()
    categories = Category.objects.all()
    #create a context variable to send some datas to the courses.html page.
    context = {
        'courses': courses.order_by('-date'),
        'categories': categories,'tags': tags
    }
    return render(request, 'courses.html',context)

def course_detail(request,category_slug,course_id):
    course = Course.objects.get(category__slug = category_slug, id = course_id)
    tags = Tag.objects.all()
    categories = Category.objects.all()
    context = {'course': course, 'tags': tags,'categories': categories}
    return render(request, 'course.html', context)

def category_detail(request,category_slug):
    #category = Category.objects.get(category_slug = category_slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    courses = Course.objects.filter(category__slug=category_slug)
    context = {'courses': courses.order_by('-date'), 'categories': categories,'tags': tags}
    return render(request, 'courses.html',context)


def tag_detail(request,tag_slug):
    #tag = tag.objects.get(tag_slug = tag_slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    courses = Course.objects.filter(tags__slug=tag_slug)
    context = {'courses': courses.order_by('-date'), 'tags': tags,'categories': categories}
    return render(request, 'courses.html',context)