from channels import Group
from channels.sessions import channel_session
from .models import Lobby
import json

@channel_session
def ws_connect(message):
    try:
        prefix, lobbyid = message['path'].strip('/').split('/')
        lobby = Lobby.objects.get(lobbyid=lobbyid)
    except:
        return {'close':True}
    Group('chat-' + lobbyid, channel_layer=message.channel_layer).add(message.reply_channel)
    message.channel_session['lobby'] = lobby.lobbyid
    return {'accept':True}

@channel_session
def ws_receive(message):
    lobbyid = message.channel_session['lobby']
    lobby = Lobby.objects.get(lobbyid=lobbyid)
    data = json.loads(message['text'])
    m = room.messages.create(user=data['user'], message=data['message'])
    Group('chat-' + lobbyid).send({'text': json.dumps(m.as_dict())})

@channel_session
def ws_disconnect(message):
    lobbyid = message.channel_session['lobby']
    Group('chat-' + lobbyid).discard(message.reply_channel)
