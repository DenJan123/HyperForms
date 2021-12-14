from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from . import forms
from . import models
from django.views.decorators.csrf import csrf_protect
from itertools import groupby


# Create your views here.

def index(request):
    # To make life easier I populate fields in db in index call for testing purposes

    # model_form = models.FormModel.objects.get_or_create(name='participants')[0]
    # name = models.FormField.objects.get_or_create(name='name', label='your name', type='text', form=model_form.id)
    # age = models.FormField.objects.get_or_create(name='age', label='your age', type='number', form=model_form)
    # favorite_book = models.FormField.objects.get_or_create(name='favorite_book', label='your favorite book',
    #                                                        type='text', form=model_form)

    ##################
    # that is a workaround for the test, otherwise they don't work
    ##################
    model_form = models.FormModel.objects.all()
    if not model_form:
        return render(request, 'index.html')
    else:
        model_form = model_form.get(name='participants')
    #################
    fields = list(models.FormField.objects.all().values('name'))
    res = models.FormData.objects.filter(form_id=models.FormModel.objects.filter(name='participants').first().id)
    data = [list(group) for _, group in groupby(res, key=lambda x: getattr(x, 'record_id'))]
    # participants = list(zip(*participants))
    return render(request, 'index.html', context={
        # 'participants': participants,
        'fields': fields,
        'data': data
    })


@csrf_protect
def register(request):
    form = forms.RegisterForm()
    form_fields = models.FormField.objects.filter(form__name='participants')
    if request.method == "GET":
        return render(request, 'register.html', context={
            'form_fields': form_fields
        })
    elif request.method == "POST":
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            record = models.FormRecord()
            record.save()
            for field in form_fields:
                form_data = models.FormData()
                form_data.form_id = field.form.id
                form_data.field_id = field.id
                form_data.value = request.POST[field.name]
                form_data.record_id = record.id
                form_data.save()
            return redirect('/')
