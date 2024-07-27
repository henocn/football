# Generated by Django 4.2 on 2023-10-11 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0002_alter_activite_images_alter_depense_eleve_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activite',
            name='description',
            field=models.CharField(blank=True, default='Aucune', max_length=255, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='activite',
            name='eleves',
            field=models.ManyToManyField(blank=True, null=True, to='gestion.eleve', verbose_name='Participants'),
        ),
        migrations.AlterField(
            model_name='depense',
            name='eleve',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gestion.eleve', verbose_name='Personne concernée'),
            preserve_default=False,
        ),
    ]
