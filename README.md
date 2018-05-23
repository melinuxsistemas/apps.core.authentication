# Otma Core

Core for company projects. To install app:

	1. Execute: pip install https://github.com/melinuxsistemas/otma_core/zipball/master

	2. Add "otma_core" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'otma_core',
    ]

	3. Include the polls URLconf in your project urls.py like this:

    	path('core/', include('otma_core.urls')),

	4. Run `python manage.py migrate` to create the core models.