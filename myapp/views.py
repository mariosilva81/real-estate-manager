from django.shortcuts import render
from myapp.models import RealEstate


def list_rentals(request):
    real_estates = RealEstate.objects.filter(is_rented=False)
    context = {
        'real_estates': real_estates
    }
    return render(request, 'list_rentals.html', context)
