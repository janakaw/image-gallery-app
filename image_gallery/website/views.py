from django.shortcuts import render

import json
import urllib.request


# Create your views here.
def render_page(request):
    projects = get_work_items()
    sliders = []
    project_list = [
        {
            "proj_id": "14",
            "image_id": "H900-0"
        },
        {
            "proj_id": "17",
            "image_id": "H900-16"
        },
        {
            "proj_id": "26",
            "image_id": "H900-1"
        },
        {
            "proj_id": "29",
            "image_id": "H900-17"
        }
    ]

    for i in project_list:
        text_url = urllib.request.urlopen(f'http://localhost:8000/image/project_text?project_id={i["proj_id"]}')
        text_json = json.load(text_url)
        text = text_json["text"].replace('Residential', '').replace('Commercial', '').split(',')

        slider = {
            "img": f'http://localhost:8000/image/project_image?project_id={i["proj_id"]}&image_id={i["image_id"]}',
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
        image_list = urllib.request.urlopen(f'http://localhost:8000/image/project_image_list?project_id={i}')
        images_json = json.load(image_list)
        text_json = json.load(text_url)
        text = text_json["text"]
        text = text.replace("Commercial", "").replace("Residential", "")

        image_url_list = []
        for j in images_json["images"]:
            image_url_list.append(f'http://localhost:8000/image/project_image?project_id={i}&image_id={j}')

        # = urllib.request.urlopen()
        project = {
            "id": f"project_{i}",
            "main_image": f'http://localhost:8000/image/project_image?project_id={i}',
            "image": f'http://localhost:8000/image/project_cover_image?project_id={i}',
            "images": image_url_list,
            "title": "",
            "description": text
        }
        projects.append(project)
    return projects



