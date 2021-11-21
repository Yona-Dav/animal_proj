from django.shortcuts import render
import json
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

# Create your views here.
def get_data():
    with open('data.json') as f:
        return json.load(f)

def animal(request,animal_id):
    data = get_data()
    selected_animal = None
    selected_image = None
    for animal in data['animals']:
        if animal['id'] == animal_id:
            selected_animal = animal
            selected_image = animal['image']
    return render(request, 'animal.html', {'animal':selected_animal, 'image':selected_image})

def family(request, family_id):
    data = get_data()
    selected_family =None
    list_animal = {}
    for family in data['families']:
        if family['id'] == family_id:
            selected_family = family['name']

    for animal in data['animals']:
        if animal['family'] == family_id:
            if family_id not in list_animal:
                list_animal[family_id] = animal['name']
            else:
                list_animal[family_id] += animal['name']+""

    context = {'animal':list_animal, 'family':selected_family}
    return render(request, 'family.html', context)

def animals(request):
    data = get_data()
    animals = {}
    for animal in data['animals']:
        animals[animal['id']]= animal['name']
    return render(request, 'animals.html', {'animals': animals})


