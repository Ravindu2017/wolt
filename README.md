# Wolt Application

Readability
## - Parent Steps
### - Children Steps

This is my attempt at wolt's front end task using django framework. I have created django project called wolt and within it an app called "menu".
Menu holds the code for displaying the restaurants in the "views.py" directory and the html documents are within the "templates" directory inside of the menu directory.

This readme contains intructions to installing django via pip, running the app, and initialising databases from scratch.

## Install Django
Install Django using python's pip tool, locate where your scripts folder within the python directory in your machine is. Once you find the
scripts folder open up command line interface with the file path to scripts. Run pip install django. Keep the file path to scripts copied
or ready since you might need it again.

## Execution

### Go to wolt directory where "manage.py" is located and open command line interface, there run "py manage.py runserver" for windows or "python manage.py runserver" for linux/mac.

### Copy the development server address in command line interface and add "/restaurants/list/" to the address bar of your browser.


## Initialising databases.
Follow these steps if creating databases from scratch, this repo includes ready made databases so it may be ignored.

### First of all
Open the wolt directory where "manage.py" is located. Open command line interface and run "py manage.py makemigrations" (for windows) or "python manage.py makemigrations" for (linux/mac). Then run the command "py manage.py migrate" for windows or "python manage.py migrate" for (linux/mac).

### Secondly
Populate the databases with the "Database_info.py" file located in the menu subdirectory. Make sure the "with open" line in Database_info.py opens the correct "restaurants.json" file. To populate the newly created databases go back to wolt directory where "manage.py" is located. In windows run "py manage.py shell < menu\\Database_info.py" or "python manage.py shell < menu\\Database_info.py" for linux/mac users. It will take some time but this will populate the database with the appropriate information.

### Finally
Go to the directory where "manage.py" is located and open command line interface and run "py manage.py runserver" in windows or "python manage.py runserver" in linux/mac. Copy the development server address and add "/restaurants/list/".
