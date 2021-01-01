from django.shortcuts import render

import json
import urllib.request


# Create your views here.
def render_page(request):
    projects = get_work_items()
    sliders = []
    project_list = [21, 1, 16, 13]

    for i in project_list:
        text_url = urllib.request.urlopen(f'http://localhost:8000/image/project_text?project_id={i}')
        text_json = json.load(text_url)
        text = text_json["text"].replace('Residential', '').replace('Commercial', '').split(',')

        slider = {
            "img": f"image/slider_image?slider_id={i}",
            "caption": text[0],
            "title": text[1]
        }
        sliders.append(slider)

    context = {
        'sliders': sliders,
        'projects': projects
    }
    return render(request, 'base.html.j2', context=context)


def get_work_items():
    projects = []
    projects_url = urllib.request.urlopen('http://localhost:8000/image/projects')
    projects_json = json.load(projects_url)
    print(projects_json)
    len_projects = len(projects_json["projects"])
    for i in range(1, len_projects):
        text_url = urllib.request.urlopen(f'http://localhost:8000/image/project_text?project_id={i}')
        text_json = json.load(text_url)
        text = text_json["text"]
        text = text.replace("Commercial", "").replace("Residential", "")
        print(text)
        # = urllib.request.urlopen()
        project = {
            "main_image": f'http://localhost:8000/image/project_image?project_id={i}',
            "image": f'http://localhost:8000/image/project_cover_image?project_id={i}',
            "title": "",
            "description": text
        }
        projects.append(project)
    return projects



