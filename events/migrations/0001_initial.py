from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial=True
    dependencies=[]
    operations=[
        migrations.CreateModel(name="Event",fields=[
            ("id",models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name="ID")),
            ("title",models.CharField(max_length=200)),
            ("description",models.TextField(blank=True)),
            ("starts_at",models.DateTimeField()),
            ("capacity",models.PositiveIntegerField(default=50)),
        ]),
        migrations.CreateModel(name="Registration",fields=[
            ("id",models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name="ID")),
            ("name",models.CharField(max_length=120)),
            ("telegram_id",models.BigIntegerField()),
            ("created_at",models.DateTimeField(auto_now_add=True)),
            ("event",models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,related_name="registrations",to="events.event")),
        ]),
        migrations.AddConstraint(model_name="registration",constraint=models.UniqueConstraint(fields=("event","telegram_id"),name="unique_event_user")),
    ]
