from django.shortcuts import render, get_object_or_404, get_list_or_404, reverse
from django.http import HttpResponse
from .models import Project, ProjectGroup, ProjectImage
from .utils import url_to_pdf


def project_view(request, uri):
    project = get_object_or_404(Project, uri=uri)
    return render(request, 'project.html', {
        'project': project,
    })


def group_view(request, uri):
    group = get_object_or_404(ProjectGroup, uri=uri)
    return render(request, 'group.html', {
        'group': group,
    })


def home_view(request):
    groups = ProjectGroup.objects.all()
    return render(request, 'home.html', {
        'groups': groups,
    })


def pdf_view_html(request):
    return render(request, 'pdf/pdf.html', {
        'groups': ProjectGroup.objects.all(),
    })

def pdf_view(request):
    pdf = url_to_pdf(request.build_absolute_uri(reverse(pdf_view_html)))
    response = HttpResponse(pdf, content_type='application/pdf')
    return response

