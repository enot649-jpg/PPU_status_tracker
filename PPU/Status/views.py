import pandas
import sqlite3
import os
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.db.models import Sum, Count
from .models import Sogl, History
from .forms import UnitForm, NewForm, DepartureForm, ActForm
from rest_framework import generics
from .serializers import SoglSerializer


def sogl(request):
    unit_query = request.GET.get('unit', '').strip()
    departure_query = request.GET.get('departure', '').strip()
    act_query = request.GET.get('needs_act', '').strip()
    for_sum = Sogl.objects.all()
    if unit_query:
        for_sum = for_sum.filter(unit_id=unit_query)
    if departure_query:
        for_sum = for_sum.filter(departure_id=departure_query)
    if act_query:
        for_sum = for_sum.filter(needs_act_id=act_query)
    totals = for_sum.aggregate(
        val = Sum('value'),
        pay = Sum('payed'),
        count = Count('name'),
        )
    sum_val = totals['val'] or 0
    sum_pay = totals['pay'] or 0
    count_el = totals['count'] or 0
    if sum_val != 0:
        percent = sum_pay / sum_val * 100
    else:
        percent = 0
    sogl_list = for_sum.values(
    'id', 'group', 'name', 'value', 'payed', 'status', 'unit__unit',
    'departure__departure', 'needs_act__needs_act'
    ).order_by('group')
    template ='main/sogl.html'
    context = {
    'sogl_list':sogl_list,
    'sum_val': sum_val,
    'sum_pay': sum_pay,
    'count_el': count_el,
    'percent': percent,
    'form2': UnitForm(initial={'unit': unit_query}),
    'form3': DepartureForm(initial={'departure': departure_query}),
    'form4': ActForm(initial={'needs_act': act_query}),
    }
    return render(request, template, context)

def delete_sogl(request, pk):
    instance = get_object_or_404(Sogl, id=pk)
    template ='main/delete.html'
    context = {'object': instance,}
    if request.method == 'POST':
        instance.delete()
        return redirect('Status:sogl')
    return render(request, template, context)

def create_sogl(request):
    form = NewForm(request.POST or None)
    template ='main/create.html'
    context = {'form': form,}
    if form.is_valid() and request.method == 'POST':
        saved = form.save()
        History.objects.create(
            status = saved.status,
            name = saved
            )
        return redirect('Status:sogl')
    return render(request, template, context)

def edit_sogl(request, pk):
    instance = get_object_or_404(Sogl, id=pk)
    template ='main/edit.html'
    if request.method == 'POST':
        old1 = instance.status
        old2 = instance.payed
        form = NewForm(request.POST or None, instance=instance)
        if form.is_valid():
            saved = form.save()
            if old1 != saved.status or old2 != saved.payed:
                History.objects.create(
                status = saved.status,
                payed = saved.payed,
                name = saved
                )
        return redirect('Status:sogl')
    else:
        form = NewForm(instance=instance)
    return render(request, template, {'form': form,})

def export_sogl(request):
    template ='main/export.html'
    db_path = os.path.join(settings.BASE_DIR, 'db.sqlite3')
    file_path = os.path.join(settings.BASE_DIR, 'sogl.xlsx')
    start = sqlite3.connect(db_path)
    query = 'SELECT * FROM Status_sogl ORDER BY departure_id, "group"'
    read = pandas.read_sql_query(query, start)
    read.to_excel(file_path, index=False)
    start.close()
    return render(request, template)

def history_sogl(request, pk):
    sogl = get_object_or_404(Sogl, id=pk)
    history = History.objects.filter(name=sogl).order_by('-date')
    template ='main/history.html'
    context = {
    'sogl': sogl,
    'history': history
    }
    return render(request, template, context)


class SoglListAPIView(generics.ListAPIView):
    queryset = Sogl.objects.all()
    serializer_class = SoglSerializer

