from django import forms
from gestion.models import Eleve, Activite, Depense


class FormEleve(forms.ModelForm):
    class Meta:
        model = Eleve
        fields = ["nom", "prenom", "dateNaiss", "residence", "profil"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for element in self.fields:
            self.fields[element].widget.attrs.update({
                'class': 'form-control',
            })

class AjoutActivite(forms.ModelForm):
    class Meta:
        model = Activite
        fields = ["type", "description", "eleves", "date", "images"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for element in self.fields:
            self.fields[element].widget.attrs.update({
                'class': 'form-control form-control-sm',
            })

class AjoutDepense(forms.ModelForm):
    class Meta:
        model = Depense
        fields = ["type", "infos", "eleve", "date", "montant", "recu"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for element in self.fields:
            self.fields[element].widget.attrs.update({
                'class': 'form-control form-control-sm',
            })