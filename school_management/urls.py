from django.urls import path

from .views import StudentAPIView,StudentUpdateView

urlpatterns = [
    path('students/',StudentAPIView.as_view(),name="students"),
    path('students/<int:pk>/',StudentUpdateView.as_view(),name="update-student")
]