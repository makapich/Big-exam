from django.shortcuts import get_object_or_404, redirect, render

from .forms import PersonForm, TriangleForm
from .models import Person


def triangle(request):
    hypotenuse = None
    if "Submit" in request.GET:
        user_form = TriangleForm(request.GET)

        if user_form.is_valid():
            leg1 = user_form.cleaned_data['leg1']
            leg2 = user_form.cleaned_data['leg2']
            hypotenuse = round((((leg1 ** 2) + (leg2 ** 2)) ** 0.5), 2)

            user_form = TriangleForm()
    else:
        user_form = TriangleForm()

    return render(request, 'triangle/triangle.html', {'form': user_form, 'hypotenuse': hypotenuse})


def person_list(request):
    users = Person.objects.all()
    return render(request, 'triangle/user_list.html', {'users': users})


def person_register(request):
    if request.method == 'POST':
        user_form = PersonForm(request.POST)

        if user_form.is_valid():
            user_form.save()
            return redirect('triangle:person')

    else:
        user_form = PersonForm()

    return render(request, 'triangle/user_register.html', {'form': user_form})


def person_update(request, pk):
    obj = get_object_or_404(Person, pk=pk)

    if request.method == 'POST':
        user_form = PersonForm(request.POST, instance=obj)

        if user_form.is_valid():
            obj = user_form.save()
            return redirect('triangle:person')

    else:
        user_form = PersonForm(instance=obj)

    return render(request, 'triangle/user_update.html', {'form': user_form, 'obj': obj})
