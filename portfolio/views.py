from django.shortcuts import render, get_object_or_404, get_list_or_404, reverse, render_to_response
from django.http import HttpResponse
from django.conf import settings
from django.template import RequestContext
from .models import Project, ProjectGroup, ProjectImage, Profile
from .utils import url_to_pdf


def context_processor(request):
    return {
        'profile': get_object_or_404(Profile, uri=settings.PORTFOLIO_PROFILE),
        'groups': ProjectGroup.objects.all(),
    }


def project_view(request, uri):
    return render(request, 'project.html', {'project': get_object_or_404(Project, uri=uri)})


def group_view(request, uri):
    return render(request, 'group.html', {'group': get_object_or_404(ProjectGroup, uri=uri)})


def home_view(request):
    return render(request, 'home.html')


def printable_view(request):
    return render(request, 'printable.html')


def pdf_view(request):
    url = request.GET.get('url', request.build_absolute_uri(reverse(printable_view)))
    return HttpResponse(url_to_pdf(url), content_type='application/pdf')

