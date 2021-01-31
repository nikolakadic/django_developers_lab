from django.shortcuts import render
from .models import Band

def band_listing(request):
    """A view of all bands."""
    bands = Band.objects.all() # SELECT * FROM BAND
    # first_band = Band.objects.first()
    # print(first_band)
    return render(request, 'bands/band_listing.html', {'bands': bands})

def band_detail(request, band_id):
    """A view of band detail."""
    band = Band.objects.get(pk=band_id) # SELECT * FROM BAND WHERE ID = band_id
    return render(request, 'bands/band_detail.html', {'band': band})

def band_search(request):
    """A view of band detail."""
    queried_band = request.GET['q']
    band = None
    try:
        band = Band.objects.get(name=queried_band) # SELECT * FROM BAND WHERE NAME = queried_band
        queried_band_exists = True
    except:
        queried_band_exists = False
    return render(request, 'bands/band_searched.html', {'band': band, 'valid_results':queried_band_exists})

