from django.urls import path

from pets.views import pet_list, pet_detail, pet_like, pet_create, pet_edit, pet_delete

urlpatterns = [
    path('', pet_list, name='pet_list'),
    path('detail/<int:pk>/', pet_detail, name='pet_detail'),
    path('like/<int:pk>/', pet_like, name='pet_like'),
    path('create/', pet_create, name='create_pet'),
    path('edit/<int:pk>/', pet_edit, name='edit_pet'),
    path('delete/<int:pk>/', pet_delete, name='delete_pet'),
]
