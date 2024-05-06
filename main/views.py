from django.shortcuts import render
from .forms import RecordForm


def main(request):
    message = 'Мы ждём Вас!'
    return render(request, 'base.html', {'message': message})


def add_record(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            message = 'Вы успешно записались.Ждём Вас с нетерпением!'
            return render(request, 'base.html', {'message': message})
    else:
        form = RecordForm()
        return render(request, 'main/record_client.html', {'form': form})
