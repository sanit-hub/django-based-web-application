# django-based-web-application
A django based project front end as html css
This is a main django based project on workshop automation.it help to reduce fileworks.it also reduce the workload too.

# Extra modules required

1) python required latest version

2) you can install this modules using pip command on command prompt.
   pip install django
   pip install psycopg2
   pip install pillow(if pillow not installed)
   Ensure that all the followig python modules are installed using "pip list" command

3) you need to download postgresql server PgAdmin for this project and you need to create a data base named wheelzone1 for using this project



# Running of the project

Also while running this project for first time you need a open the project folder in command prompt .once its opens you need to setup your database.
step 1:apply new migrations

command: python manage.py makemigration (you need to crate a data base named wheelzone1  on postgre sql PgAdmin before using the commands)
python manage.py migrate

step2:you need to create superuser
command:python manage.py createsuperuser 
enter gmaiil and any password.

step3:after creating super user you can run your project
command:python manage.py runserver

once the command runs open the locahost adress and paste it in your browser



