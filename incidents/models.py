from django.db import models
from django.contrib.auth.models import User

class Incident(models.Model):
    INCIDENT_STATUSES = [
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Closed', 'Closed'),
    ]

    INCIDENT_PRIORITIES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]

    incident_id = models.CharField(max_length=15, unique=True)
    reporter_name = models.CharField(max_length=100)
    incident_details = models.TextField()
    reported_at = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=10, choices=INCIDENT_PRIORITIES)
    status = models.CharField(max_length=15, choices=INCIDENT_STATUSES, default='Open')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.incident_id
