from django.shortcuts import render
from django.views.generic import TemplateView


class ProjectListView(TemplateView):
    template_name = 'project_list.html'