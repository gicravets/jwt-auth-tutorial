
source venv/bin/activate

export APP_SETTINGS="project.server.config.DevelopmentConfig"
export SECRET_KEY="\xf9'"

python manage.py runserver