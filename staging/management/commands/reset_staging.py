import os
from django.conf import settings
from django.core.management import BaseCommand, call_command
from django.db import connection
from django.contrib.contenttypes.models import ContentType
from wagtail.core.models import Page
from staging.db_signals import disable_db_signals


class Command(BaseCommand):

    def handle(self, *a, **kw):
        if settings.DATABASES['default']['ENGINE'] != 'django.db.backends.sqlite3':
            if input('Database engine is not SQLite. Do you wish load staging data? [y/N]') != 'y':
                return
            self._drop_postgres()
        else:
            self._drop_sqlite()
        
        call_command('migrate')

        # cleaning shit created by wagtail in migrations:
        disable_db_signals()
        print(Page.objects.all().delete())
        print(ContentType.objects.all().delete())
        
        # loading staging fixtures:
        call_command('load_staging')

    def _drop_sqlite(self):
        db_file = settings.DATABASES['default']['NAME']
        if os.path.exists(db_file):
            os.unlink(db_file)

    def _drop_postgres(self):
        with connection.cursor() as cursor:
            sql = "SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname = 'public';"
            cursor.execute(sql)
            tables = cursor.fetchall()
            for row in tables:
                cursor.execute(f'DROP TABLE {row[0]} CASCADE;')
