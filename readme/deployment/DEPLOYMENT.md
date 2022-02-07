# Deployment

### Heroku deployment
Although deployed from its GitHub repository, the project is hosted by Heroku. In order to deploy to Heroku, the following steps should be followed:
1. Create an account at [Heroku](https://heroku.com/) and log in.
2. Choose 'create new app' from the drop down menu labelled 'new'.
3. Give the app an appropriate name and choose the closest region from the dropdown list, then click 'create app'.
4. From the dashboard, navigate to the 'resources' tab. Add Heroku Postgres to the app by searching and then selecting it. 
5. Choose 'Hobby Dev – Free plan'.
6. Create json files within GitPod in order to populate the Postgres database in Heroku:
    * `python3 manage.py dumpdata products.Category > categories.json`
    * `python3 manage.py dumpdata products.Product > products.json`
7. Install dj_database_url and psycopg2-binary using `pip3 install`.
8. In `settings.py`, import the dj_database_url and replace the default `DATABASE` setting with the 'database_url' found in the app's config vars in Heroku:
```
DATABASES = {
        'default': dj_database_url.parse(<DATABASE_URL>)
    }
```
9. In GitPod, enter `python3 manage.py migrate` to run migrations and create the models in the Postgres database.
10. Populate the new database by loading the data from the json files. Be sure to load categories first:
    * `python3 manage.py loaddata categories.json`
    * `python3 manage.py loaddata products.json`
11. Create a new superuser, this was done by using `python3 manage.py createsuperuser` and then following the instructions shown in the terminal.
12. Install gunicorn using `pip3 install`.
13. Run `pip3 freeze > requirements.txt` to make sure the app has all the necessary requirements.
14. Create a Procfile and populate it by typing in the GitPod terminal:
```
web: gunicorn <app_name>.wsgi:application
```
15. Log into Heroku via your IDE terminal using 'heroku login -i'.
16. To ensure no static files are transferred, type `heroku config:set COLLECTSTATIC=1 --app <app_name>`
17. In `settings.py` add the hostname of the Heroku app:
```
ALLOWED_HOSTS = ['<hostname>', 'localhost']
```
18. From the Heroku dashboard, navigate to the 'deploy' tab, 'Deployment method' section and select 'connect to GitHub'. 
20. Search for your GitHub repository and click 'connect'.
21. Select 'Automatic Deploys'.
22. In dashboard, navigate to the 'settings' tab, 'config vars' section and enter the following key value pairs:
    * AWS_ACCESS_KEY_ID - I get this when I set up AWS.
    * AWS_SECRET_ACCESS_KEY - I get this when I set up AWS.
    * DATABASE_URL - Prepopulated.
    * DISABLE_COLLECTSTATIC - Created this during step 17.
    * SECRET_KEY
    * STRIPE_PUBLIC_KEY
    * STRIPE_SECRET_KEY
    * STRIPE_WH_SECRET
    * USE_AWS - True
23. Back in 'settings.py', chanage the default 'DATABASE' in order that it retrieves the value held in Heroku:
```
DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
```
24. Add, committ and push all changes via the terminal.
25. The app can now be launched directly from Heroku (or at https://ENTER-APP-NAME.herokuapp.com) and will automatically update to the latest version each time commits are pushed to Github.

### AWS and S3 Bucket Setup
1. Create an [AWS](https://aws.amazon.com/) account.
2. Navigate to the management console, search for "S3" to be taken to the S3 dashboard.
3. Click **create bucket** button.
    * Give it a name and select the region closest to you.
    * Allow public access.
4. In the bucket's properties select **static website hosting**.
    * Select "use this bucket to host a website".
    * Give it the default values of `index.html` and `error.html` then save.
5. For the buckets permissions CORS configuration use:
```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```
6. For the buckets permissions policy:
    * Copy the Amazon resource name (ARN) from the top of the page.
    * Click "policy generator".
    * Select type of policy as "S3 Bucket Policy".
    * Allow all principals by using `*`.
    * Set action to "GetObject".
    * Paste in the ARN.
    * Click **Add statement**. Then **Generate policy** and copy the json file shown.
    * Paste this json file to bucket policy.
        * Add `/*` at the end of the 'Resource' key.
    * Save.
7. For the access control list:
    * Set list objects to everyone.