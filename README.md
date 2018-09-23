# Introduction
This is a Very simple Django based backend for Upstox API. This will help you get started, But do keep in mind that running server on localhost is not safe.

This Django app server will help you complete the OAuth login flow, get access token and saves it in os environment and local file. The accesss token remains valid for a day. You can directly use this access token from the os environment.
### Clone git repository:
```
git clone https://github.com/swapniljariwala/upstox_oauth.git

cd upstox_oauth

pip install -r requirements.txt
```

Now configure go to your [Upstox API Console](https://developer.upstox.com/#/apps) and set up redirect url as [http://localhost:8000/upstox/redirect/](http://localhost:8000/upstox/redirect/).

### Copy API and Secret Keys from API console and set up environment
```
python manage.py setenv
Enter API KEY: Your-api-key
Enter API SECRET: Your-secret-key
```
### Run Django development server
```
python manage.py runserver
```
Hopefully there should be no errors. You are all set.