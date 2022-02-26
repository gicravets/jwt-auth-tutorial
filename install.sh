

pyenv install 3.7.6

pyenv local 3.7.6

python -m venv venv

source venv/bin/activate

pip install --upgrade pip setuptools wheel

pip install -r requirements.txt

pip install pyjwt==1.4.2
pip install psycopg2==2.9.3  
pip install psycopg2-binary==2.9.3
pip install --upgrade sqlalchemy

export APP_SETTINGS="project.server.config.DevelopmentConfig"
export SECRET_KEY="\xf9'"


python manage.py test

echo "python manage.py runserver"