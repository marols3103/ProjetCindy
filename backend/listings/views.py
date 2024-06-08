from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import PremiereA, Etudiant
import json
from .models import Professeur,Admin,Notes
"""from .models import Notes"""

@csrf_exempt
def mes_donnees(request):
    if request.method == 'POST':
        form = json.loads(request.body)
        print(form)
        form_data = PremiereA.objects.create(
            cne             = form.get('cne', ''),
            nom_etudiant    = form.get('nom_etudiant', ''),
            prenom_etudiant = form.get('prenom_etudiant', ''),
            email_etudiant  = form.get('email_etudiant', ''),
            adresse         = form.get('adresse'),
            telephone       = form.get('telephone',''),
            niveau          = form.get('niveau',''),
            
        )
        return JsonResponse({'message':'reussi'})
    return JsonResponse({'error':'erreur'},status = 405),

@csrf_exempt
def notes(request):
    if request.method == 'POST':
        noteBody = json.loads(request.body)
        formNote = Notes.objects.create(
            cne = noteBody.get('cne',''),
            add = noteBody.get('add',''),
            sir = noteBody.get('sir',''),
            programmation = noteBody.get('programmation',''),
            tec = noteBody.get('tec',''),
            an =noteBody.get('an',''),
            tst =noteBody.get('tst',''),
            moyenne = noteBody.get('moyenne',''),
        )
        return JsonResponse({'message':'reussi'})
    return JsonResponse({'error':'erreur'},status = 405),

@csrf_exempt
def donneNote(request):
    if request.method == 'POST':
        form = json.loads(request.body)
        print(form) 
        dataNote  =  Notes.objects.create(
            cne               = form.get('cne',''),
            nom_etudiant      = form.get('nom_etudiant',''),
            prenom_etudiant   = form.get('prenom_etudiant',''),
            note              = form.get('note',''),
        )
        return JsonResponse({'message':'reussi'})
    return JsonResponse({'error':'erreur'},status = 405),    

def get_data(request):
    students = PremiereA.objects.all()
    data = [{'cne': student.cne,
             'nom_etudiant'   : student.nom_etudiant, 
             'prenom_etudiant': student.prenom_etudiant,
             'email_etudiant' :student.email_etudiant,
             'adresse'        : student.adresse, 
             'telephone'      : student.telephone,
             'niveau'         : student.niveau}
            for student in students]
    return JsonResponse({'data': data})

def dataProf(request):
    profs = Professeur.objects.all()
    dataprof = [{
        'identifiant' : prof.identifiant,
        'nom_professeur':prof.nom_professeur,
        'prenom_professeur':prof.prenom_professeur,
        'departement':prof.departement,
        'mot_de_passe':prof.mot_de_passe} 
        for prof in profs]
    return JsonResponse({'dataprof': dataprof})

def GetNotes(request):
    notes = Notes.objects.all()
    notesEtu = [{
        'cne':note.cne,
        'add':note.add,
        'sir':note.sir,
        'programmation':note.programmation,
        'tec':note.tec,
        'tst':note.tst,
    }for note in notes]



@csrf_exempt
def migrer_donnees(request):
    if request.method == 'POST':
    
        donnees_source = PremiereA.objects.all()

        # Migratez les données vers la base de données de destination
        for donnee in donnees_source:
            Etudiant.objects.create(
                cne=donnee.cne,
                nom_etudiant=donnee.nom_etudiant,
                prenom_etudiant=donnee.prenom_etudiant,
                adresse=donnee.adresse,
                telephone=donnee.telephone,
                niveau=donnee.niveau,
                email_etudiant=donnee.email_etudiant,
            )
            donnee.delete()

        return JsonResponse({'message': 'Migration réussie'})
    return JsonResponse({'error': 'Méthode non autorisée'}, status=405)

@csrf_exempt
def supprimer_donnees(request):
    if request.method == 'POST':
        # Effacez toutes les données du modèle Etudiant
        PremiereA.objects.all().delete()
        return JsonResponse({'message': 'Suppression réussie'})
 
    return JsonResponse({'error': 'Méthode non autorisée'}, status=405)