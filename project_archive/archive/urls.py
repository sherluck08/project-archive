from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('account.urls'), name="archive-home"),
    path('project/', views.project_page, name='project-page'),
    path('add-project/', views.add_project, name='add-project'),
    path('admin-page/', views.adminpage, name='admin-page'),
    path('admin-home/', views.admin_home, name='admin-home'),
    path('assign-project/', views.assign_project, name='assign-project'),
    path('submitted-project/', views.submitted_project, name='submitted-project'),
    path('student/home/', views.student_home, name='student-home'),
    path('student/submit-project/', views.student_submit_project,
         name='student-submit-project'),
]
