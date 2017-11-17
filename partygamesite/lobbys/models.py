from django.db import models
from django.contrib.auth import User
from django.utils import timezone

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Lobby(models.Model):
    lobbyid = models.SlugField(unique=True)
    game = models.ForeignKey(Game, related_name="lobby")

    def __unicode__(self):
        return self.lobbyid

class Message(models.Model):
    lobby = models.ForeignKey(Lobby, related_name='messages')
    user = models.ForeignKey(User)
    message = models.TextField()
    timestamp = models.DatetimeField(default=timezone.now, db_index=True)

    def __unicode__(self):
        return '[{timestamp}] {user}: {message}'.format(**self.as_dict())

    def as_dict(self):
        return {'handle': self.handle, 'message': self.message, 'timestamp': self.timestamp}
