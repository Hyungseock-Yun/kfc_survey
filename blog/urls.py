from django.urls import path
from . import views


urlpatterns = [
    path('', views.posts, name='posts'),
    path('survey/', views.survey, name='survey'),

    # path('post/<int:id>/', views.post_detail, name='post_detail'),
]
