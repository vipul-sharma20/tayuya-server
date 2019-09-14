from django.urls import path

from app import views


urlpatterns = [
    path('', views.home, name='home_view'),
    path('tabs/', views.render_tabs, name='tabs_view'),
]
