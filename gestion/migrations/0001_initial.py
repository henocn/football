# Generated by Django 4.2 on 2023-10-11 22:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eleve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profil', models.ImageField(upload_to='profils', verbose_name='Photo de profil')),
                ('nom', models.CharField(max_length=128, verbose_name='Nom')),
                ('prenom', models.CharField(max_length=128, verbose_name='Prenom')),
                ('dateNaiss', models.DateField(verbose_name='Date de naissanse')),
                ('residence', models.CharField(max_length=50, verbose_name='Lieu de résidence')),
            ],
        ),
        migrations.CreateModel(
            name='Depense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recu', models.ImageField(upload_to='recu', verbose_name='Réçu de paiement')),
                ('type', models.CharField(choices=[('Sanitaires', 'Sanitaires'), ('Scolaires', 'Scolaires'), ('Sportifs', 'Sportifs'), ('Autres', 'Autres')], max_length=40, verbose_name='Type de dépense')),
                ('infos', models.CharField(max_length=255, null=True, verbose_name='Infos supplémentaires')),
                ('date', models.DateField(max_length=255, verbose_name='Effectuée le ')),
                ('montant', models.IntegerField(default=0)),
                ('eleve', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.eleve', verbose_name='Personne concernée')),
            ],
        ),
        migrations.CreateModel(
            name='Activite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='activite', verbose_name="Image de l'activité")),
                ('type', models.CharField(choices=[('Entrainement', 'Entrainement'), ('Match', 'Match'), ('Autre activite sportive', 'Autre activite sportive'), ('Activité non sportive', 'Activité non sportive')], max_length=40, verbose_name="Type d'activité")),
                ('description', models.CharField(max_length=255, null=True, verbose_name='Description')),
                ('date', models.DateField(max_length=255, verbose_name="Date de l'activité")),
                ('eleves', models.ManyToManyField(to='gestion.eleve', verbose_name='Participants')),
            ],
        ),
    ]
