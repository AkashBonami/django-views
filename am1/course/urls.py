from django.urls import path, include
from course import views

urlpatterns = [
    path('learndj/', views.learn_django),
    path('learnpy/', views.learn_python),
]