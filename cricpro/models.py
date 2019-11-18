import uuid

from django.db import models


class Team(models.Model):
    """Model class for the cricpro apps Teams
    """
    class Meta:
        verbose_name_plural = "Teams"
    team_id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                               editable=False)
    name = models.CharField(max_length=255)
    logo_uri = models.CharField(max_length=2048)
    club_state = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)


class Player(models.Model):
    """Model class for the cricpro apps Player
    """
    class Meta:
        verbose_name_plural = "Players"
    player_id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                                 editable=False)
    teams = models.ManyToManyField(Team)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    image_uri = models.CharField(max_length=2048)
    jersey_number = models.PositiveIntegerField()
    country = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)


class PlayerHistory(models.Model):
    """Model class for the cricpro apps PlayerHistory. This is where the
    extra/miscellaneous information about the player will be stored
    """
    class Meta:
        verbose_name_plural = "PlayerHistory"
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)


class Matches(models.Model):
    """Model class for the cricpro apps Matches
    """
    class Meta:
        verbose_name_plural = "Matches"
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    teams = models.ManyToManyField(Team)
    match_number = models.PositiveIntegerField(unique=True)
    match_stadium = models.CharField(max_length=255)
    match_location = models.CharField(max_length=255)
    match_tournament = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)


class Points(models.Model):
    """Model class for the cricpro apps Points
    """
    class Meta:
        verbose_name_plural = "Points"
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    team = models.OneToOneField(Team, on_delete=models.CASCADE)
    points = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)
