Django webapp protected by the django-cas client (https://github.com/kstateome/django-cas)
==

Demo using the django-cas client (v1.0.0) to protect a Django web application (`pip install git+ssh://git@github.com/kstateome/django-cas.git@1.0.0#egg=cas`).

Use **python manage.py runserver** to start the webapp on **http://localhost:8000**. The url 'protected/index' is protected and should trigger a CAS authentication.

Most of the configuration is defined in the **python_cas_client_demo/settings.py** file.

A specific logout application url is available at: http://localhost:8000/logout.

Run your CAS server on http://localhost:8888/cas.
