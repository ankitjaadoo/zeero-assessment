from django.shortcuts import render
from .forms import TimerForm

def countdown_view(request):
    form = TimerForm(request.POST or None)
    context = {'form': form}

    if form.is_valid():
        hours = form.cleaned_data.get('hours')
        minutes = form.cleaned_data.get('minutes')
        seconds = form.cleaned_data.get('seconds')

        # Convert time to total seconds
        total_seconds = hours * 3600 + minutes * 60 + seconds
        context['total_seconds'] = total_seconds

    return render(request, 'countdown.html', context)