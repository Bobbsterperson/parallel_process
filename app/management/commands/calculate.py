from django.core.management.base import BaseCommand
from celery import group
from app.tasks import perform_calculation

class Command(BaseCommand):
    help = "Run parallel calculations and store results in the database"

    def handle(self, *args, **kwargs):
        self.stdout.write("Starting parallel calculations...")
        tasks = []
        task_counter = 1
        for a in range(1, 10):
            for b in range(1, 10):
                task_id = f"task_{task_counter}"
                tasks.append(perform_calculation.s(task_id, a, b))
                task_counter += 1
        job = group(tasks)
        result = job.apply_async()

        self.stdout.write("Calculations have been initiated.")
        self.stdout.write(f"Celery Group ID: {result.id}")
        self.stdout.write("Results will be saved in the database as tasks complete.")
