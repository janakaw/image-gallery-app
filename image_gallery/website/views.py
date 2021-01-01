from django.shortcuts import render

import json
import urllib.request


# Create your views here.
def render_page(request):
    sliders = []
    for i in range(1, 5):
        slider_text_url = urllib.request.urlopen(f'http://localhost:8000/image/slider_text?slider_id={i}')
        slider_text = json.load(slider_text_url)
        print(slider_text)
        slider = {
            "img": f"image/slider_image?slider_id={i}",
            "caption": slider_text["title"],
            "title": slider_text["client"]
        }
        sliders.append(slider)

    context = {
        'sliders': sliders
    }
    return render(request, 'base.html.j2', context=context)
