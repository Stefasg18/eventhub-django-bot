import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_events_api(client):
    response=client.get(reverse("api_events"))
    assert response.status_code==200
    assert response.json()=={"events":[]}
