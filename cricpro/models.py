import uuid

from django.db import models


class Team(models.Model):
    team_id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                               editable=False)
    name = models.CharField(max_length=255)
    logo_uri = models.CharField(max_length=2048)
    club_state = models.CharField(max_length=255)


class Player(models.Model):
    player_id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                                 editable=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    image_uri = models.CharField(max_length=2048)
    jersey_number = models.PositiveIntegerField()
    country = models.CharField(max_length=255)


class PlayerHistory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    player_id = models.ForeignKey(Player, on_delete=models.CASCADE)
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255)


class Matches(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    match_number = models.PositiveIntegerField()
    match_stadium = models.CharField(max_length=255)
    match_location = models.CharField(max_length=255)
    match_tournament = models.CharField(max_length=255)
    match_team_1 = models.CharField(max_length=255)
    match_team_2 = models.CharField(max_length=255)


class Points(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    points = models.PositiveIntegerField()
    points_team_1 = models.CharField(max_length=255)
    points_team_2 = models.CharField(max_length=255)