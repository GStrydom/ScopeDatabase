#!/usr/bin/env python
import os
import sys

sys.path.append('C:/Users/Seth/PycharmProjects/ScopeDatabase/PipingScopeDatabase/projsettings/')

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PipingScopingDatabase.projsettings.dev_settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
