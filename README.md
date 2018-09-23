### Clone git repository:
```
git clone https://github.com/swapniljariwala/upstox_oauth.git

cd upstox_oauth

pip install -r requirements.txt
```

### Now configure go to your [Upstox API Console](https://developer.upstox.com/#/apps) and set up redirect url as [http://localhost:8000/upstox/redirect/](http://localhost:8000/upstox/redirect/).

### Copy API and Secret Keys from API console and set up environment

python manage.py setenv
Enter API KEY: Your-api-key
Enter API SECRET: Your-secret-key

### Run Django development server

python manage.py runserver

Hopefully there should be no errors. You are all set.