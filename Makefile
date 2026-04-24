dj:
	 python manage.py runserver

django_project:
	django-admin startproject django_p38

app:
	python manage.py startapp apps

mig:
	python3 manage.py makemigrations
	python3 manage.py migrate


git:
	git init

git add:
	git add .

git commit:
	git commit -m "first commit"

git remote:
	git remote add origin https://github.com/abdumanovakbar-art/Django.git

git push:
	git push -u origin main


