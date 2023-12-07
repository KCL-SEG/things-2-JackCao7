from django.shortcuts import render, redirect
from .forms import ThingForm
from .models import Thing
def home(request):
    if request.method == 'POST':
        form = ThingForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            description = form.cleaned_data.get('description')
            quantity = form.cleaned_data.get('quantity')
            thing = Thing.objects.create(name=name, description=description, quantity=quantity)
            thing.save()
            return redirect('home')
    form = ThingForm()
    return render(request, 'home.html', {'form': form})
