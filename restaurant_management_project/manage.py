#!/usr/bin/env python
import os, sys
def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant_management.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Couldn't import Django. Install requirements and try again.") from exc
    execute_from_command_line(sys.argv)
if __name__ == '__main__':
    main()
