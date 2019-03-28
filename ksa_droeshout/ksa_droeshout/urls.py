from django.contrib import admin
from django.urls import path
from agenda import views as agenda_views
from inschrijven import views as inschrijven_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', agenda_views.IndexView.as_view(), name='home'),
    path('agenda/',agenda_views.AgendaView.as_view(),name='agenda'),
    path('agenda/<int:pk>/',agenda_views.AgendaItemView.as_view(),name='agenda_item'),
    path('inschrijven/',inschrijven_views.InschrijvenView.as_view(),name='inschrijven'),
    path('inschrijven/<int:pk>/',inschrijven_views.InschrijvenDetailView.as_view(),name='inschrijven_info'),
    path('inschrijven/add/',inschrijven_views.InschrijvenForm.as_view()),
    path('inschrijven/update/<int:pk>/',inschrijven_views.InschrijvenForm.as_view())
]
