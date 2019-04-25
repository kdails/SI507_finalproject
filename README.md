# Project Title

Kara Dailey - Scraping NPS, caching, creating a CSV and Database to view with using Flask.

[Link to this repository](https://github.com/kdails/final_project_checkin)

---

## Project Description

<h2>This project for SI507 requires that you have python 3.7, Beautiful Soup, SQLite and others that provides opportunity to interact with scraped website data to aggregate it, read and write it in an organized CSV. </h2>
<h3>After running, this program will create 3 new files - a SQLite database (allstateparks_info.sqlite) , a CSV (nps_parks.csv) and a json cache file (nps_cache.json). In order for this project to work properly, please refer to the required list of dependencies in requirements.txt and pip-install all dependencies into a virtual environment within the project folder for this application to run.</h3>

<h4> Additionally, after running the tools file which caches, scrapes and builds the database, you can now run the app.py file. This app.py file is a Flask file defining flask applications that will build upon the SQLAlchemy database that has been created by the SI507project_tools file.</h4>

<h4> Over the past few weeks, I've made the Flask interface for this project simple and easy to use and presents data and information in a way that is more understandable than a messy JSON file and additionally uses modules that are new to me like WTForms as well as Flask-Table which you will need to install with the requirements.txt.  These paths are defined and can be reached at any page of the application - 've considered the following paths listed below under "Routes in this application"  </h4>

<h4> Also included is a test file that tests for two major parts of this project assignment, the database as well as the CSV correctness.

## How to run

Before doing anything, download this entire project file. Then you must create a virtual environment within the project folder. Now you should move on to the following steps:

1. First, you should ...install all requirements with `pip install -r requirements.txt`)
2. Second, you should run `python SIproject_tools.py`
3. If you want to run the test file, do so after the `python SIproject_tools.py` file is run because the output of that file ( database and csv) influences the success of the test.)
4. Now, in your shell again type a different command: `python app.py`
5. This will now throw back information into the terminal about the port for the application - all you need to do now is copy the following URL into your browser and press enter:  http://localhost:5000/ - you'll get a greeting and options to view data using organization from different modules depending on the button you'll press.


## How to use

1. You'll notice that if you run the SI507_project_tools file, you'll see the scraped data from nps.gov get transformed into a JSON, database and csv file! 
2. If you've run the app.py file with python `python SIproject_tools.py`  you'll be able to follow a few different routes, specifically the ones below.
3. Once you
3. You won't need to type anything into the browser, the app can be completely navigated through with buttons. For route information, see below: 
4. To close the 

## Routes in this application

Interface description
- Route 1: /   →   
  This page is the welcome screen, it's just for an overview and blurb about the app with a nice national parks image from Yellowstone featuring some Bison.

- Route 2: /all →   
  This page will show all scraped parks from the Park database table with abbreviations populated from the State table. Image featured is from Joshua Tree National Park.

- Route 3: /allstateinfo  →   
  This page will show the information on all state parks with data from the State table. You can copy and paste the hyperlink into your browser to learn more about the state and what's available in terms of national parks within it. The image featured is of Grand Canyon in the winter.
 
- Route 4: /search  →
  This page acts as a navigation page. You're able to get anywhere on the site from this centralized location. It additionally features a dropdown of the columns in the Park table which the user can look at. I wanted to see what I could do with a new module, so I tried my hand at wtform to showcase the information. 

- Route 5: /table  →   
  This page was tough for me to figure out. I wanted to be able to present the data for the parks in something OTHER than an organized string print like I did in /all. I was finally able to present the data in a database-like structure using a module I've never used before so the user didn't have to download a database viewing software and could view it locally with the help of the flask_table module. 

## How to run tests
1. First - cd into this repository after cloning to your machine.
2. Second - run the SI507_project_tests file. 

## In this repository:
- SI507project_tools.py - where the scraping, caching and csv creation happens
- db_setup.py - where the classes for the database creation are set up and is initialized. 
- requirements.txt - current requirements from my virtual environment needed in order to run this program properly.
- SI507project_tests.py - must be run AFTER the tools file is run.
- READMe.md - this readme file with all the know-how information on this project.
- IMG_4873.JPG - A picture of my Database as it currently stands and how I designed it to begin with.
- nps_parks.csv - the CSV that is included just for show and my own reference - if you want to cache your own, just delete this file after you've finished cloning this repository and run the tools file in your terminal! 
- db.py is where the SQLAlchemy is called. 
- models.py is a file that created a model for the app to use in querying data from the database. It took me a long time to figure out that SQLAlchemy and SQLAlchemy flask were so different in many ways, and especially in the way that SQLAlchemy Flask sets up models for it's databases, so that's why this file exists. 
-TEMPLATES FOLDER includes all of the templates and html files that are the structure of the app interface. these include the following 
  - _formhelpers.html which throws form error help if needed, this uses mainly JINJA to template and throw errors if needed. 
  - all.html which is where the all route leads mentioned above. It uses JINJA to template the information for each park as well as call the CSS file.  
  - allstates.html is where the all states route leads to and provides info and links to state information.and uses JINJA to template the information for each state as well as call the CSS file.  
  - index.html is the greeting page of the app and uses JINJA call the CSS file. 
  - results.html is where the table is created and uses JINJA to template the table as well as call the CSS file.
  - searchform.html is where all of the buttons are and can be navigated to. This page additionally offers a form drop view of the table column names for the Parks table. 
  - 


---
## Code Requirements for Grading
Please check the requirements you have accomplished in your code as demonstrated.
- [x] This is a completed requirement.
- [ ] This is an incomplete requirement.

Below is a list of the requirements listed in the rubric for you to copy and paste.  See rubric on Canvas for more details.

### General
- [X] Project is submitted as a Github repository
- [X] Project includes a working Flask application that runs locally on a computer
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
