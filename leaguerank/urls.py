from django.urls import path
from . import views

app_name = 'leaguerank'

urlpatterns = [
    path('', views.leaguerankListView.as_view(), name='all'),
    path('leaguerank/<int:pk>/detail', views.leaguerankDetailView.as_view(), name='leaguerank_detail'),
    path('leaguerank/create/', views.leaguerankCreateView.as_view(), name='leaguerank_create'),
    path('leaguerank/<int:pk>/update/', views.leaguerankUpdateView.as_view(), name='leaguerank_update'),
    path('leaguerank/<int:pk>/delete/', views.leaguerankDeleteView.as_view(), name='leaguerank_delete'),
]
