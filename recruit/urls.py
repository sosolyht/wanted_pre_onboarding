from django.urls import path
from .views import RecruitView, RecruitModifyView

urlpatterns = [
    path('', RecruitView.as_view()),
    path('<int:job_id>', RecruitModifyView.as_view()),
]
