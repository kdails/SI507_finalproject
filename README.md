# Project Title

Kara Dailey - Scraping NPS, caching, creating a CSV and Database to interface with using Flask.

[Link to this repository](https://github.com/kdails/final_project_checkin)

---

## Project Description

<h2>This project for SI507 requires that you have python 3.7, Beautiful Soup, SQLite and others that provides opportunity to interact with scraped website data to aggregate it, read and write it in an organized CSV. </h2>
<h3>After running, this program will create 3 new files - a SQLite database (allstateparks_info.sqlite) , a CSV (nps_parks.csv) and a json cache file (nps_cache.json). In order for this project to work properly, please refer to the required list of dependencies in requirements.txt and pip-install all dependencies to a virtual environment within the project folder for this application to run.</h3>

<h4> Additionally, there's a soon to be(not-finshed yet) but in progress Flask file defining flask applications that will build upon the SQLAlchemy database that has been created by the SI507project_tools file.</h4>

<h4> Over the course of the next week, I plan on spending time making the Flask interface for this project simple and easy to use and define paths for them too - so far i've considered the following paths listed below under "Routes in this application"  </h4>

<h4> Also included for this check-in is a test file that tests for two major parts of this project assignment, the database as well as the CSV correctness.

## How to run

1. First, you should ...install all requirements with `pip install -r requirements.txt`)
2. Second, you should run `python SIproject_tools.py`
3. If you want to run the test file, do so after the `python SIproject_tools.py` file is run because the output of that file ( database and csv) influences the success of the test.)

## How to use

1. So far we don't have anything super useful, but if you run the SI507_project_tools file, you'll see the scraped data from nps.gov get transformed into a database and csv file.
2. My next moves ater this check in are solidify the routes which are tentatively listed below!

## Routes in this application

Interface description
- Route 1: /all_parks   →   
  This page will show all of the parks in the country by name, location as well as a short description!

- Route 2: /park_search/<input> →   
  This page will show relative parks that have a certain search term ( user input) in their short description.

- Route 3: /park_by_state/<input>  →   
  This page will show the information on parks sorted by state. The user will search and input a state abbreviation ex: “ma”  to see all parks in Massachusetts.


## How to run tests
1. First - cd into this repository after cloning to your machine.
2. Second - run the SI507_project_tests file. 

## In this repository:
- SI507project_tools.py - where the scraping, caching and csv creation happens
- db_setup.py - where the classes for the database creation are set up and is initialized. 
- requirements.txt - current requirements from my virtual environment needed in order to run this program properly.
- SI507project_tests.py - must be run AFTER the tools file is run.
- ReadMe.md - this readme file with all the know-how information on this project.
- IMG_4873.JPG - A picture of my Database as it currently stands and how I designed it to begin with.
- nps_parks.csv - the CSV that is included just for show and my own reference - if you want to cache your own, just delete this file after you've finished cloning this repository and run the tools file in your terminal! 

---
## Code Requirements for Grading
Please check the requirements you have accomplished in your code as demonstrated.
- [x] This is a completed requirement.
- [ ] This is an incomplete requirement.

Below is a list of the requirements listed in the rubric for you to copy and paste.  See rubric on Canvas for more details.

### General
- [X] Project is submitted as a Github repository
- [ ] Project includes a working Flask application that runs locally on a computer
- [X] Project includes at least 1 test suite file with reasonable tests in it.
- [X] Includes a `requirements.txt` file containing all required modules to run program
- [X] Includes a clear and readable README.md that follows this template
- [X] Includes a sample .sqlite/.db file
- [X] Includes a diagram of your database schema
- [X] Includes EVERY file needed in order to run the project
- [ ] Includes screenshots and/or clear descriptions of what your project should look like when it is working

### Flask Application - soon to exist!
- [ ] Includes at least 3 different routes
- [ ] View/s a user can see when the application runs that are understandable/legible for someone who has NOT taken this course
- [ ] Interactions with a database that has at least 2 tables
- [ ] At least 1 relationship between 2 tables in database
- [ ] Information stored in the database is viewed or interacted with in some way

### Additional Components (at least 6 required)
- [O] Use of a new module
- [ ] Use of a second new module
- [ ] Object definitions using inheritance (indicate if this counts for 2 or 3 of the six requirements in a parenthetical)
- [X] A many-to-many relationship in your database structure
- [ ] At least one form in your Flask application
- [O] Templating in your Flask application
- [O] Inclusion of JavaScript files in the application
- [ ] Links in the views of Flask application page/s
- [ ] Relevant use of `itertools` and/or `collections`
- [X] Sourcing of data using web scraping
- [ ] Sourcing of data using web REST API requests
- [X] Sourcing of data using user input and/or a downloaded .csv or .json dataset
- [X] Caching of data you continually retrieve from the internet in some way

### Submission
- [X] I included a link to my GitHub repository with the correct permissions on Canvas! (Did you though? Did you actually? Are you sure you didn't forget?)
- [ ] I included a summary of my project and how I thought it went **in my Canvas submission**!
