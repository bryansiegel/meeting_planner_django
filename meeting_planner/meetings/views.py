from django.shortcuts import get_object_or_404, render

from meetings.models import Meeting, Room


def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})

def rooms(request):
    room = Room.objects.all()
    return render(request, "meetings/rooms.html", {"room": room})
