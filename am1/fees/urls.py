from django.urls import path, include
from fees import views

urlpatterns = [
    path('feesdj/', views.fees_django),
    path('feespy/', views.fees_python),
]