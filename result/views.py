from django.shortcuts import render
from result.models import Show


def result_list(request):
    return render(request, 'result_list.html')


def show_1(request):
    show = Show.objects.get(pk=1)
    return render(request, 'show_1.html', {'show': show})


def show_2(request):
    show = Show.objects.get(pk=2)
    return render(request, 'show_2.html', {'show': show})


def show_3(request):
    show = Show.objects.get(pk=3)
    return render(request, 'show_3.html', {'show': show})


def show_4(request):
    show = Show.objects.get(pk=4)
    return render(request, 'show_4.html', {'show': show})


def show_5(request):
    show = Show.objects.get(pk=5)
    return render(request, 'show_5.html', {'show': show})