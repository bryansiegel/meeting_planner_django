from django.shortcuts import get_object_or_404, render, redirect

from .models import Meeting, Room
from .forms import MeetingForm


def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})


def rooms(request):
    room = Room.objects.all()
    return render(request, "meetings/rooms.html", {"room": room})


def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = MeetingForm()
    return render(request, "meetings/new.html", {"form": form})
