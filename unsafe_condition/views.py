from django.shortcuts import render, redirect
from .forms import UnsafeConditionForm

# Create your views here.

from django.shortcuts import render, redirect
from .forms import UnsafeConditionForm

def report_unsafe_condition(request):
    """View for reporting an unsafe condition."""
    if request.method == 'POST':
        form = UnsafeConditionForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form data to the database
            unsafe_condition = form.save(commit=False)
            unsafe_condition.save()
            form.save_m2m()
            return redirect('unsafe_condition:success')
    else:
        form = UnsafeConditionForm()

    context = {'form': form}
    return render(request, 'unsafe_condition/report_unsafe_condition.html', context)

def unsafe_condition_success(request):
    """View for displaying the success message after reporting an unsafe condition."""
    return render(request, 'unsafe_condition/unsafe_condition_success.html')