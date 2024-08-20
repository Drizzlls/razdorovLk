from django.shortcuts import render
from django.views import View
from .models import Tasks

class TasksPage(View):
    """ Страница Задач """
    template_name = 'tasks/tasksList.html'

    def get(self, request):
        context = {
            'tasks': Tasks.objects.all()
        }
        return render(request, self.template_name, context=context)
