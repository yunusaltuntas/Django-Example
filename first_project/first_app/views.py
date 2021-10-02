from django.shortcuts import render
from first_app.models import Topic, Webpage, AccessRecord, User
from . import forms


# Create your views here.


def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request, "first_app/index.html", context=date_dict)


def help(request):
    my_dict = {"help_me": "help page"}
    return render(request, "first_app/help.html", context=my_dict)


def index2(request):
    return render(request, "first_app/login.html")


def user(request):
    print("hello", flush=True)
    user_list = User.objects.order_by('first_name')
    print(user_list, flush=True)
    user_dict = {'users': user_list}
    return render(request, "first_app/users.html", context=user_dict)


def form_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print("validation success")
            print("name: " + form.cleaned_data["name"])
            print("email: " + form.cleaned_data["email"])
            print("text: " + form.cleaned_data["text"])
        else:
            print("validation dont success")

    return render(request, "first_app/form.html", {"form": form})
