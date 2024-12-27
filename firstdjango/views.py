from django.http import HttpResponse
# สร้างฟังก์ชันสำหรับไว้เรียกที่ URL ที่เราสร้างไว้
from django.shortcuts import render
def index(request):
    return render(request,'index.html')


def about(request):
    return HttpResponse("about Page.")

# get parameters from url
def search(request,keyword,page):
    return HttpResponse(f'Search Page {keyword} {page}')

# get query string
def map(request):
    type = request.GET.get('type','hybrid')
    lat = request.GET.get('lat','0')
    lng = request.GET.get('lng','0')
    zoom = request.GET.get('zoom',11)
    return HttpResponse(f'page map {type} {lat} {lng} {zoom}')

