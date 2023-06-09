from django.urls import path
from . import views

urlpatterns = [
    path("teacher/", views.add_teacher, name="add_teacher"),
    path("teachers/", views.teacher_list, name="teacher_list"),
    path("group/", views.add_group, name="add_group"),
    path("groups/", views.group_list, name="group_list"),
]
