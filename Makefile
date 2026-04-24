dj:
	 python manage.py runserver

django_project:
	django-admin startproject django_p38

app:
	python manage.py startapp apps

mig:
	python3 manage.py makemigrations
	python3 manage.py migrate


#
#git init
#git add README.md
#git commit -m "first commit"
#git branch -M main
#git remote add origin https://github.com/abdumanovakbar-art/Django.git
#git push -u origin main