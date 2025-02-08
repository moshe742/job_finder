from django.shortcuts import render
from django.views.generic import View
from .models import Position


# Create your views here.
class PositionListView(View):
    def get(self, request):
        positions = Position.objects.all().select_related()
        return render(request, 'jobs/positions-list.html', context={'positions': positions})