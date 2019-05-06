from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponseForbidden, HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse
from authapp.models import User
from groupapp.models import GroupUser, Group
from taskapp.forms import NewTaskForm, TaskEditForm
from taskapp.models import Task

# Create your views here.

@login_required
def view_tasks_list(request, group_pk):
    '''
    Просмотр списка задач группы по pk группы
    '''

    friendlyuser = GroupUser.objects.filter(group=group_pk, user=request.user.pk)
    if not friendlyuser:
        return HttpResponseForbidden()

    donelist = Task.objects.filter(group=group_pk, done=True)
    todolist = Task.objects.filter(group=group_pk, done=False)

    content = {
        'done': donelist,
        'todo': todolist,
        'group_pk': group_pk
    }

    return render(request, 'taskapp/taskslist.html', content)

@login_required
def checkbox_tasks_list(request, task_pk, group_pk):
    '''
    Функция меняет статут выполнено/невыполнено через чекбокс без захода на страницу редактирования
    '''

    if request.is_ajax():
        task_item = Task.objects.get(pk=task_pk)
        if task_item.done == False:
            task_item.done = True
            task_item.save()
        else:
            task_item.done = False
            task_item.save()

        donelist = Task.objects.filter(group=group_pk, done=True)
        todolist = Task.objects.filter(group=group_pk, done=False)

        content = {
            'group_pk': group_pk,
            'done': donelist,
            'todo': todolist,
        }

        result = render_to_string('taskapp/includes/inc_task_ajax.html', content)
        return JsonResponse({'result': result})
    else:
        return Http404

@login_required
def newtaskpage(request, group_pk):
    '''
    Добавление задачи в группе
    '''

    friendlyuser = GroupUser.objects.filter(group=group_pk, user=request.user.pk)
    if not friendlyuser:
        return HttpResponseForbidden()

    form = NewTaskForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            response = form.save(commit=False)
            group = get_object_or_404(Group, pk=group_pk)
            response.group = group
            response.save()
            form.save_m2m()
            return HttpResponseRedirect(reverse('taskapp:taskslist', args = [group_pk]))
    else:
        formuser = User.objects.filter(pk__in=GroupUser.objects.filter(group=group_pk).values_list('user'))
        form = NewTaskForm()
        form.fields['user'].queryset = formuser

    content = {
        'newtask_form': form,
        'group_pk': group_pk
    }

    return render(request, 'taskapp/newtask.html', content)

@transaction.atomic
def taskedit(request, group_pk, task_pk):
    '''
    Просмотр/изменение покупки группы
    '''

    friendlyuser = GroupUser.objects.filter(group=group_pk, user=request.user.pk)
    if not friendlyuser:
        return HttpResponseForbidden()

    task = get_object_or_404(Task, pk=task_pk)
    form = TaskEditForm(request.POST, instance=task)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('taskapp:taskslist', args=[group_pk]))
    else:
        form = TaskEditForm(instance=task)
        formuser = User.objects.filter(pk__in=GroupUser.objects.filter(group=group_pk).values_list('user'))
        form.fields['user'].queryset = formuser

    content = {
        'taskedit_form': form,
        'group_pk': group_pk,
        'task_pk': task_pk,
    }

    return render(request, 'taskapp/taskedit.html', content)

@login_required
def taskremove(request, task_pk, group_pk):
    '''
    Удаление покупки
    '''

    friendlyuser = GroupUser.objects.filter(group=group_pk, user=request.user.pk)
    if not friendlyuser:
        return HttpResponseForbidden()

    item = get_object_or_404(Task, pk=task_pk)
    item.delete()
    return HttpResponseRedirect(reverse('taskapp:taskslist', args=[group_pk]))

