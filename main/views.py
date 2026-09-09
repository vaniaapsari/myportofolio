
# Create your views here.

from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "name": "Vania",
        "npm": "2506615103",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Mahasiswa Fakultas Ilmu Komputer Universitas Indonesia yang sedang "
            "belajar Pemrograman Berbasis Platform."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Vania",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)
