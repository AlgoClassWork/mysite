from django.shortcuts import render

from .models import Ad

# Create your views here.
def ad_list(request):
    ads = Ad.objects.all() 
    return render(request, 'ads/ad_list.html', {'ads': ads})
