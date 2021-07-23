from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, PatientProfilUpdateForm

# Update Profile
@login_required
def patient_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = PatientProfilUpdateForm(request.POST,
                                         request.FILES,
                                         instance=request.user.patientprofile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Profile has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = PatientProfilUpdateForm(instance=request.user.patientprofile)


    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/patient_profile.html', context)
