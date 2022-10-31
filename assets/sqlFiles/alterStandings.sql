-- Active: 1667155008712@@nhlpredictions.mysql.database.azure.com@3306@nhlpredictions

SELECT * FROM player_statistics WHERE full_name = 'Brock Nelson';

ALTER TABLE standings
    ADD COLUMN home_games_played INT GENERATED ALWAYS AS (home_wins + home_losses + home_overtime_losses),
    ADD COLUMN road_games_played INT GENERATED ALWAYS AS (road_wins + road_losses + road_overtime_losses),
    ADD COLUMN points_pg FLOAT GENERATED ALWAYS AS (points / games_played),
    ADD COLUMN goals_for_pg FLOAT GENERATED ALWAYS AS (goals_for / games_played),
    ADD COLUMN goals_against_pg FLOAT GENERATED ALWAYS AS (goals_against / games_played),
    ADD COLUMN home_points_pg FLOAT GENERATED ALWAYS AS (home_points / home_games_played),
    ADD COLUMN home_goals_for_pg FLOAT GENERATED ALWAYS AS (home_goals_for / home_games_played),
    ADD COLUMN home_goals_against_pg FLOAT GENERATED ALWAYS AS (home_goals_against / home_games_played),
    ADD COLUMN road_points_pg FLOAT GENERATED ALWAYS AS (road_points / road_games_played),
    ADD COLUMN road_goals_for_pg FLOAT GENERATED ALWAYS AS (road_goals_for / road_games_played),
    ADD COLUMN road_goals_against_pg FLOAT GENERATED ALWAYS AS (road_goals_against / road_games_played)
;

