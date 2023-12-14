from django.shortcuts import redirect, render
from .forms import ClientForm
from .models import RealEstate


def list_rentals(request):
    real_estates = RealEstate.objects.filter(is_rented=False)
    context = {'real_estates': real_estates}
    return render(request, 'list-rentals.html', context)


def form_client(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-rentals')
    return render(request, 'form-client.html', {'form': form})
