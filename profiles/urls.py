from django.urls import path
from profiles import views

urlpatterns = [
    path('details/', views.detailed_profile, name='profile-details'),
    path('delete/', views.delete_profile, name='delete-profile'),

]