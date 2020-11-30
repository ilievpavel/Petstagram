from django.shortcuts import render, redirect

from common.models import Comment
from .forms.comment_form import CommentForm
from .forms.pet_form import PetForm
from .models import Pet, Like


def pet_list(request):
    context = {
        'pets': Pet.objects.all()
    }

    return render(request, 'pet_list.html', context)


def pet_detail(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'pet': pet,
            'form': CommentForm(),
        }

        return render(request, 'pet_detail.html', context)
    else:
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = Comment(text=form.cleaned_data['text'])
            comment.pet = pet
            comment.save()

            return redirect('pet_detail', pk)

        context = {
            'pet': pet,
            'form': form,
        }

        return render(request, 'pet_detail.html', context)


def persist_pet(request, pet, template):
    if request.method == 'GET':
        form = PetForm(instance=pet)

        context = {
            'form': form,
            'pet': pet,
        }
        return render(request, f'{template}.html', context)
    else:
        form = PetForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet_detail', pet.pk)

        context = {

            'form': form,
            'pet': pet,
        }

        return redirect(request, f'{template}.html', context)


def pet_create(request):
    pet = Pet()
    return persist_pet(request, pet, 'pet_create')


def pet_edit(request, pk):
    pet = Pet.objects.get(pk=pk)
    return persist_pet(request, pet, 'pet_edit')


def pet_delete(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'pet': pet
        }
        return render(request, 'pet_delete.html', context)
    else:
        pet.delete()
        return redirect('pet_list')


def pet_like(request, pk):
    pet = Pet.objects.get(pk=pk)
    like = Like()
    like.pet = pet
    like.save()

    return redirect('pet_detail', pk)
