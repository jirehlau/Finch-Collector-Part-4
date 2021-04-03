from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.about, name='about'),
    path('restaurants/', views.restaurants_index, name='index'),
    path('restaurants/<int:r_id>/', views.restaurants_detail, name='detail'),
    path('restaurants/<int:r_id>/delete/', views.delete, name='delete'),
    # create form 1 - deliver a form
    path('restaurants/create_form', views.create_form),
    # create step 2 - accept form submission    
    path('restaurants/submit_create_form',views.submit_create_form),
    # update step 1 - deliver the form to user
    path('restaurants/<int:r_id>/edit/', views.edit_form),
    # update step 2 - accept form submission 
    path('restaurants/<int:r_id>/submit_update_form/', views.submit_update_form),
]

