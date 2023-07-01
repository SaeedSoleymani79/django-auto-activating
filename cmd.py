import os

def activate():
    os.system('cmd/k "cd../../../django/projects/env/Scripts && activate && cd ../../todolist && python manage.py runserver"')


activate()
