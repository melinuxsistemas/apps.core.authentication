# Otma Core

Core for company projects. To install app:

	1. Execute: pip install https://github.com/melinuxsistemas/modules.core.authentication/zipball/master

	2. Add "apps.core.authentication" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'apps.core.authentication',
    ]

	3. Include the polls URLconf in your project urls.py like this:

    	path('core/', include('apps.core.authentication.urls')),

	4. Run `python manage.py migrate` to create the core models.