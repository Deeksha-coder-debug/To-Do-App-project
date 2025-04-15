from django.db import models

PRIORITY_CHOICES = [
    ('L', 'Low'),
    ('M', 'Medium'),
    ('H', 'High'),
]
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)  # 📅 Due date for sorting
    priority = models.CharField(
        max_length=1,
        choices=[('L', 'Low'), ('M', 'Medium'), ('H', 'High')],
        default='M'
    )  # ⭐ Priority choice
    category = models.CharField(
        max_length=50,
        choices=[('Work', 'Work'), ('Personal', 'Personal'), ('Study', 'Study')],
        default='Personal'
    )
    def __str__(self):
        return self.title
