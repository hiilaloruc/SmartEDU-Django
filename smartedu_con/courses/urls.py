from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name="courses"), #that name can be used in navbar

    path('<slug:category_slug>/<int:course_id>',views.course_detail, name="course_detail" ),

    path('category/<slug:category_slug>', views.category_detail,name= 'category_detail' ), #category_detail page

    path('tag/<slug:tag_slug>', views.tag_detail, name="tag_detail") #tag_detail page
]