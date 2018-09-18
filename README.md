# Mozilla Azerbaijan Website

Public website for Mozilla Azerbaijan Community.

INSTALL
-------

* Fork and clone the repository
* Create a virtual environment (optional): `virtualenv venv -p python3`
* Activate the virtual environment (optional): `source venv/bin/activate`
* Install requirements: `pip install -r requirements.txt`
* Create `local_settings.py` file in the project's root directory
* Initialize database: `./manage.py migrate`
* Create admin user: `./manage.py createsuperuser`
* Run the application: `./manage.py runserver`

LICENSE
-------
Copyright 2018 Mozilla Azerbaijan <info@mozillaz.org>

Website's code and contents are released under **Mozilla Public License v2**.
All third-party contents and their licenses are mentioned in `CREDITS.md` file.

CONTRIBUTORS
------------
Emin Mastizada
