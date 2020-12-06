from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ArchiveForm
from .models import Archive


def home(request):
    archives = Archive.objects.all()
    return render(request, 'archive/index.html', {'archives': archives})


def project_page(request):
    return render(request, 'archive/project_page.html')


def adminpage(request):
    return render(request, 'archive/adminbase.html')


def admin_home(request):
    return render(request, 'archive/admin-home.html')


def add_project(request):

    if request.method == "POST":
        print("POST")
        form = ArchiveForm(request.POST, request.FILES)
        if form.is_valid():
            new_archive = form.save(commit=False)
            # user = User.objects.get(id=request.user.id)
            new_archive.added_by = request.user
            new_archive.save()
            return redirect('archive-home')
        else:
            print("form not valid")
            form = ArchiveForm()
            return render(request, 'archive/add-project.html', {'form': form})
    else:
        form = ArchiveForm()
        return render(request, 'archive/add-project.html', {'form': form})


def assign_project(request):
    return render(request, 'archive/assign-project.html')


def submitted_project(request):
    return render(request, 'archive/submitted-project.html')


def student_home(request):
    return render(request, 'archive/student-dashboard-home.html')


def student_submit_project(request):
    return render(request, 'archive/student-submit-project.html')
