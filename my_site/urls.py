from django.urls import path

from . import views
from .views import CountListView

urlpatterns = [
    path('', CountListView.as_view() , name='index'),
    path('my_site', CountListView.as_view(), name='main'),
    path('count/<int:count_id>/', views.count, name='count'),
    path('count/<int:count_id>/delete/', views.delete, name='delete'),
    path('count/<int:count_id>/update/', views.update, name='update'),
]