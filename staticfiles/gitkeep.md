This file created to make Git track this directory.

This directory is mandatory to escape warning while running tests for Django.

Files for this directory will be created automatically by Heroku after push changes to GitHub.

If you need to start this application in production mode locally, you should run the following command:
```bash
   python manage.py collectstatic
   ```
and set 
DEBUG = False
in [settings](../library/settings.py)
