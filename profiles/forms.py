from django import forms

from profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileCreateForm(ProfileBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set placeholders for each field based on the field's name
        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = field_name.replace('_', ' ').capitalize()  # Replace underscores with spaces and capitalize