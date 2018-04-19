from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_changeList'),
    path('add/', views.PostCreateView.as_view(), name='post_add'),
    path('detail/<int:pk>/', views.PostDetailView.as_view(), name = 'post_detail'),
    path('<int:pk>/', views.PostUpdateView.as_view(), name = 'post_change'),

    # this is the url which will be loaded by ajax calls
    path('ajax/load-cities', views.load_cities, name='ajax_load_cities'),
]