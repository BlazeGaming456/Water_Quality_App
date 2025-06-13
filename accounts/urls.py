from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('api/save-test/', views.save_test_data, name='save_test'),
    path('api/test-history/', views.get_test_history, name='test_history'),
    path('api/generate-dummy-test/', views.generate_dummy_test, name='generate_dummy_test'),
]