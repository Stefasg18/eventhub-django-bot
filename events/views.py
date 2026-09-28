from django.shortcuts import render
from django.http import JsonResponse
from .models import Event

def index(request):
    return render(request,"events/index.html",{"events":Event.objects.order_by("starts_at")})

def api_events(request):
    data=[{"id":e.id,"title":e.title,"description":e.description,"starts_at":e.starts_at.isoformat(),"free_places":max(e.capacity-e.registrations.count(),0)} for e in Event.objects.order_by("starts_at")]
    return JsonResponse({"events":data})
