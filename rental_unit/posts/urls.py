from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_changeList'),
    path('add/', views.PostCreateView.as_view(), name='post_add'),
    path('detail/<slug:slug>/', views.PostDetailView.as_view(), name = 'post_detail'),
    path('<slug:slug>/', views.PostUpdateView.as_view(), name = 'post_change'),

    # this is the url which will be loaded by ajax calls
    # path('ajax/load-cities', views.load_cities, name='ajax_load_cities'),
    path('city-autocomplete/', views.CityAutoComplete.as_view(), name='city-autocomplete'),
    path('state-autocomplete/', views.StateAutoComplete.as_view(), name='state-autocomplete'),
]