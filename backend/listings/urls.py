
from django.urls import path
from .views import migrer_donnees
from . import views
urlpatterns = [
    path('etudiant',views.mes_donnees, name = 'mes_donnees'),
    path('admin', views.get_data, name='get_data'),
    path('professeur',views.donneNote,name='donneNote'),
    path('migrer-donnees/', migrer_donnees, name='migrer_donnees'),
    path('suppressionDonnees',views.supprimer_donnees,name='supprimer_donnees'),
    path('cheminDataProf',views.dataProf,name='dataProf'),
    path('cheminNote',views.notes,name ='notes'),
]