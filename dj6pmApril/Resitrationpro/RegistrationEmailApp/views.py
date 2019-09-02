from django.shortcuts import render
from .forms import RegistrationForm

def accounts_register(request):
    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']

            # Save the User object
            user.save()
    else:
        registerForm = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': registerForm})