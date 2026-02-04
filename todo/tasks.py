from celery import shared_task
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
from .models import Todo
from collections import defaultdict

@shared_task
def demo_admin_task():
    print("✅ Demo task executed from Django Admin!")

@shared_task
def send_daily_task_reminder():
    today = timezone.localdate()

    tasks = Todo.objects.filter(is_done=False, due_date=today).select_related('owner')
    user_tasks = defaultdict(list)

    for task in tasks:
        if task.owner and task.owner.email:
            user_tasks[task.owner].append(task)

    for user, tasks in user_tasks.items():
        task_list = "\n".join(f"- {task.title}" for task in tasks)

        message = f"""
Hi {user.username},

This is your daily reminder. You have the following tasks scheduled for today:

{task_list}

Best regards,
Todo App
"""
        send_mail(
            subject="Today's Tasks",
            message=message.strip(),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
        )
