import json

from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import DetectionForm
from .models import PisImage
from pi_detection.detection import Detector


def test(request):
    if request.method == 'GET':
        return render(request, 'api/test.html', {
            'form': DetectionForm(),
            'images':PisImage.objects.all(),
        })

    elif request.method == 'POST':
        form = DetectionForm(request.POST, request.FILES)
        if not form.is_valid():
            raise ValueError('invalid form')

        image = PisImage()
        image.image = form.cleaned_data['image']
        image.save()

        return render(request, 'api/test.html', {
            'form': DetectionForm(),
            'images':PisImage.objects.all(),
        })

def detection(request):
    if request.method == 'GET':
        return render(request, 'api/detection.html', {
            'form': DetectionForm(),
            'result':{},
        })
    if request.method == 'POST':
        detctor = Detector()
        form = DetectionForm(request.POST, request.FILES)
        if not form.is_valid():
            raise ValueError('invalid form')

        # 画像の保存 media/
        image = PisImage()
        image.image = form.cleaned_data['image']
        image.save()
        # 最後に登録した画像のidとパス取得
        info = PisImage.objects.order_by('-id').all()[:1].values()
        _id = info[0]['id']
        img_path = info[0]['image']
        # detectを読んで画像の牌情報をとる
        _result = detctor.detect('media/'+img_path)
        # 結果の整形
        _result['image_id'] = int(_id)
        result = json.dumps(_result)
        # レスポンス
        return HttpResponse(result, content_type='application/json')


    error_res = {
                  "error":{
                    "message":"error"
                  }
                }
    result = json.dumps(error_res)
    return HttpResponse(result, content_type='application/json', status=400)

