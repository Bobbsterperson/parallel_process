from django.contrib import admin
from .models import TaskResult

@admin.register(TaskResult)
class TaskResultAdmin(admin.ModelAdmin):
    list_display = ('task_id', 'result', 'current_time', 'time_taken')
