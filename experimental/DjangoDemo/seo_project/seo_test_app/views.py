from django.shortcuts import render, redirect
from .forms import DLForm
from .models import Drug, Liquor

# Create your views here.
def seo_list(request):
    drug = Drug.objects.all()
    liquor = Liquor.objects.all()
    return render(request, 'seo_test_app/seo_list.html', {'drug': drug, 'liquor': liquor})


def seo_create(request):
    form = DLForm(data=request.POST)
    if request.method == 'POST':
        print(form.is_valid())
        if form.is_valid():
            if request.POST.get('dorl', '') == 'Drug':
                Drug.objects.create(
                    title=form.cleaned_data['title'],
                    description=form.cleaned_data['description'],
                    type=form.cleaned_data['type']
                )
                return redirect('seo_list')
            elif request.POST.get('dorl', '') == 'Liquor':
                Liquor.objects.create(
                    title=form.cleaned_data['title'],
                    description=form.cleaned_data['description'],
                    type=form.cleaned_data['type']
                )
                return redirect('seo_list')
    return render(request, 'seo_test_app/seo_create.html', {'form':form})


def seo_drug_edit(request, id):
    drug = Drug.objects.get(pk=int(id))
    form = DLForm(data=request.POST)
    if request.method == 'POST':
        print(form.is_valid())
        if form.is_valid():
            drug.title = form.cleaned_data['title']
            drug.description = form.cleaned_data['description']
            drug.type = form.cleaned_data['type']
            drug.save()
            return redirect('seo_list')
    return render(request, 'seo_test_app/seo_drug_edit.html', {'form': form, 'drug': drug})


def seo_drug_delete(request, id):
    Drug.objects.get(pk=int(id)).delete()
    return redirect('seo_list')


def seo_liquor_edit(request, id):
    liquor = Liquor.objects.get(pk=int(id))
    form = DLForm(data=request.POST)
    if request.method == 'POST':
        print(form.is_valid())
        if form.is_valid():
            liquor.title = form.cleaned_data['title']
            liquor.description = form.cleaned_data['description']
            liquor.type = form.cleaned_data['type']
            liquor.save()
            return redirect('seo_list')
    return render(request, 'seo_test_app/seo_liquor_edit.html', {'form': form, 'liquor': liquor})


def seo_liquor_delete(request, id):
    Liquor.objects.get(pk=int(id)).delete()
    return redirect('seo_list')