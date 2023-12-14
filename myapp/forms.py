from django import forms
from .models import Client, RealEstate, RentalRegister


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class RealEstateForm(forms.ModelForm):
    real_estate = MultipleFileField()

    class Meta:
        model = RealEstate
        fields = "__all__"
        exclude = ("is_rented",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.__class__ in [forms.CheckboxInput, forms.RadioSelect]:
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class RentalRegisterForm(forms.ModelForm):
    start_date = forms.DateTimeField(
        widget=forms.DateInput(
            format="%d-%m-%Y",
            attrs={
                "type": "date",
            },
        )
    )
    end_date = forms.DateTimeField(
        widget=forms.DateInput(
            format="%d-%m-%Y",
            attrs={
                "type": "date",
            },
        )
    )

    class Meta:
        model = RentalRegister
        fields = "__all__"
        exclude = (
            "real_estate",
            "created_at",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
