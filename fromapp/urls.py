from django.urls import path
# from .views import FormDataListCreateView, FormDataDetailsUpadteView, submit_form, success
from . import views

urlpatterns = [
    path('submit-form/', views.submit_form, name='submit-form'),
    path('success/', views.success, name='success'),
    path('form-data/', views.FormDataListCreateView.as_view(), name = 'form-data-list-create'),
    path('form-data/<int:pk>/', views.FormDataDetailsUpadteView.as_view(), name = 'form-data-detail-update')
]