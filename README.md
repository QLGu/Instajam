Instajam
========
--------

## Installation and configuration

1.  Install Python, virtualenv and npm.

2.  Make, enter and activate a virtualenv:

        $ virtualenv instajam --no-site-packages
        New python executable in clientes/bin/python
        Installing setuptools............done.
        $ cd instajam/
        $ . bin/activate

2.  Clone this repo into a sub-directory of the new virtualenv:

        $ git clone git@github.com:diegotoral/Instajam.git
        $ cd instajam/

3.  Go through the following files, editing as necessary:

        `settings/testing.py`
        `settings/development.py`

4.  Symlink the project directory into the virtualenv's `site-packages`:

        $ ln -s `pwd` ../lib/python2.6/site-packages/instajam

    Replace `python2.6` with the installed version of Python on your machine.

5.  Set the `DJANGO_SETTINGS_MODULE` environment variable now, and on every
    virtualenv activation:

        $ export DJANGO_SETTINGS_MODULE=instajam.settings.development
        $ echo "!!" >> ../bin/activate

6.  Install the basic project requirements:

        $ easy_install pip
        $ pip install -r requirements/DEVELOPMENT
        $ pip install -r requirements/TESTING
        $ npm install
        $ bower install

    As you edit your `REQUIREMENTS` files, you can run those last commands again;
    `pip` will realise which packages you've added and will ignore those already
    installed.
