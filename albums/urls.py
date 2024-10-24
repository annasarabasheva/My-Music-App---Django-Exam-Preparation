from django.urls import path, include
from albums import views

urlpatterns = [
    path('add/', views.add_album, name='add-album'),
    path('<int:id>/', include([
        path('details/', views.detailed_album, name='album-details'),
        path('edit/', views.edit_album, name='edit-album'),
        path('delete/', views.delete_album, name='delete-album'),
    ]))

]