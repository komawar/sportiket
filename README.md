# sportiket
A cricket teams, players, matches and points app

This is a Django based project. The models, views, templates and tests have been written as per the framework.

A couple of migrations scripts have been provided to setup the tables.

Most of the views are readonly. One form exists for match creation as per the assignment direction. Also the fixtures/tournament creation is automated/without user input.

Settings have been made less permissible (restrict access to localhost). If this is to be deployed to another server, this needs to be changed. Debug has been set to False too.

Admin panel has access to all models so this app can be tested using some sample data creation there too.

Tests have been included for views and models. Coverage report as per command `coverage run --source='.' manage.py test cricpro` can be generated accordingly.

Local run of the `coverage report` shows:
TOTAL                                             343     25    93%


To access the app (for example on localhost):
  * front page: http://127.0.0.1:8000/cricpro/
  * teams list: http://127.0.0.1:8000/cricpro/teams/
  * team detail: http://127.0.0.1:8000/cricpro/teams/<team_uuid>
  * players list: http://127.0.0.1:8000/cricpro/players/
  * player detail: http://127.0.0.1:8000/cricpro/players/<player_uuid>
  * setup a match: http://127.0.0.1:8000/cricpro/matches/
  * create a tournament: http://127.0.0.1:8000/cricpro/matches/fixtures
