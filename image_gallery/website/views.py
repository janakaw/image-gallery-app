from django.shortcuts import render


# Create your views here.
def render_page(request):
    return render(request, 'base.html.j2')
