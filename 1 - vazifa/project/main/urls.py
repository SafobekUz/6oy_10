from django.urls import path
from . import views

urlpatterns = [
    path('course/<int:course_id>/update/', views.update_course, name='update_course'),
    path('lesson/<int:lesson_id>/update/', views.update_lesson, name='update_lesson'),
]
