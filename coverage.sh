#!/bin/bash
rm -rf htmlcov
coverage run --source='.' manage.py test
coverage report -m
coverage html
cd htmlcov
rm .gitignore