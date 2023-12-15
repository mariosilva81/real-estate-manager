from django.shortcuts import redirect, render
from .forms import ClientForm, RealEstateForm, RentalRegisterForm
from .models import RealEstate, RealEstateImage


def list_real_estates(request):
    real_estates = RealEstate.objects.filter(is_rented=False)
    context = {"real_estates": real_estates}
    return render(request, "list-real-estates.html", context)


def form_client(request):
    form = ClientForm()
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list-real-estates")
    return render(request, "form-client.html", {"form": form})


def form_real_estate(request):
    form = RealEstateForm()
    if request.method == "POST":
        form = RealEstateForm(request.POST, request.FILES)
        if form.is_valid():
            real_estate = form.save()
            files = request.FILES.getlist("real_estate")
            if files:
                for file in files:
                    RealEstateImage.objects.create(real_estate=real_estate, image=file)
            return redirect("list-real-estates")
    return render(request, "form-real-estate.html", {"form": form})


def form_rental(request, real_estate_id):
    real_estate = RealEstate.objects.get(id=real_estate_id)
    form = RentalRegisterForm()
    if request.method == "POST":
        form = RentalRegisterForm(request.POST)
        if form.is_valid():
            rental_form = form.save(commit=False)
            rental_form.real_estate = real_estate
            rental_form.save()
            real_estate.is_rented = True
            real_estate.save()
            return redirect("list-real-estates")
    context = {"form": form, "real_estate": real_estate}
    return render(request, "form-rental.html", context)
