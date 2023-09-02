from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Create your views here.


def SignupView(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")

    else:
        form = CustomUserCreationForm()
    return render(request, "registration/signup.html", context={"form": form})
