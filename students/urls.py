from django.urls import path
from django.contrib.auth import views as auth_views
from students.views import *

urlpatterns = [
    path('',home,name='home'),
    path('register/', register, name='register'),
    path('dashboard/', student_dashboard, name='student_dashboard'),
    path('update-profile/', update_profile, name='update_profile'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', student_dashboard, name='student_dashboard'),
    path('course/<int:course_id>/', course_materials, name='course_materials'),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('remove-course/<int:course_id>/', remove_course, name='remove_course'),

]
