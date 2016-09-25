# ROGER SKYLINE THE WEBSITE


## configuration

requiert python3

	pip install -r requirements.txt

in roger/settings.py complete

	# line 82
	DATABASES = {
	    'default': {
	        'ENGINE': 'django.db.backends.mysql',	# for mysql or mariadb
	        'NAME': '',				# name of db
	        'USER': '',
	        'PASSWORD': '',
	        'HOST': '',
	        'PORT': '',
	    }
	}
	# line 138
	EMAIL_HOST = 'smtp.XXX.com'
	EMAIL_HOST_USER = 'XXXX@gXXX.XX'
	EMAIL_HOST_PASSWORD = ''
	EMAIL_PORT = 587
	EMAIL_USE_TLS = True

and init django

	python3 manage.py makemigrations
	python3 manage.py migrate
	python3 manage.py createsuperuser
	python3 manage.py runserver
