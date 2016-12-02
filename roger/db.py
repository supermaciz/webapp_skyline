from pathlib import Path


class   ReadOrWrite(object):

    def db_for_read(self, model, **hints):
        if Path('/tmp/db.lock').exists():
            return "db_read"
        else:
            return "db_read"

    def db_for_write(self, model, **hints):
        if Path('/tmp/db.lock').exists():
            return "default"
        else:
            return "default"
