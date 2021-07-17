import datetime
import os

class Logger:
    file_name = 'temp'

    @classmethod
    def _write_log_to_file(cls, data: str):
        return True