from django.shortcuts import render, get_object_or_404, redirect
from .models import Issue, Answer, Attitude
from .forms import IssueForm, AnswerForm


# Create your views here.
def zhihu_index(request):
    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            anonymity = form.cleaned_data['anonymity']
            print(title, description, anonymity)
            issue = Issue(author=request.user, title=title, description=description, anonymity=anonymity)
            issue.save()
            return redirect('zhihu:zhihu_index')

    answer_list = Answer.objects.all()
    context = {'answer_list': answer_list}
    return render(request, 'zhihu_index.html', context=context)


def detail(request, pk):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            anonymity = form.cleaned_data['anonymity']
            issue = Issue.objects.get(pk=pk)
            answer = Answer(author=request.user, issue=issue, content=content, anonymity=anonymity)
            answer.save()
            return redirect('zhihu:detail', pk=pk)
    issue = get_object_or_404(Issue, pk=pk)
    return render(request, 'detail.html', context={'issue': issue})