from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('post/<int:post_id>/', views.post_detail),
    path('create/', views.create_post),
    path('edit/<int:post_id>/', views.edit_post),
    path('delete/<int:post_id>/', views.delete_post),
    path('signup/', views.signup),
    path('user/<str:username>/', views.profile),

]
