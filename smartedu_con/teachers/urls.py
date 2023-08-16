from django.urls import path
from teachers.views import TeacherListView

urlpatterns = [
    path('', TeacherListView.as_view() , name="teachers"), #that name can be used in navbar

]