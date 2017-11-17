from django.shortcuts import render
from . import models

# Create your views here.
def lobby(request, lobbyid):
    # If the room with the given lobbyid doesn't exist, automatically create it
    # upon first visit (a la etherpad).
    lobby, created = Lobby.objects.get_or_create(lobbyid=lobbyid)

    # We want to show the last 50 messages, ordered most recent-last
    messages = reversed(lobby.messages.order_by('-timestamp')[:50])

    return render(request, "lobbys/lobby.html", {'lobby':lobby,'messages':messages})
