import pytest
from django.utils import timezone
from events.models import Event

@pytest.mark.django_db
def test_event_string_representation():
    event = Event.objects.create(title="Python Meetup", starts_at=timezone.now(), capacity=20)
    assert str(event) == "Python Meetup"
