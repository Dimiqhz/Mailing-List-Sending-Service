#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "email_service.settings")
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        try:
            import django
        except ImportError:
            raise ImportError(
                "Не удалось импортировать Django. Убедитесь, что он установлен и доступен в PYTHONPATH."
            )
        raise
    execute_from_command_line(sys.argv)
