#!/bin/bash
rm -rf htmlcov
coverage run --source='.' manage.py test
coverage report -m
coverage html
rm .coverage
cd htmlcov
rm .gitignore