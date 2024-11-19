from django.db import models

class TaskResult(models.Model):
    task_id = models.CharField(max_length=50)
    result = models.IntegerField()
    current_time = models.TimeField()
    time_taken = models.FloatField()

    def __str__(self):
        return f"Task {self.task_id}: Result={self.result} at {self.current_time}"
