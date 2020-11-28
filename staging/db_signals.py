from django.db.models import signals

DB_SIGNALS = (
    signals.pre_init,
    signals.post_init,
    signals.pre_save,
    signals.post_save,
    signals.pre_delete,
    signals.post_delete,
    signals.pre_migrate,
    signals.post_migrate,
)


def disable_db_signals():
    for signal in DB_SIGNALS:
        signal.receivers = []
