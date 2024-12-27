from django.http import HttpResponse
# สร้างฟังก์ชันสำหรับไว้เรียกที่ URL ที่เราสร้างไว้
def index(request):
    return HttpResponse("Hello, world. You're at the firstdjango index.")
