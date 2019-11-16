import uuid

from django.db import models


class Team(models.Model):
    team_id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                               editable=False)
    name = models.CharField(max_length=255)
    logo_uri = models.CharField(max_length=2048)
    club_state = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)


class Player(models.Model):
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
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    player_id = models.ForeignKey(Player, on_delete=models.CASCADE)
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)


class Matches(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    teams = models.ManyToManyField(Team)
    match_number = models.PositiveIntegerField()
    match_stadium = models.CharField(max_length=255)
    match_location = models.CharField(max_length=255)
    match_tournament = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)


class Points(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    teams = models.ManyToManyField(Team)
    points = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)
