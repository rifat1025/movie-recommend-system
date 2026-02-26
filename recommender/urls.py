from django.urls import path
from . import views

urlpatterns = [
    path('',views.fetch_poster,name='fetch_poster'),
]
