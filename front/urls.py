from django.urls import path

from . import views


urlpatterns = [
    path('add-picture/', views.AddPictureView.as_view(), name='add'),
    path('', views.AllPicturesView.as_view(), name='list')
]
