#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'graph_tutorial.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

"""
From analyzing this file, it seems this file will be the one in charge of initializing the Django application
It will import the settings and enter a try/catch sequence to import django.core.management/execute_from_command_line, 
If it fails, will throw an exception with a message. If no exception is thrown, it will use the imported function and will execute the server.
"""