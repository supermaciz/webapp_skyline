
class   ReadOrWrite(object):

    def db_for_read(self, model, **hints):
        return "db_read"

    def db_for_write(self, model, **hints):
        return "default"
