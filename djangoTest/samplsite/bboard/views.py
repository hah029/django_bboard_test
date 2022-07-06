from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse
from django.template import loader

from .models import Bb
from .models import Rubric

# def index(request):
#
#     s = 'Список объявлений\r\n\r\n\r\n'
#     for bb in Bb.objects.order_by('-published'):
#         s += bb.title + '\r\n' + str(bb.published) + '\r\n\r\n'
#
#     return HttpResponse(s, content_type='text/plain; charset=utf-8')

# def index(request):
#     template = loader.get_template('bboard/index.html')
#     rubrics = Rubric.objects.all()
#     bbs = Bb.objects.order_by('-published')
#     context = {'bbs': bbs, 'rubrics': rubrics}
#
#     return HttpResponse(template.render(context, request))

def index(request):
    rubrics = Rubric.objects.all()
    bbs = Bb.objects.order_by('-published')
    context = {'bbs': bbs, 'rubrics': rubrics}
    return render(request, 'bboard/index.html', context)

def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs,
               'rubrics': rubrics,
               'current_rubric': current_rubric,
    }
    return render(request, 'bboard/by_rubric.html', context)

# Create Form for adding, modifying and deleting records of Bb
from django.views.generic.edit import CreateView
from .forms import BbForm
from django.urls import reverse_lazy

class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = reverse_lazy('index§')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context