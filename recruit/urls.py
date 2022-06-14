from django.urls import path
from .views import RecruitView

urlpatterns = [
    path('', RecruitView.as_view()),
]
