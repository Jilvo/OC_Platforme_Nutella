## Créez une plateforme pour amateurs de Nutella
## Project 8 of the Parcours développeur d'application python from OpenClassrooms
### Specification

## How can i access to the website ? 
On the project 8, the application was push with heroku on this link https://purbeurre-jilvo.herokuapp.com/

Or with the project 10 when i have to integrade my app on a unix server here http://51.15.236.212/

### How to run the program?
Follow the different steps :

### Setup
You need to download the django framework : 
```bash
pip install django
```
If you are on MacOS, or Linux : 
```bash
sudo apt-get install -y python3-pip
sudo apt-get install -y \
    python3-numpy libav-tools libsdl-image1.2-dev \
    libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev libsdl1.2-dev \
    libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev \
    libfreetype6-dev
sudo pip3 install -q django
```
### Installation
 ```
pip install -r OC_Platforme_Nutella/requirements.txt
```

### Running
Now you can run the app with :
```
python manage.py runserver
```
### Testing 
```
python manage.py test catalog/test/
```
## Versioning :
V0.1 Creation of the home page

V0.2 Adding sign in and sign up pages,starting with the authentification of the users

V0.3 Create postgresl_db, connect to it with django

V0.4 Create the models and the script to fill in the DB

V0.5 End of the script for adding products in the DB, create a "base.html" so i can split my code more easily

V0.6 Create a result page for the product we are looking for

V0.7 Set up the register view

V0.8 Starting tests, Set up the connection and the register for the user, order the substitute 

V0.9 Create the function in order to add favorits,build the favorit's page, so we can see the favorits

V0.9.1 Black library, flake8 library, make a route with selenium

V1.0 Test endend

V1.1 Integration with Unix Server

## Author and Contribution :
I built this program as part of an formation on OpenClassrooms. Therefore every *pull request* will be refused. Insted you can open an *issue* to signal a *bug*, a typographical error or just for give me an advice

### DjangoAuthenticationApp     
[![Build Status](https://travis-ci.com/Jilvo/OC_Platforme_Nutella.svg?branch=master)](https://travis-ci.com/Jilvo/OC_Platforme_Nutella)
