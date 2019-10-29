# rp-portfolio

setup the environment
	make a directory
	setup virtual environment = an isolated python environment where each project is independent to dev so other projects are not affected by it.
	command 1: python -m venv venv(name of the environment)
  
  Basically all the python basic files and libraries would be copied over in this file from now on so it's isolated
	to activate virtual environment
	command: source venv/bin/activate
	or windows command 2: venv\Scripts\activate.bat

Once in the venv, install django:command: django-admin startproject portfolio (or any project name)


Once the django is installed create a django project: command: django-admin startproject portfolio (your project name)

Or if want to run this project run command 1,2,3 then paste the project in the same folder where venv is created
and run command: python manage.py runserver
