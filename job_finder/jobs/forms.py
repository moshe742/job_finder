from django.forms import ModelForm
from .models import (
    Position,
    Note
)


class PositionForm(ModelForm):
    class Meta:
        model = Position
        fields = '__all__'


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = '__all__'
