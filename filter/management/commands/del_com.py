from django.db import connection
from filter.models import AppTaskresult
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM app_taskresult WHERE MOD(result, 3) = 0 ORDER BY id DESC LIMIT 1")
        last_row = cursor.fetchone()
        if last_row:
            cursor.execute("DELETE FROM app_taskresult WHERE MOD(result, 3) = 0 AND id != %s", [last_row[0]])
            connection.commit()
            self.stdout.write("Deleted rows where result MOD 3 == 0, excluding the last one.")
        else:
            self.stdout.write("No rows divisible by 3 were found.")
