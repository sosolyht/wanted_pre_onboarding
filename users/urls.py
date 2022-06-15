from django.urls import path

from users.views import ApplyJobView

urlpatterns = [
    path('', ApplyJobView.as_view()),
]
