from django.shortcuts import render
from django.http import StreamingHttpResponse, FileResponse
from itertools import count
from django.conf import settings
from django.templatetags.static import static




def home_view(request):
    return render(request, 'example/home.html')

def download_view(request):
    pass
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
    
    # This alternative worked, but the download was incomplete:
    # file_url = static('images/example.jpg')
    # response = FileResponse(file_url)
    # response['Content-Disposition'] = f'attachment; filename=example.zip'
    # return response
