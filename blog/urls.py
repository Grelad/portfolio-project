from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    path('<int:blog_id>/', views.detail, name = 'detail'),
]
