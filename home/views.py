from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Project, ProjectGroup, ProjectImage


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
