from django import forms

from albums.models import Album


class AlbumBaseForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ('owner',)


class AlbumCreateForm(AlbumBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set placeholders for each field based on the field's name
        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = field_name.replace('_',
                                                                   ' ').capitalize()  # Replace underscores with spaces and capitalize


class AlbumEditForm(AlbumBaseForm):
    pass


class AlbumDeleteForm(AlbumBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['readonly'] = True
