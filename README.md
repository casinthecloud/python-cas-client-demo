Django webapp protected by the django-cas client (https://github.com/kstateome/django-cas)
==

![English](https://www.casinthecloud.com/img/other/flag_en.png)

Demo using the django-cas client (v1.0.0) to protect a Django web application (`pip install git+ssh://git@github.com/kstateome/django-cas.git@1.0.0#egg=cas`).

Use **python manage.py runserver** to start the webapp on **http://localhost:8000**. The url 'protected/index' is protected and should trigger a CAS authentication.

Most of the configuration is defined in the **python_cas_client_demo/settings.py** file.

Use your own CAS in the cloud server with the following option:

- 'Authorize redirection urls after logout'

and the following service:

- Service url: 'http://localhost:8000/accounts/login/*' as an 'Ant pattern'
- 'Call from the browser to the specific application url for logout: http://localhost:8000/logout'
- *Returned attribute(s)* : 'all the attributes'.

==

![Français](https://www.casinthecloud.com/img/other/flag_fr.png)

Démo utilisant le client django-cas (v1.0.0) pour protéger une application web Django (`pip install git+ssh://git@github.com/kstateome/django-cas.git@1.0.0#egg=cas`).

Utilisez **python manage.py runserver** pour lancer le site web sur **http://localhost:8000**. L'url 'protected/index' est protégée et déclenche une authentification CAS.

L'essentiel de la configuration est défini dans le fichier **python_cas_client_demo/settings.py**.

Utilisez votre propre serveur CAS in the cloud avec l'option :

- 'Autoriser les urls de redirection après déconnexion'

et le service suivant :

- Url de service : 'http://localhost:8000/accounts/login/*' en tant que 'Expression Ant'
- 'Appel depuis le navigateur de l'url applicative spécifique pour la déconnexion : http://localhost:8000/logout'
- *Attribut(s) renvoyé(s)* : 'tous les attributs'.
