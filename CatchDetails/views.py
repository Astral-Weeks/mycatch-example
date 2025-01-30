from django.shortcuts import render
from .models import Catch, Species, Subspecies
from .forms import CatchForm
from django.contrib import messages
from django.views.generic import CreateView

# Create your views here.

def home(request):
    return render(request, 'index.html')

def submit_a_catch(request):
    context = {}
    context['form'] = CatchForm()
    # a = Catch()
    f = CatchForm(request.POST)
    if request.method == 'POST':    
        f = CatchForm(request.POST, request.FILES)
        # j = f.cleaned_data()
        print(f.errors)
        if f.is_valid():
            f.save()
            messages.success(request, 'Thank you. Your comment has been sent successfully')
            return render(request, 'thankyouforyoursubmission.html', context)
        else:
            messages.error(request, 'Something went wrong. Please try again.')
    return render(request, 'catch.html', context)



# def catch(request):
    # if request.method == 'GET':
    #     return render(request, 'catchinitial.html')
    # if request.method == 'POST':
    #     species = request.GET.get("species")
    #     if species == "trout":
    #         return render(request, 'home.html')

# def catch(request):
#     context = {}
#     context['form'] = CatchForm()
#     a = Catch()
#     f = CatchForm(request.POST, instance=a)
#     return render(request, 'catch.html', context)
    
# def catch(request):
#     if request.method == "GET":
#         context = {}
#         context['form'] = CatchForm()
#         a = Catch()
#         f = CatchForm(request.POST, instance=a)
#         return render(request, 'catch.html', context)
#     if request.method == "POST":
#         context = {}
#         context['form'] = CatchForm()
#         a = Catch()
#         f = CatchForm(request.POST, instance=a)
#         if f.is_valid():
#             f.save()
#             messages.success(request, 'Thank you. Your comment has been sent successfully')
#             return render(request, 'thankyouforyoursubmission.html', context)
#         else:
#             messages.error(request, 'Something went wrong. Please try again.')
#             return render(request, 'index.html', context)


# class catch(CreateView):
#     form_class = CatchForm
#     template_name = "catch.html"

#     def get(self, request):
#         context = {}
#         context['form'] = CatchForm()
#         a = Catch()
#         f = CatchForm(request.POST, instance=a)
#         return render(request, 'catch.html', context)

#     def post(self, request, *args):
#         if request.method == "POST":
#             context = {}
#             context['form'] = CatchForm()
#             a = Catch()
#             f = CatchForm(request.POST, instance=a)
#             if f.is_valid():
#                 f.save(commit=False)
#                 f.save()
#                 messages.success(request, 'Thank you. Your comment has been sent successfully')
#                 return render(request, 'thankyouforyoursubmission.html', context)
#             else:
#                 messages.error(request, 'Something went wrong. Please try again.')
#             return render(request, 'index.html', context)


def load_subspecies(request):
    species_id = request.GET.get('species')
    subspecies = Subspecies.objects.filter(species=species_id)
    return render(request, 'subspecies_options.html', {"subspecies": subspecies})