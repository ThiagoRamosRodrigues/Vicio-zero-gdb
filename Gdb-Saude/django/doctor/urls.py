from django.urls import path
from .views import HomeTemplateView, AppointmentTemplateView, ManageAppointmentTemplateView
from . import views
urlpatterns = [
    path("", HomeTemplateView.as_view(), name="home"),
    path("make-an-appointment/", AppointmentTemplateView.as_view(), name="appointment"),
    path("manage-appointments/", ManageAppointmentTemplateView.as_view(), name="manage"),
    path('tratamento-cannabis/', views.tratamento_cannabis, name='tratamento_cannabis'),
    path('tratamento-jogos-de-azar/', views.tratamento_jogos_de_azar, name='tratamento_jogos_de_azar'),
    path('tratamento-tabaco/', views.tratamento_tabaco, name='tratamento_tabaco'),
    path('tratamento-alcoolismo/', views.tratamento_alcoolismo, name='tratamento_alcoolismo'),
]
