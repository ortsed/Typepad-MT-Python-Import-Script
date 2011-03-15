# Sample settings file for MT import

DATABASES = {
 	'default': {
 		'ENGINE': 'mysql', #django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
 		'NAME': 'mt',					  # Or path to database file if using sqlite3.
 		'USER': 'username',					  # Not used with sqlite3.
 		'PASSWORD': 'password',				  # Not used with sqlite3.
 		'HOST': 'localhost',					  # Set to empty string for localhost. Not used with sqlite3.
 		'PORT': '',					  # Set to empty string for default. Not used with sqlite3.
 	}
}
