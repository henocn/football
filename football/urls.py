from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from football import settings
from gestion.views import accueil, ajouter_eleve, activite, ajouter_depense, details_eleve, generer_pdf

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accueil, name="accueil"),
    path('<str:nom>/<str:prenom>/', details_eleve, name="details_eleve"),
    path('ajouter/', ajouter_eleve, name="ajouter_eleve"),
    path('generer_pdf/', generer_pdf, name="generer_pdf"),
    path('activite/', activite, name="activite"),
    path('depense/', ajouter_depense, name="ajouter_depense"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)