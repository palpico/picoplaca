picoplaca
=========

Ecuadorian license plate verification system for "Pico y Placa" policies.

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django

Basic Commands
--------------


Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To start developer environment, use this command::

    $docker-compose -f developer.yml up

* To start production environment, use this command::

    $docker-compose -f production.yml up

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser


Deployment
----------

The following details how to deploy this application.





