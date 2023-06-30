from django.shortcuts import render
from django.http import StreamingHttpResponse
from django.views.decorators import gzip

from .camera import *

@gzip.gzip_page
def livefe(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:  # This is bad!
        pass

def index(request, *args, **kwargs):
    return render(request, 'home/index_exs.html')