# Flask homework

This is a homework project that uses Flask framework to perform the following tasks:

## PATH: /names/

This endpoint returns the number of unique artists in the tracks table.

## PATH: /tracks/

This endpoint returns the total number of tracks in the tracks table.

## PATH: /tracks/<genre>

This endpoint takes a genre parameter and returns the number of tracks with that genre in the tracks table.

## PATH: /tracks/seconds

This endpoint returns a list of all track titles and their corresponding durations in seconds from the tracks table.

## PATH: /tracks/statistics/

This endpoint returns the average and total duration of all tracks in seconds from the tracks table.

## Special features

This web app contains two management commands:

init-db: uses the file schema.sql to add a schema to a database.

load-fixtures: uses the file fixtures.sql to add fixtures to initialized table.
