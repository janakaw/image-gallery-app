from django.shortcuts import render
from django.http import FileResponse, HttpResponse, HttpResponseNotFound, JsonResponse

from .utils import ProjectUtils


def get_projects(request):
    projects = ProjectUtils.get_projects()
    test_projects = {"projects": projects}
    return JsonResponse(test_projects)


def get_project_image(request):
    project_id = request.GET.get('project_id', '0')
    try:
        proj_utils = ProjectUtils()
        img = proj_utils.get_project_cover_image(project_id)
        return FileResponse(img)
    except Exception as e:
        return HttpResponseNotFound(str(e))


def get_project_text(request):
    project_id = request.GET.get('project_id', '0')
    try:
        proj_utils = ProjectUtils()
        text = proj_utils.get_project_text(project_id)
        response = { "text": text}
        return JsonResponse(response)
    except Exception as e:
        return HttpResponseNotFound(str(e))


def get_slider_image_count(request):
    try:
        proj_utils = ProjectUtils()
        count = proj_utils.get_slider_image_count()
        return HttpResponse(count)
    except Exception as e:
        return HttpResponseNotFound(str(e))


def get_slider_image(request):
    slider_id = request.GET.get('slider_id', '0')
    try:
        proj_utils = ProjectUtils()
        return FileResponse(proj_utils.get_slider_image(slider_id))
    except Exception as e:
        return HttpResponseNotFound(str(e))


def get_slider_text(request):
    slider_id = request.GET.get('slider_id', '0')
    try:
        proj_utils = ProjectUtils()
        return JsonResponse(proj_utils.get_slider_text(slider_id))
    except Exception as e:
        return HttpResponseNotFound(str(e))
