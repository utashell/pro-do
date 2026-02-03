from django.db import models
from django.utils.html import format_html


class Todo(models.Model):
    class Prority(models.TextChoices):
        HIGH = 'High'
        MEDIUM = 'Medium'
        LOW = 'Low'
        
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_done = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=10,
        choices=Prority.choices,
        default=Prority.MEDIUM,
    )    
    due_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        
    def status_colored(self):
        if self.is_done:
            return format_html(
                '<span style="color: {}; font-weight: bold;">{}</span>',
                'green',
                '✔ Done'
            )
        return format_html(
            '<span style="color: {}; font-weight: bold;">{}</span>',
            'orange',
            '⏳ Pending'
        )
    
    status_colored.short_description = "Status"
    
    def __str__(self):
        return self.title