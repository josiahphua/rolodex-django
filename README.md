# ROLODEX - Contacts Management w/ Django
![](https://cdn.mscdirect.com/global/images/ProductImages/7474251-11.jpg)
# Back Story
Goodbye rolodex, Hello 21st Century.
Let's get rid of the rolodex that's gathering dust on our desk and start storing our contacts in an app.

# Deliverables
1. User should be able to create a contact via a form
1. A page listing all of your contacts
1. A page to show one contact

# Further (But you've got the whole weekend to solve it and it's the final weekend homework so you might as well push yourself and please the homework GOD)
1. Search through your rolodex
2. Style it with style

## Getting Started
- Clone this repository
- Create a django project `django-admin startproject rolodex`
- Install Django `pipenv install django`
- Start python virtual environment `pipenv shell`
- Create a django app `python manage.py startapp contacts`
- When complete send a pull request with a readme containing screenshots of your app.

## Helper
Since we have all agreed to use Postgresql as the Database for our app. Here is the hint on how to set it up.
1. On your terminal run `createdb <appname_development>`
2. Add to `your settings.py` under database
```python
  DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<database name>',
        'USER': '<ebere>',
        # 'PASSWORD': '<ebere>', # only required if on windows
        'HOST': 'localhost',
        'PORT': 5432
    }
}
```

If the above doesn't work for you, please consider using sqlite as a the Database for your app, as seen in class.



