from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Lesson

def update_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        course.name = request.POST.get('name', course.name)
        course.description = request.POST.get('description', course.description)
        course.save()
        return redirect('course_detail', course_id=course.id)
    return render(request, 'update_course.html', {'course': course})


def update_lesson(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    if request.method == 'POST':
        lesson.title = request.POST.get('title', lesson.title)
        lesson.content = request.POST.get('content', lesson.content)
        lesson.save()
        return redirect('lesson_detail', lesson_id=lesson.id)
    return render(request, 'update_lesson.html', {'lesson': lesson})
