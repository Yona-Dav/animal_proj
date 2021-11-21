from django.shortcuts import render
import json
from collections import defaultdict
# Create your views here.

def animal(request,animal_id):
    with open('data.json') as f:
        data = json.load(f)
    selected_animal = None
    for animal in data['animals']:
        if animal['id']== animal_id:
            selected_animal = animal
    return render(request, 'animal.html', {'animal':selected_animal})

def family(request, family_id):
    with open('data.json') as f:
        data = json.load(f)
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



