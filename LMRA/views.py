from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import LMRA, Hazard
from .forms import LMRAForm, HazardFormSet
from django.contrib.auth.decorators import login_required

# Create your views here.

#LMRA Creation
def create_LMRA(request):
    """Create LMRA with linked hazar forms"""
    if request.method == 'POST':
        lmra_form = LMRAForm(data=request.POST)
        hazard_formset = HazardFormSet(data=request.POST)

        if lmra_form.is_valid() and hazard_formset.is_valid():
            lmra = lmra_form.save(commit=False)
            lmra.owner = request.user
            lmra.save()

            for form in hazard_formset:
                hazard = form.save(commit=False)
                hazard.lmra = lmra
                hazard.save()
            return redirect('/')
    else:
        lmra_form = LMRAForm()
        hazard_formset = HazardFormSet()
    
    context = {'lmra_form': lmra_form, 'hazard_formset': hazard_formset}
    return render(request, 'LMRA/create_LMRA.html', context)

def homepage(request):
    return render(request, 'LMRA/home.html')


#View to see LMRA's
def lmras(request):
    """Shows all LMRA's"""
    lmras = LMRA.objects.order_by('date_added')
    context = {'lmras': lmras }
    return render(request, 'LMRA/lmras.html', context)

class lmra(DetailView):
    """Show single LMRA"""
    model = LMRA
    template_name = 'LMRA/lmra.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hazards'] = self.object.hazard_set.all()
        return context