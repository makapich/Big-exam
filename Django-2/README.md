# Second Django Homework

This repository contains second Django homework project.

## Features

### Books app

* Contains cached views on Author list and book list.
* Contains management command which populates all db models. Used generators to make the command the most optimised.
* Contains all needed views for CRUD (both class-based and functions-based)

### Celery example app

* Contains a parsing task which is being performed every 2 hours by celery beat. The function uses BS4 to parse the page and save the data to the db.
The function scrapes a quote and saves it into db. If the quote was saved earlier - the scraper scrapes the next one until it reaches the last quote on the last page
of a website. After the last quote was scraped - admin receives an email about finished scraping procedure.
