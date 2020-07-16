from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse,JsonResponse
# Create your views here.

from client.models import Category, Food ,Event ,Reason,Info,Reservation
from client.forms import ReservationForm

CATEGORIES = [
     {
          'id':1,
          'name' : "Categorie name 1",
          'description' : "Categorie description 1",
     },
     {
          'id':2,
          'name' : "Categorie name 2",
          'description' : "Categorie description 2",
     },
     {
          'id':3,
          'name' : "Categorie name 3",
          'description' : "Categorie description 3",
     }
]

MENUS = [
     {
          'name':"Plat 1",
          'description': "Description 1",
          'image' : 'https://s3.amazonaws.com/medias.recettesdici.com/recettes-photos/p/pizza-aux-3-fromages/pizza-aux-3-fromages-1-1200x630.jpg',
          'category': CATEGORIES[0],
          'price': 1501,
     },
      {
          'name':"Plat 2",
          'description': "Description 2",
          'image' : 'https://s3.amazonaws.com/medias.recettesdici.com/recettes-photos/p/pizza-aux-3-fromages/pizza-aux-3-fromages-1-1200x630.jpg',
          'category': CATEGORIES[1],
          'price': 1502,
     },
       {
          'name':"Plat 3",
          'description': "Description 3",
          'image' : 'https://s3.amazonaws.com/medias.recettesdici.com/recettes-photos/p/pizza-aux-3-fromages/pizza-aux-3-fromages-1-1200x630.jpg',
          'category': CATEGORIES[2],
          'price': 1503,
     }
]

REASONS_TO_CHOOSE = [
     {'name' : "Nom 1",'description' : "Description 1"},
     {'name' : "Nom 2",'description' : "Description 2"},
     {'name' : "Nom 3",'description' : "Description 3"},
]

TESTIMONIALS = [
     {
          'client':{
               'name':"Richard Bathiebo",
               'profession': "Web developer",
          },
          'description' : "aaaaaaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaa aaaaaaaaaaaaaaaaaa",
     },
     {
          'client':{
               'name':"Richard Bathiebo",
               'profession': "Web developer",
          },
          'description' : "bbbbbbbbbbbbbbbbbbbbbbbbbbbbb bbbbbbbbbbbbbbb bbbbbbbbbb",
     },
     {
          'client':{
               'name':"Richard Bathiebo",
               'profession': "Web developer",
          },
          'description' : "ccccccccccccccc cccccccccccccccccccccc ccccccccccccccccccc",
     }
]

INFOS = {
          'location': "Dakar,Senegal Sacré coeur 3",
          'openTime': ["Lundi - Samedi","10h00 - 22h30"],
          'email' : "restaurantly@gmail.com",
          'phoneNumber': "+221 78 159 78 69",
     }

EVENTS = [
     {
          'name':"Fêtes d'anniversaire",
          'price':15000,
          'description': "Fêtes d'anniversaireFêtes d'anniversaireFêtes d'anniversaireFêtes d'anniversaireFêtes d'anniversaire",
          'image' : "",
     },
]
GALERIE = [
     {},{},{},{},
     {},{},{},{},
]

CHEFS = [
     {
          'name':"Richard ",
          'poste':"Chef numéro 1 (plats Africains)"
     },
     {
          'name':"Lucas ",
          'poste':"Chef numéro 2 (plats Européens)"
     }
]

def home(request):
     reservationForm = ReservationForm()
     
     return render(request,"home.html",{
                                        'CATEGORIES':Category.objects.all(),
                                        'MENUS' : Food.objects.all(),
                                        'REASONS_TO_CHOOSE':Reason.objects.all(),
                                        'TESTIMONIALS':TESTIMONIALS,
                                        'INFOS':Info.objects.first(),
                                        'EVENTS':Event.objects.all(),
                                        'GALERIE':GALERIE,
                                        'CHEFS':CHEFS,
                                        'ReservationForm':reservationForm
                                        })

def makeReservation(request):
     print("Reservation demande")
     if request.method == 'POST':
          form = ReservationForm(request.POST)
          if form.is_valid():
               print(form.cleaned_data)
               obj = ReservationForm(form.cleaned_data)
               obj.save()
               
               return JsonResponse(data={
                    "message":"Quel succès ! Votre Reservation a bien été prise en compte",
                    "status":201,
               })
          else:
               return JsonResponse(data={
                    "message":"Il y'a des erreurs dans le formulaire",
                    "status":400,
                    "formError":form.errors
               })
               
    