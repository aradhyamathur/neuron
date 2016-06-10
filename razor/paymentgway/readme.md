<H1>Razor Payment Gateway</H1>
This project aims at integrating Razor payment gateway with a sample Django project.

<h3>Setting Up </h3>
-download the project
-createdb raz_user
-fill in the DB detail in settings.py
-enter your Razor pay  "<API_KEY>" "<API_SECRET>" in views.py razorpayclient definition
-enter your razor pay API_KEY in data-key in script in index.html 
-enter other details in the script
-run command _python manage.py makemigrations_
-run command _pyhton manage.py migrate_
-create super user
-create a dummy person in Payee table
-run command python manage.py runserver
-go to http://127.0.0.1:8000/razor/

<H3> Checking </H3>
-login as dummy user
-click pay with razorpay
-log in your razorpay dashboard to view the transaction