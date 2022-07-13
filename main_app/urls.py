# path function to define each route
from django.urls import path
from . import views

# urlpatterns to hold each route
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('businesses/', views.businesses_index, name='index'),
    path('businesses/<int:business_id>/', views.businesses_detail, name='detail'),
    path('businesses/create/', views.BusinessCreate.as_view(), name='businesses_create'),
    path('businesses/<int:pk>/update/', views.BusinessUpdate.as_view(), name='businesses_update'),
    path('businesses/<int:pk>/delete/', views.BusinessDelete.as_view(), name='businesses_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]
