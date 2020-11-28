from django.core.management import BaseCommand, call_command
from django.core.management.commands.loaddata import Command as LoadDataCmd
from utils.db_signals import disable_db_signals


class Command(BaseCommand):
    """
    This is an overlooing default django's loaddata command
    that also disables all model signals
    """

    def handle(self, *args, **options):
        disable_db_signals()
        cmd = LoadDataCmd()
        cmd.handle(*args, **options)
    
    def add_arguments(self, parser):
        parser.add_argument('args', metavar='fixture', nargs='+', help='Fixture labels.')
        parser.add_argument(
            '--database', default='default',
            help='Nominates a specific database to load fixtures into. Defaults to the "default" database.',
        )
        parser.add_argument(
            '--app', dest='app_label',
            help='Only look for fixtures in the specified app.',
        )
        parser.add_argument(
            '--ignorenonexistent', '-i', action='store_true', dest='ignore',
            help='Ignores entries in the serialized data for fields that do not '
                 'currently exist on the model.',
        )
        parser.add_argument(
            '-e', '--exclude', action='append', default=[],
            help='An app_label or app_label.ModelName to exclude. Can be used multiple times.',
        )
        parser.add_argument(
            '--format',
            help='Format of serialized data when reading from stdin.',
        )