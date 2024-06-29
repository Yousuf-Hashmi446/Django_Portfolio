from django.shortcuts import render, redirect

from .models import Header, AboutMe, Education, Skill, Project, Contact

# Create your views here.
def index(request):
    header = Header.objects.first()
    about_me = "Hey there! I'm Muhammad Yousaf, a BS Computer Science student. I'm passionate about coding and all things tech-related. My journey into the world of software engineering started a few years ago, and since then, I've been immersed in learning various programming languages and exploring different aspects of software development. In my free time, you'll often find me tinkering with code, working on personal projects, or diving into the latest tech trends. I believe that technology has the power to shape the future, and I'm excited to be part of that journey. This space is where I share my experiences, challenges, and insights as I navigate through my software engineering journey. Join me as I continue to learn, grow, and explore the ever-evolving world of technology!"
    education = Education.objects.all()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    return render(request, 'index.html', {
        'header': header,
        'about_me': about_me,
        'education': education,
        'skills': skills,
        'projects': projects,
    })

def contact(request):
    return render(request, 'contact.html')


def submit_contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Contact.objects.create(name=name, email=email, message=message)
        return redirect('index')
    return redirect('contact')