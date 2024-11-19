from celery import shared_task
from datetime import datetime
import time
from .models import TaskResult

@shared_task
def perform_calculation(task_id, a, b):
    start_time = time.time()
    result = a + b
    end_time = time.time()
    duration = end_time - start_time
    current_time = datetime.now().time()
    TaskResult.objects.create(
        task_id=task_id,
        result=result,
        current_time=current_time,
        time_taken=duration,
    )
    return {
        "task_id": task_id,
        "result": result,
        "current_time": current_time.strftime("%H:%M:%S"),
        "time_taken": duration,
    }
