from django.shortcuts import render, get_object_or_404, get_list_or_404, reverse
from django.http import HttpResponse
from django.conf import settings
from .models import Project, ProjectGroup, ProjectImage, Profile
from .utils import url_to_pdf


def project_view(request, uri):
    return render(request, 'project.html', {
        'project': get_object_or_404(Project, uri=uri),
        'profile': get_object_or_404(Profile, uri=settings.PORTFOLIO_PROFILE),
    })


def group_view(request, uri):
    return render(request, 'group.html', {
        'group': get_object_or_404(ProjectGroup, uri=uri),
        'profile': get_object_or_404(Profile, uri=settings.PORTFOLIO_PROFILE),
    })


def home_view(request):
    return render(request, 'home.html', {
        'groups': ProjectGroup.objects.all(),
        'profile': get_object_or_404(Profile, uri=settings.PORTFOLIO_PROFILE),
    })


def pdf_view_html(request):
    return render(request, 'pdf/pdf.html', {
        'groups': ProjectGroup.objects.all(),
        'profile': get_object_or_404(Profile, uri=settings.PORTFOLIO_PROFILE),
    })


def pdf_view(request):
    url = request.GET.get('url', request.build_absolute_uri(reverse(pdf_view_html)))
    pdf = url_to_pdf(url)
    response = HttpResponse(pdf, content_type='application/pdf')
    return response

