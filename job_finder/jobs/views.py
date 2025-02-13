from django.shortcuts import render, redirect
from django.views.generic import View

from .forms import NoteForm, PositionForm
from .models import Position


# Create your views here.
class PositionListView(View):
    def get(self, request):
        positions = Position.objects.filter(is_rejected=False).select_related().all()
        return render(request, 'jobs/positions-list.html',
                      context={'positions': positions})


class PositionDetailView(View):
    def get(self, request, position_id):
        position = Position.objects.get(pk=position_id)
        return render(request, 'jobs/position.html',
                      context={'position': position})


class PositionCreateView(View):
    def get(self, request):
        form = PositionForm()
        return render(request, 'jobs/position-form.html', context={'form': form})

    def post(self, request):
        form = PositionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('position_list')
        else:
            return render(request, 'jobs/position-form.html', context={'form': form})


class PositionUpdateView(View):
    def get(self, request, position_id):
        position = Position.objects.get(pk=position_id)
        form = PositionForm(instance=position)
        return render(request, 'jobs/position-form.html', context={'form': form, 'is_edit': True})

    def post(self, request, position_id):
        position = Position.objects.get(pk=position_id)
        form = PositionForm(request.POST, instance=position)
        if form.is_valid():
            form.save()
            return redirect('position_list')
        else:
            return render(request, 'jobs/position-form.html', context={'form': form, 'is_edit': True})

class NoteCreateView(View):
    def get(self, request, position_id):
        position = Position.objects.get(pk=position_id)
        form = NoteForm(initial={'position': position})
        return render(request, 'jobs/note-form.html', context={'form': form})

    def post(self, request, position_id):
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('position-detail', position_id=position_id)
        else:
            return render(request, 'jobs/note-form.html', context={'form': form})