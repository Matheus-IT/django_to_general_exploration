import requests
from django.shortcuts import render
from django.http import StreamingHttpResponse, FileResponse
from itertools import count
from django.conf import settings
from django.templatetags.static import static




def home_view(request):
    return render(request, 'example/home.html')

def download_view(request):
    # def file_iterator(file_path, chunk_size=512):
    #     print(file_path)
    #     with open(file_path) as f:
    #         while True:
    #             c = f.read(chunk_size)
    #             if c:
    #                 yield bytes(c)
    #             else:
    #                 break


    # response = StreamingHttpResponse(file_iterator(file_path), content_type='application/octet-stream')
    
    # This approach was successful, but the response was not chunked
    file = requests.get('https://sample-videos.com/img/Sample-jpg-image-1mb.jpg')
    response = FileResponse(file)
    response['Content-Disposition'] = f'attachment; filename=example.jpg'
    return response
