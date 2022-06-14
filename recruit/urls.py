from django.urls import path
from .views import JobSearchView, RecruitView, RecruitModifyView

urlpatterns = [
    path('', RecruitView.as_view()),
    path('<int:job_id>', RecruitModifyView.as_view()),
    path('search', JobSearchView.as_view()),
]
