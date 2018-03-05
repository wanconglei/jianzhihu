from django.shortcuts import render
from .models import Issue, Answer, Attitude


# Create your views here.
def index(request):
    answer_list = Answer.objects.all()
    context = {'answer_list': answer_list}
    return render(request, 'zhihu_index.html', context=context)