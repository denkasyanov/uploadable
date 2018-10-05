from django.urls import path

from . import views


urlpatterns = [
    path('', views.PictureListView.as_view(), name='list'),
    path('add-picture/', views.PictureCreateView.as_view(), name='create'),
    # path('upload/', views.simple_upload, name='upload'),
    # path('model-form-upload/', views.model_form_upload,
    #       name='model-form-upload'),
]
