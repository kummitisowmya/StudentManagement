from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import Student
from .forms import StudentRegistrationForm, StudentProfileForm
from django.contrib.auth.decorators import login_required
from .models import StudentCourse, Material
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from .forms import StudentCourseForm

def home(request):
    return render(request,"home.html")
def register(request):
    if request.method == "POST":
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            Student.objects.create(user=user)
            return redirect('login')
    else:
        form = StudentRegistrationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def student_dashboard(request):
    student = request.user.student
    return render(request, 'dashboard.html', {'student': student})
@login_required
def update_profile(request):
    user = request.user

    # Ensure the user has a Student object
    student, created = Student.objects.get_or_create(user=user)

    if request.method == "POST":
        form = StudentProfileForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_dashboard')
    else:
        form = StudentProfileForm(instance=student)

    return render(request, 'update_profile.html', {'form': form})

@login_required
def student_dashboard(request):
    student_courses = StudentCourse.objects.filter(student=request.user)
    return render(request, 'dashboard.html', {'student_courses': student_courses})

@login_required
def course_materials(request, course_id):
    materials = Material.objects.filter(course_id=course_id)
    return render(request, 'course_material.html', {'materials': materials})


# Ensure only superusers can access this view

from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import StudentCourse
from .forms import StudentCourseForm

# Ensure only superusers can access
def superuser_required(user):
    return user.is_superuser

@user_passes_test(superuser_required)
def admin_dashboard(request):
    courses = StudentCourse.objects.all()  # Fetch all course assignments

    if request.method == "POST":
        form = StudentCourseForm(request.POST)
        if form.is_valid():
            student = form.cleaned_data['student']
            course = form.cleaned_data['course']

            if StudentCourse.objects.filter(student=student, course=course).exists():
                messages.error(request, "This student is already assigned to this course.")
            else:
                form.save()
                messages.success(request, "Course assigned successfully!")
                return redirect('admin_dashboard')

    else:
        form = StudentCourseForm()

    return render(request, 'admin_dashboard.html', {'form': form, 'courses': courses})
from django.shortcuts import get_object_or_404

@user_passes_test(superuser_required)
def remove_course(request, course_id):
    course = get_object_or_404(StudentCourse, id=course_id)
    course.delete()
    messages.success(request, "Course removed successfully!")
    return redirect('admin_dashboard')
