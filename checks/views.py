

# Create your views here.

from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.conf import settings
from django.core.files.storage import FileSystemStorage



from .models import Check
from django.http import HttpResponse, Http404
from .forms import SubmitCheckForm
from .processing.header import XLdocument

import os



def checks_list(request):
    checks = Check.objects.all().order_by('init_date')
    return render(request, 'checks/checks_list.html', {'checks': checks})


def check_details(request, pk):
    try:
        check = Check.objects.get(pk=pk)
    except:
        resp = render(request, '404.html')
        resp.status_code = 404
        return resp

    return render(request, 'checks/check_details.html', {'check': check})


def check_new(request):
    if request.method == "POST":
        form = SubmitCheckForm(request.POST)
        if form.is_valid():
            check = form.save(commit=False)
            check.author = request.user
            check.init_date = timezone.now()
            check.save()
            return redirect('check_details', pk=check.pk)
    else:
        form = SubmitCheckForm()
    return render(request, 'checks/check_new.html', {'form': form})


def check_edit(request, pk):
    check = get_object_or_404(Check, pk)
    if (request.method == "POST"):
        form = SubmitCheckForm(request.POST)
    return HttpResponse("editing cceck")




def direct_file(request):
    if (request.method == "POST" and request.FILES['upload']):
        ufile = request.FILES['upload']
        fs = FileSystemStorage()
        filename = fs.save(ufile.name, ufile)
        doc = XLdocument(5000000,
                         os.path.join(settings.MEDIA_ROOT, filename),
                         proft_path = os.path.join(settings.MEDIA_ROOT, filename + "_profit.xlsx"),
                         loss_path = os.path.join(settings.MEDIA_ROOT, filename + "_loss.xlsx"),
                         )
        doc.search_and_devide()

        uploaded_file_url = fs.url(filename)
        return render(request, 'checks/direct_file.html', {
            'uploaded_file_url': uploaded_file_url,
            'name': filename,
        })
    return render(request, 'checks/direct_file.html')
