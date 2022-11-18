from django.shortcuts import render
from django.http import StreamingHttpResponse, FileResponse
from itertools import count


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

    filename = 'JS41917_598474_US_RAIMUNDA NONATA DA SILVA FRANCA_DICOM'
    file_path = f'example/assets/{filename}.zip'
    
    # response = StreamingHttpResponse(file_iterator(file_path), content_type='application/octet-stream')
    with open(file_path) as f:
        response = FileResponse(f)
        response['Content-Disposition'] = f'attachment; filename={filename}.zip'
        return response
