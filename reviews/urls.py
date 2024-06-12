
from . import views
from django.urls import path

urlpatterns=[
    path("",views.ReviewView.as_view()),
    path("thank-you",views.ThanksYouView.as_view()),
    path("reviews",views.ReviewListView.as_view()),
    path("reviews/<int:pk>",views.SignleReviewView.as_view()),    
]