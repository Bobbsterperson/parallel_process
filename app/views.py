from django.http import JsonResponse
from .tasks import perform_calculation
from celery import group

def run_calculations(request):
    tasks = []
    task_counter = 1
    task_ids = []
    for a in range(1, 10):
        for b in range(1, 10):
            task_id = f"task_{task_counter}"
            tasks.append(perform_calculation.s(task_id, a, b))
            task_ids.append(task_id)
            task_counter += 1
    job = group(tasks)
    result = job.apply_async()

    return JsonResponse({
        "status": "All calculations initiated",
        "task_ids": task_ids
    })