import uuid

from django.test import TestCase
from django.urls import reverse

from .models import Team, Player, PlayerHistory, Matches, Points


def _create_team(name, logo_uri='logo_uri', club_state='club_state'):
    team_id = uuid.uuid4()
    team = Team(team_id=team_id, name=name, logo_uri=logo_uri,
                club_state=club_state)
    team.save()
    return team_id, team


def _create_player(player_id=uuid.uuid4(), first_name="james",
                   last_name="vince", image_uri="http://example.com",
                   jersey_number=100, country="Earth"):
    player = Player(player_id=player_id, first_name=first_name,
                    last_name=last_name, image_uri=image_uri,
                    jersey_number=jersey_number, country=country)
    return player


def _create_match(id=uuid.uuid4(), match_number=1,
                  match_stadium="stadium", match_location="location",
                  match_tournament="match_tournament"):
    match = Matches(id=id, match_number=match_number,
                    match_stadium=match_stadium, match_location=match_location,
                    match_tournament=match_tournament)
    return match


class TeamModelTest(TestCase):
    def test_team_create(self):
        name = "Greatest team ever"
        logo_uri = "http://foo.bar"
        club_state = "Earth"
        team_id, team = _create_team(name, logo_uri=logo_uri,
                                     club_state=club_state)
        self.assertEqual(team_id, team.team_id)
        self.assertEqual(name, team.name)
        self.assertEqual(logo_uri, team.logo_uri)
        self.assertEqual(club_state, team.club_state)
        # Note: a test/assert related to many to many field 'players' has been
        # skipped


class PlayerModelTest(TestCase):
    def test_player_create(self):
        player_id = uuid.uuid4()
        first_name = "vince"
        last_name = "james"
        image_uri = "http://example.org"
        jersey_number = 10
        country = "Local"
        player = _create_player(player_id=player_id, first_name=first_name,
                                last_name=last_name, image_uri=image_uri,
                                jersey_number=jersey_number, country=country)
        player.save()
        self.assertEqual(player_id, player.player_id)
        # Note: a test/assert related to many to many field 'teams' has been
        # skipped
        self.assertEqual(first_name, player.first_name)
        self.assertEqual(last_name, player.last_name)
        self.assertEqual(image_uri, player.image_uri)
        self.assertEqual(jersey_number, player.jersey_number)
        self.assertEqual(country, player.country)


class PlayerHistoryModelTest(TestCase):
    def test_player_history_create(self):
        id = uuid.uuid4()
        player_id = uuid.uuid4()
        key = 'key'
        value = 'value'
        _ = Player(player_id=player_id, first_name="foo",
                   last_name="bar", image_uri="http://example.com",
                   jersey_number=7, country="UK")
        player_history = PlayerHistory(id=id, player_id=player_id, key=key,
                                       value=value)
        self.assertEqual(id, player_history.id)
        self.assertEqual(player_id, player_history.player_id)
        self.assertEqual(key, player_history.key)
        self.assertEqual(value, player_history.value)


class MatchesModelTest(TestCase):
    def test_match_create(self):
        id = uuid.uuid4()
        match_number = 1
        match_stadium = "Circle"
        match_location = "Earth"
        match_tournament = "World Cup"
        match = _create_match(id=id, match_number=match_number,
                              match_stadium=match_stadium,
                              match_location=match_location,
                              match_tournament=match_tournament)
        self.assertEqual(id, match.id)
        # Note: a test/assert related to many to many field 'teams' has been
        # skipped
        self.assertEqual(match_number, match.match_number)
        self.assertEqual(match_stadium, match.match_stadium)
        self.assertEqual(match_location, match.match_location)
        self.assertEqual(match_tournament, match.match_tournament)


class PointsModelTest(TestCase):
    def test_point_create(self):
        id = uuid.uuid4()
        point = 1
        points = Points(id=id, points=point)
        self.assertEqual(id, points.id)
        # Note: a test/assert related to many to many field 'teams' has been
        # skipped
        self.assertEqual(point, points.points)


class IndexViewTest(TestCase):
    def test_index(self):
        resp = self.client.get(reverse('cricpro:index'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'The Cricpro App')
        self.assertContains(resp, 'Teams List')
        self.assertContains(resp, 'Players List')
        self.assertContains(resp, 'Points table')
        self.assertContains(resp, 'No data available.')
        self.assertContains(resp, 'Matches')
        self.assertContains(resp, 'Set up a match')
        self.assertContains(resp, 'No match exist.')


class TeamsIndexViewTest(TestCase):
    def test_teams_index(self):
        resp = self.client.get(reverse('cricpro:teams_index'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Cricket Teams')


class TeamsDetailViewTest(TestCase):
    def test_teams_detail(self):
        team_id, team = _create_team('teams_detail_view_team')
        team.save()
        resp = self.client.get(reverse('cricpro:teams_detail', args=(team_id,)))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'teams_detail_view_team')
        self.assertContains(resp, 'Players list in this team:')
        self.assertContains(resp, 'Matches list for this team:')


class PlayersIndexViewTest(TestCase):
    def test_players_index(self):
        player = _create_player()
        player.save()
        resp = self.client.get(reverse('cricpro:players_index'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Cricket Players')
        self.assertContains(resp, 'Players List')


class PlayersDetailViewTest(TestCase):
    def test_players_detail(self):
        player = _create_player()
        player.save()
        resp = self.client.get(reverse('cricpro:players_detail',
                                       args=(player.player_id,)))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'james')
        self.assertContains(resp, 'Teams this player belongs to:')
        self.assertContains(resp, 'Other information about this player:')


class MatchesCreateTest(TestCase):
    def test_matches_create(self):
        _create_team('matches_create_team_1')
        _create_team('matches_create_team_2')
        resp = self.client.post(reverse('cricpro:matches_create'),
                                {'team_1': 'matches_create_team_1',
                                 'team_2': 'matches_create_team_2',
                                 'match_number': 13,
                                 'match_stadium': 'new_stadium',
                                 'match_location': 'new_location',
                                 'match_tournament': 'new_tournament',
                                 })
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Match # 13 created successfully')
        self.assertContains(resp, 'Please visit the')


class MatchesFixturesCreateTest(TestCase):
    def test_matches_fixtures_create(self):
        resp = self.client.get(reverse('cricpro:fixtures_create'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Tournament # %s created successfully' %
                            resp.context['tournament_no'])
        self.assertContains(resp, 'Please visit the')


class MatchesDetailViewTest(TestCase):
    def test_matches_detail(self):
        match = _create_match()
        match.save()
        team_id, team = _create_team('matches_create_team')
        team.save()
        match.teams.set([team])
        match.save()
        resp = self.client.get(reverse('cricpro:matches_detail',
                                       args=(match.id,)))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Welcome to the match number: '
                                  '%s' % match.match_number)
        self.assertContains(resp, 'Details:')
        self.assertContains(resp, 'Teams Playing:')
        self.assertContains(resp, '%s' % team.name)
        self.assertContains(resp, 'Match Number: %s' % match.match_number)
        self.assertContains(resp, 'Match Stadium: %s' % match.match_stadium)
        self.assertContains(resp, 'Match Location: %s' % match.match_location)
        self.assertContains(resp, 'Match Tournament: '
                                  '%s' % match.match_tournament)
        self.assertContains(resp, 'Setup another match')
