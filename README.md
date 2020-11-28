#what does it do
This will make in a very easy way fixture of all your models in wagtail

# to install
TODO

#usage
Add `'staging'` to your installed packackages in your settings.py

    installed_packages = [  
        ...
        'staging'
        ]  

Make sure that staging is the last item in you installed packages.

Add a fixtures directory

FIXTURES_DIRS = (
    os.path.join(BASE_DIR, 'fixtures)
)

Thats it, your done!

#usage

##save_staging

    ./manage.py save_staging
    or
    ./manage.py save_staging [model] 

this will loop over all you installed packages and create a fixture for it
It will also create in you media folder a staging folder saving all staging images seperate
You could include that folder in you repo. So you will have an easy install with media.
Without overriding the original content.

    TIP: to reduce the image size you can use morgrify:
    https://imagemagick.org/script/mogrify.php

##reset_staging

./manage.py reset_staging

This command wil reinstall all fixtures in you datbase.

#workflow

Build your pages and database. Populate your DB manualy with content.
./manage.py save_staging

change your model. Populate again you DB with content of new db.
./manage.py save_staging <model>

Push to git and let college work further on your DB and tell him to
./manage.py reset_staging

Come back 1 year later and start your project with 
./manage.py reset_staging
