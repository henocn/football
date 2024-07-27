from django.db import models

# Create your models here.
class Eleve(models.Model):
    profil = models.ImageField(verbose_name="Photo de profil", upload_to="profils", blank=True, null=True)
    nom = models.CharField(verbose_name="Nom", max_length=128)
    prenom = models.CharField(verbose_name="Prenom", max_length=128)
    dateNaiss = models.DateField(verbose_name="Date de naissanse")
    residence = models.CharField(verbose_name="Lieu de résidence", max_length=50)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Activite(models.Model):
    choix = [
        ("Entrainement", "Entrainement"), ("Match", "Match"), ("Autre activite sportive", "Autre activite sportive"),
        ("Activité non sportive", "Activité non sportive"),
    ]
    images = models.ImageField(verbose_name="Image de l'activité", upload_to="activite", blank=True, null=True)
    type = models.CharField(verbose_name="Type d'activité", max_length=40, choices=choix)
    eleves = models.ManyToManyField(Eleve, verbose_name="Participants", null=True, blank=True)
    description = models.CharField(verbose_name="Description",default="Aucune",  max_length=255, null=True, blank=True)
    date = models.DateField(verbose_name="Date de l'activité", max_length=255)

    def __str__(self):
        return f"Activité du {self.date}"


class Depense(models.Model):
    choix = [
        ("Sanitaires", "Sanitaires"), ("Scolaires", "Scolaires"), ("Sportifs", "Sportifs"),
        ("Autres", "Autres"),
    ]
    recu = models.ImageField(verbose_name="Réçu de paiement", upload_to="recu", blank=True, null=True)
    type = models.CharField(verbose_name="Type de dépense", max_length=40, choices=choix)
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE, verbose_name="Personne concernée")
    infos = models.CharField(verbose_name="Infos supplémentaires", max_length=255, null=True, blank=True)
    date = models.DateField(verbose_name="Effectuée le ", max_length=255)
    montant = models.IntegerField(default=0)


    def __str__(self):
        return f"{self.eleve.nom} {self.eleve.prenom} {self.type}"

