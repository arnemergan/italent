from django.contrib import admin
from django.urls import path,include
from agenda import views as agenda_views
from inschrijven import views as inschrijven_views
from dashboard import views as daschboard_views
from django.contrib.auth import views as auth_views
from verhuur import views as verhuur_views
from index import views as index_views
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.contrib.auth.models import User

urlpatterns = [
    path('admin/', admin.site.urls),

    #overons
    path('overons/',index_views.OverView.as_view(),name='overons'),

    #contact
    path('contact/',index_views.ContactView.as_view(),name='contact'),
    #privacy
    path('privacy/',index_views.PrivacyView.as_view(),name='privacy'),

    #groepen
    path('groepen/',inschrijven_views.GroepenView.as_view(),name='groepen'),
    path('dashboard/groepen/',login_required(inschrijven_views.GroepListView.as_view()),name='dash_groepen'),
    path('dashboard/groepen/<int:pk>/update',login_required(inschrijven_views.GroepUpdateView.as_view()),name='dash_update_groep'),

    #verhuur
    path('verhuur/',verhuur_views.VerhuurTemplateView.as_view(),name='verhuur'),
    path('verhuur/lokaal/<int:pk>/update',verhuur_views.VerhuurLokaalUpdate.as_view(),name='updatelokaal'),
    path('verhuur/tent/<int:pk>/update',verhuur_views.VerhuurTentUpdate.as_view(),name='updatetent'),
    path('verhuur/materiaal/<int:pk>/update',verhuur_views.VerhuurMateriaalUpdate.as_view(),name='updatemateriaal'),
    path('dashboard/verhuur/',login_required(verhuur_views.VerhuurDashTemplateView.as_view()),name='dash_verhuur'),
    path('verhuur/tent/image/add/',login_required(verhuur_views.TentCreateImage.as_view()),name='add_tent'),
    path('verhuur/tent/image/<int:pk>/delete',login_required(verhuur_views.TentDeleteImage.as_view()),name='del_tent'),
    path('verhuur/lokaal/image/add/', login_required(verhuur_views.LokaalCreateImage.as_view()), name='add_lokaal'),
    path('verhuur/lokaal/image/<int:pk>/delete', login_required(verhuur_views.LokaalDeleteImage.as_view()), name='del_lokaal'),
    path('verhuur/lokaal/image/list/',login_required(verhuur_views.LokaalImageList.as_view()),name='lokaal_list'),
    path('verhuur/tent/image/list/',login_required(verhuur_views.TentImageList.as_view()),name='tent_list'),

    #begeleiding
    path('begeleiding/',inschrijven_views.BegeleidingView.as_view(),name='begeleiding'),
    path('dashboard/leiding/',login_required(inschrijven_views.LeidingListView.as_view()),name='dash_leiding'),
    path('dashboard/leiding/add/',login_required(inschrijven_views.LeidingCreateView.as_view()),name='add_leiding'),
    path('dashboard/leiding/<int:pk>/update',login_required(inschrijven_views.LeidingUpdateView.as_view()), name='update_leiding'),
    path('dashboard/leiding/<int:pk>/delete', login_required(inschrijven_views.LeidingDeleteView.as_view()),name='del_leiding'),
    # path('dashboard/user/add',login_required(inschrijven_views.UserCreateView.as_view()),name='add_user'),
    # path('dashboard/user/',login_required(inschrijven_views.UserListView.as_view()),name='users'),
    # path('dashboard/user/<int:pk>/delete/',login_required(inschrijven_views.UserDeleteView.as_view()),name='del_user'),

    #agenda
    path('', agenda_views.IndexView.as_view(), name='home'),
    path('agenda/',agenda_views.AgendaView.as_view(),name='agenda'),
    path('agenda/<int:pk>/',agenda_views.AgendaItemDetailView.as_view(),name='agenda_item'),

    path('agenda/item/add/',login_required(agenda_views.AgendaItemCreateView.as_view()),name='agenda_item_add'),
    path('agenda/item/<int:pk>/update/',login_required(agenda_views.AgendaItemUpdateView.as_view()),name='agenda_item_update'),
    path('agenda/item/<int:pk>/delete/',login_required(agenda_views.AgendaItemDeleteView.as_view()),name='agenda_item_delete'),
    path('agenda/list/',login_required(agenda_views.AgendaItemView.as_view()),name="agenda_item_list"),

    path ('agenda/download/',agenda_views.write_pdf_view,name='agenda_download'),

    #inschrijven
    path('inschrijven/',inschrijven_views.InschrijvenView.as_view(),name='inschrijven'),
    path('inschrijven/<int:pk>/',inschrijven_views.InschrijvenDetailView.as_view(),name='inschrijven_info'),
    path('inschrijven/lid/<uuid:lid_id>/<int:inschrijven_id>/',inschrijven_views.InschrijvenLidView.as_view(),name='inschrijven_lid'),
    path('inschrijven/nieuw/',inschrijven_views.InschrijveNieuwView.as_view(),name='inschrijven_nieuw'),

    path('inschrijven/item/add/',login_required(inschrijven_views.InschrijvenCreateView.as_view()),name='inschrijving_add'),
    path('inschrijven/item/<int:pk>/update/',login_required(inschrijven_views.InschrijvenUpdateView.as_view()),name='inschrijving_update'),
    path('inschrijven/item/<int:pk>/delete/',login_required(inschrijven_views.InschrijvenDeleteView.as_view()),name='inschrijving_delete'),
    path('inschrijven/list/',login_required(inschrijven_views.InschrijvingAllView.as_view()),name='inschrijving_all'),

    path('inschrijven/lid/<int:pk>/',login_required(inschrijven_views.InschrijvenLidListView.as_view()),name='inschrijvinglid_list'),
    path('inschrijven/lid/list/',login_required(inschrijven_views.InschrijvenLidListView.as_view()),name='list_inschrijvinglid'),

    path('leden/download/',login_required(inschrijven_views.export_leden_csv),name='leden_download'),
   # path('inscrhijving/download/',login_required(inschrijven_views.export_inschrijving_csv),name='export_leden'),

    #auth
    path('auth/login/',auth_views.LoginView.as_view(),name="login"),
    path('auth/logout/',auth_views.LogoutView.as_view(),name="logout"),
    path('auth/password_reset/',auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"),name="password_reset"),
    path('auth/password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="registration/reset_done.html"), name="password_reset_done"),
    path('auth/password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/reset_confirm.html"), name="password_reset_done"),

    #dashboard
    path('dashboard/',login_required(daschboard_views.dashboardView.as_view(),redirect_field_name=None),name="dash"),
    path('dashboard/leden/',login_required(inschrijven_views.LedenView.as_view()),name="dash_leden"),
    path('dashboad/leden/<uuid:lid_id>/',login_required(inschrijven_views.LidView.as_view()),name="dash_lid"),
    path('dashboard/leden/<uuid:lid_id>/delete/',login_required(inschrijven_views.LidDeleteView()),name='lid_delete'),

    path('dashboard/setting/change_password/',login_required(auth_views.PasswordChangeView.as_view()),name="change_password"),
    path('dashboard/setting/change_password/done/',login_required(auth_views.PasswordChangeDoneView.as_view()),name="change_password_done"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
