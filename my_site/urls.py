from django.urls import path

from . import views
from .views import CountListView

app_name = 'my_site'
urlpatterns = [
    path('', CountListView.as_view() , name='index'),
    path('my_site', CountListView.as_view(), name='my_site'),
    path('count/<int:count_id>/', views.count, name='count'),
    path('count/<int:count_id>/delete/', views.delete, name='delete'),
    path('count/<int:count_id>/update/', views.update, name='update'),
]