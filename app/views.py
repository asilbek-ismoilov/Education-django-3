from django.shortcuts import render, redirect
from .models import Courses, Comments, Instructors
from .forms import ContactForm
            
def home_view(request):
    return render(request, "index.html")

def about_view(request):
    return render(request, "about.html")

def team_view(request):
    teams = Instructors.objects.all()
    context = { 
        "temas": teams, 
    }
    return render(request, "team.html", context)

def testimonial_view(request):
    comments = Comments.objects.all()
    context = {
        
        "comments":comments,
    }
    return render(request,'testimonial.html', context)


def courses_view(request):
    courses = Courses.objects.all()
    context = {
        
        "courses":courses,
    }
    return render(request,'courses.html', context)

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact-page')  # Bu yerda 'contact-page' deb o'zgartiramiz
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})