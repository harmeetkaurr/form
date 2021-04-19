from django.shortcuts import render
from .form import College_Form, StuDent_Form, Login


def college_form(request):

    if request.method == 'POST':
        form = College_Form(request.POST)

        if form.is_valid():
            form.save()

    else:
        form = College_Form()
    return render(request, "polls/college_form.html", {'form': form})



def school_form(request):

    if request.method == 'POST':
        form = StuDent_Form(request.POST)

        if form.is_valid():
            form.save()

    else:
        form = StuDent_Form()
    return render(request, "polls/student_form.html", {'form': form})



def login(request):

    if request.method == 'POST':
        form = Login(request.POST)

        if form.is_valid():
            form.save()

    else:
        form = Login()
    return render(request, "polls/login.html", {'form': form})