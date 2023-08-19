## Basic Settings for Development

Activate environment

    python3 -m venv venv
    source venv/bin/activate

## Install dependencies
    pip install -r requirements-test.txt


Basic Settings
You’ll have to make the following creations to your your .env file
and Django Secret Key

    DB_NAME=your_database_name
    DB_USR=your_user_name
    DB_PWD=your_password

    SECRET_KEY='your_secret_key'
    JWT_SECRET_KEY='your_jwt_secret_key'

 ## migrate 
 python manage.py migrate  

 ## Setup Initial User, and Admin

    # create first user
    python manage.py createsuperuser
    python manage.py runserver 