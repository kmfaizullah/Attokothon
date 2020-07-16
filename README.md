### Attokothon: A Digital Personal Note Book
This is a web application containing personal information including blog post, todo list, personal note etc.
<b>Technology/Tools : </b> Django, Python, PostgreSQL, Bootstrap, HTML and CSS.
<h6> <a href="https://youtu.be/VuQEjrhJ4sQ">Click here to see the Demo</h6>

#### Dependencies
1. It has been tested in windows 10 machine. 
2. Python
3. Django
4. Crispy Forms
5. PostgreSQL
6. psycopg2

#### Running Procedure
<b>Step 1: </b> Install Python, Django and PostgreSQL in your machine. <br>
<b>Step 2: </b> While installing postgresql remember the given password.<br>
<b>Step 3: </b> Run pgadmin (Will be installed while installing postgre) and using the password connect with the server.<br>
<b>Step 4: </b> Create a databse named `Attokothon` <br>
<b>Step 5: </b> Create a folder name `atto` in your local machine to start the django application. <br>
<b>Step 6: </b> Go inside the `atto` folder and run the command `django-admin startproject attokothon` to start the project. It will create a project name `attokothon`. <br>
<b>Step 7: </b> Go to the settings file of `attokothon project` and connect the database with the server (Same as this repo setting file). <br>
<b>Step 8: </b> Execute `pip install psycopg2` command to install psycopg2 module. <br>
<b>Step 9: </b> Now create another app named `diary` using `python manage.py startapp diary` command. <br>
<b>Step 10: </b> Now go to the setting file and connect installed app with the main project.<br>
<b>Step 11: </b> Download this repository and copy `static folder, templates folder, forms.py, models.py, urls.py and views.py` files to the newly created diary project.<br>
<b>Step 12: </b> Connect the local url with the global project url  <br>
<b>Step 13: </b> Now to create databse run the following commands: <br>
            <h6>`python manage.py makemigrations diary` </h6>
            <b>Note: </b> This command will create a file under migration folder named like `0001_initialy.py` <br>
            Now execute: <br>
            <h6>`python manage.py sqlmigrate diary 0001` </h6>
            <b>Note: </b> This command will create corresponding sql query. <br>
            Finally execute : <br>
            <h6>`python manage.py migrate`</h6>
            <b>Note: </b> This will create the final table.<br>
            
<b>Step 14: </b> Install django crispy form using `pip install django-crispy-forms` command. <br>
<b>Step 15: </b> Add the crispy template and crispy form to the `setting.py` file.<br>
<b>Step 16: </b> Now run the `python manage.py runserver` command and this will start the project in `http://127.0.0.1:8000/`<br>

