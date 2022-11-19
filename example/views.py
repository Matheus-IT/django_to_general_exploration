import requests
from django.shortcuts import render
from django.http import StreamingHttpResponse, FileResponse
from itertools import count
from django.conf import settings
from django.templatetags.static import static




def home_view(request):
    return render(request, 'example/home.html')

def download_view(request):
    def file_iterator(file_response, chunk_size=512):
        for c in file_response.iter_content(chunk_size):
            if c:
                yield c
            else:
                break

    # This solution returns
    URL = 'https://sample-videos.com/img/Sample-jpg-image-1mb.jpg'
    file_response = requests.get(URL, stream=True)
    response = StreamingHttpResponse(file_iterator(file_response))
    response['Content-Disposition'] = f'attachment; filename=example.jpeg'
    return response

    # # In this approach the request to the file is chunked
    # URL = 'https://sample-videos.com/img/Sample-jpg-image-1mb.jpg'
    # file = requests.get(URL, stream=True)
    # response = FileResponse(file)
    # response['Content-Disposition'] = f'attachment; filename=example.jpeg'
    # return response

    # # In this approach the response was not chunked, and the file is not opening
    # URL = 'https://sample-videos.com/img/Sample-jpg-image-1mb.jpg'
    # file = requests.get(URL)
    # response = FileResponse(file)
    # response['Content-Disposition'] = f'attachment; filename=example.zip'
    # return response
