from django.contrib import admin

from .models import Position
from .models import Note


# Register your models here.
admin.site.register(Position)
admin.site.register(Note)
