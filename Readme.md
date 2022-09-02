$ Welcome to this spav project $
## I would like to thank Prof. Dr. Minakshi Jain (Director SPAV) for giving me this oppertunity to work for this institute of national importance, whos encuragement and good leadership inspired me to work harder as she working. #
##

## Project Details ##
- This project is the techanical solution to minimize and optimize the most of the techanical work of the SPAV by Creating. 
-Dynamic Website to provide information to the students and public. 
-Giving admin control to administrative staff for managing CRUD operation in the website. 
-
-
## Project Details ##

## Techonology Used ##
- HTML - For Structuring the web page. 
- CSS - To Style the Web Page 
- Bootstrap 5 - As a CSS library for making Website Responsice and Mobile Phone Fraindly. 
- Python - As a Backend Programminng Language. 
- Django - As a Python web Framework
- Git - For Version Control
- Heroku - As a Server 
- Other Dependency used, refer - requirements.txt file
## Techonology Used ##

## Installation Guide ##
Step 01:
- Create a folder and open the terminal in it. 
Step 02:
- Create a virtial enviroment $ python -m venv venv
- Activate the virtual Enviroment $ venv\scripts\activate
- Clone this git repo ~ git clone https://github.com/ingeniousabhinavg/spaav.git
- Run $ cd projectspav
- Run $ python manage.py makemigrations
- Run $ python manage.py migrate
- Run $ python manage.py createsuperuser
- Run $ puthon manage .py runserver

### Operations
- Now go to the development server and access the website 
- To make changes in the website go to url -- Developmentserver/admin 
  and login with the admin account you have created earlier. 
#### Enjoy the Website  #### 

## How to Add this website on the server ##

##### I have explained the deployment process for the herku 
Step 01:
- create a heroku account
- create a app with {app_name}

Step 02:  
- open the project folder 
- $ cd projectspav
- Open the terminal 
- $ heroku login
- $ git init 
- $ git remote:{app_name}
- $ git add .
- $ git commit -am "Your Commit"
- $ git push heroku master 
