from django.urls import path
from .views import JobSearchView, RecruitDetailView, RecruitView, RecruitModifyView

urlpatterns = [
    path('', RecruitView.as_view()),
    path('<int:job_id>', RecruitModifyView.as_view()),
    path('search', JobSearchView.as_view()),
    path('find/<int:job_id>', RecruitDetailView.as_view()),
]
