# -*- coding: utf-8 -*-
from invoke import run, task
from time import gmtime, strftime


@task
def install():
    run('pip install -r requirements.txt')

@task
def migrate():
    run('python manage.py migrate')
