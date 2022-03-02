# bhill28_Milestone2

Heroku Link: [ ]


## Title of Project: Milestone 2 


## General Info: 
The goal of this assignment is to create a website that can store registered user's data information into a established database and the information should be accessible for the server to "GET" or "POST" the stored user data.

In preparation for this project, I wrote the initial lines of Python code on the VS code editor to employ the workings of Python’s Flask to build a startup webpage. Python black was useful in cleaning up the code and making it more readable. In order to dynamically fetch data from the required API keys (TMDB and Wikipedia), it was vital to use several imports as well as modules including Json, requests, Flask, redirect, ,render_template, url_for, session, flash, random, flask's SQLAlchemy and of course from dotenv import find_dotenv, load_dotenv to load the hidden keys to be able to read and store the data to load onto the webpage. Github, as a cloud based hosting service platform, is where I commited my files. I aslo employed the Heroku database url in order to create and establish a database to store users. Heroku also assisted in building, running as well as operating the final web application.

## Setup 
To run this project, you will need to have these installed or implemented in code: 
    - Flask  
    - Python  
    - SQLAlchemy
    - Heroku (for deployment and database) 
    - API_KEY (TMDB)
    - Wikimedia api key
    - dotenv 
    - Python requests 

 Required Files:  
    - app.py
    - model.py
    - home.html
    - login.html
    - register.html
    - search.html
    - trivia.html
    - trailer.html
    - .env (stores the api keys)
    - .gitignore (hides .env file)
    - requirements.txt
    - README.md
    - Procfile 

## Technologies:
    - Python 2.7.16 (or higher). Preferably Python 3.10.2
    - Flask 2.0.2
    - Werkzeug 2.0.2

## Known problems:
One problem that has persisted is that my webpage will not reload new results. I tried every solution I can think of and nothing has worked in the end. I also had an difficulty  with trying to establish a search feature on the webpage that will return movies results based on user input terms. 

## Overall Experience:
Querying the database was a lot more challenging then expected because I kept getting unexpected errors. I found it easier to create html forms that recieve user input than expected. Overall, I have learned a lot of new skills but it took quite a bit of time putting all of the elements together. 

