"""job_finder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from jobs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('position/<position_id>/note', views.NoteCreateView.as_view(), name='add-note'),
    path('position/<position_id>/edit', views.PositionUpdateView.as_view(), name='position-update'),
    path('position/<position_id>', views.PositionDetailView.as_view(), name='position-detail'),
    path('position-add', views.PositionCreateView.as_view(), name='add-position'),
    path('position/', views.PositionListView.as_view(), name='position-list'),
    path('company/', views.CompanyListView.as_view(), name='company-list'),
]
