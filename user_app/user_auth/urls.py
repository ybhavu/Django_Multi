from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('patient-dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('doctor-dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('create/', views.create_post, name='create_post'),
    path('', views.post_list, name='post_list'),
    path('drafts/', views.draft_list, name='draft_list'),
    path('int:pk/edit/', views.post_edit, name='post_edit'),
]
