from django.contrib import admin
from django.urls import path
from agenda import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='home'),
    path('agenda/',views.AgendaView.as_view(),name='agenda'),
    path('agenda/<int:pk>/',views.AgendaItemView.as_view(),name='agenda_item'),
]
