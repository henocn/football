from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from gestion.forms import FormEleve, AjoutActivite, AjoutDepense
from gestion.models import Eleve, Activite

import io
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter, portrait
from reportlab.platypus import SimpleDocTemplate, Image, Paragraph, Table, TableStyle, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

def generer_pdf(request):

    eleve = get_object_or_404(Eleve, nom="N'GASAMA", prenom="Henoc")
    activites = eleve.activite_set.all()
    depenses = eleve.depense_set.all()
    depense_total = sum([depense.montant for depense in depenses])

    na = len(activites)
    nta = len(Activite.objects.all())

    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=portrait(letter))

    elements = []
    header_table = Table([
        [Image('media/30.jpg', 150, 90), Paragraph('Programme de prise en charge dans le domaine Sportif et Social',  getSampleStyleSheet()['Title'])],
    ], colWidths=[4*inch, 2.5*inch])

    elements.extend([header_table, Spacer(1, 0.3*inch)])
    elements.append(Paragraph("Avertissements", getSampleStyleSheet()["Heading3"]))
    elements.append( Paragraph("Ceci est un fichier pdf généré de façon automatique par le site de gestion du programme de prise en charge Sportif et Social. Ces données dans ce fichiers sont basées sur celles entrées au préalables dans le système.", getSampleStyleSheet()['Normal']))

    elements.append(Spacer(2*inch, 0.5*inch))

    client_name = Paragraph(f"{eleve.nom} {eleve.prenom}", getSampleStyleSheet()['Title'])
    elements.append(client_name)

    def style(table):
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (1, 1), (-1, 0), 13, 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        elements.append(table)

    donnee_activite = [['Type', 'Date', 'Description']]
    for activite in activites:
        donnee_activite.append([activite.type, activite.date, activite.description])
    table_activite = Table(donnee_activite, colWidths=2.1*inch)

    donnee_depense = [['Type', 'Date', 'Description', 'Montant']]
    for depense in depenses:
        montant = str(depense.montant)
        donnee_depense.append([depense.type, depense.date, depense.infos, montant + ' fcfa'])
    table_depense = Table(donnee_depense, colWidths=1.575*inch)

    elements.append(Paragraph(f"Les ativités auxquelles a participé l'élève ({(na/nta)*100}%) :", getSampleStyleSheet()["Heading3"]))
    style(table_activite)
    elements.append(Spacer(2 * inch, 0.5 * inch))
    elements.append(Paragraph(f"Les dépenses pour le compte de l'élève ({depense_total} FCFA):", getSampleStyleSheet()["Heading3"]))
    style(table_depense)

    elements.append(Spacer(2 * inch, 0.5 * inch))
    footer_table = Table([
        [Paragraph(f"Date de génération : {datetime.now()}", getSampleStyleSheet()["Heading4"]), Paragraph('Mr ABCDEF Ghijkl',  getSampleStyleSheet()['Heading4'])],
    ], colWidths=[4*inch, 2.5*inch])

    elements.extend([footer_table, Spacer(1, 0.3 * inch)])
    doc.build(elements)
    
    response = HttpResponse(buffer.getvalue(), content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename=facture.pdf'
    
    buffer.close()

    return response


def accueil(request):
    eleves = Eleve.objects.all()
    return render(request, "gestion/index.html", context={"eleves": eleves})

def details_eleve(request, nom, prenom):
    eleve = get_object_or_404(Eleve, nom=nom, prenom=prenom)
    activites = eleve.activite_set.all()
    depenses = eleve.depense_set.all()
    depense_total = sum([depense.montant for depense in depenses])
    return render(request, 'gestion/details.html', {"eleve": eleve, "activites": activites, "depenses": depenses, "depense_total":depense_total})

def ajouter_eleve(request):
    if request.method == "POST":
        form = FormEleve(request.POST, request.FILES)
        if form.is_valid():
            eleve = form.save(commit=False)
            eleve.save()
            return redirect("accueil")
    else:
        form = FormEleve()
        return render(request, 'gestion/ajout.html', {"form": form })

def ajouter_depense(request):
    if request.method == "POST":
        form = AjoutDepense(request.POST, request.FILES)
        if form.is_valid():
            depense = form.save(commit=False)
            depense.save()
            return redirect(reverse("details_eleve", kwargs={"nom": form.cleaned_data["eleve"].nom, "prenom": form.cleaned_data["eleve"].prenom}))

    form = AjoutDepense()
    return render(request, 'gestion/depense.html', {"form": form})


def activite(request):
    activites = Activite.objects.all()
    if request.method == "POST":
        form = AjoutActivite(request.POST, request.FILES)
        if form.is_valid():
            activite = form.save()
            activite.save()
            return redirect(reverse("activite"))

    form = AjoutActivite()
    return render(request, 'gestion/activite.html', {"form": form, "activites": activites})
