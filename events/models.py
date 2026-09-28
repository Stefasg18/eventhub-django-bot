from django.db import models

class Event(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(blank=True)
    starts_at=models.DateTimeField()
    capacity=models.PositiveIntegerField(default=50)
    def __str__(self): return self.title

class Registration(models.Model):
    event=models.ForeignKey(Event,on_delete=models.CASCADE,related_name="registrations")
    name=models.CharField(max_length=120)
    telegram_id=models.BigIntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        constraints=[models.UniqueConstraint(fields=["event","telegram_id"],name="unique_event_user")]
