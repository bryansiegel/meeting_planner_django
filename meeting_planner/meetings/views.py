from django.shortcuts import get_object_or_404, render

from meetings.models import Meeting


def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})
