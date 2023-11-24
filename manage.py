#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from decouple import config

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'filas.settings')
    try:
        from django.core.management import execute_from_command_line
        from django.conf import settings
    
        if settings.DEBUG:
            if os.environ.get('RUN_MAIN') or os.environ.get('WERKZEUG_RUN_MAIN'):
                import debugpy
                debugpy.listen(("0.0.0.0",config('DEBUG_PORT', default=3000, cast=int)))
                print('Attached!')

    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
