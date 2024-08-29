from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.checks import messages
from django.core.paginator import EmptyPage, Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import ProfileForm,projectform,SkillForm
from .models import loginTable, profile,project,Skill


def loginuser(request):

    if request.method=="POST":
        username=request.POST.get("username")
        password = request.POST.get("password")

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('listinfo')




    return render(request,'login.html')



def logout(request):
    auth.logout(request)
    return redirect('login')


def registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')

        # Check if passwords match
        if password != password1:

            return redirect('registration')

        # Check if username is already taken
        if User.objects.filter(username=username).exists():

            return redirect('registration')

        # Create the user
        user = User.objects.create_user(username=username, password=password1)
        user.save()

        # Authenticate and log in the user
        user = authenticate(request, username=username, password=password1)
        if user is not None:
            login(request, user)
            return redirect('login')  # Redirect to user list view after logging in

    return render(request, 'registration.html')


def loginpage(request):

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=loginTable.objects.filter(username=username,password=password,type='user').exists()
        try:
            if user is not None:
                user_details=loginTable.objects.get(username=username,password=password)
                user_name=user_details.username
                type=user_details.type

                if type=='user':
                    request.session['username']=user_name
                    return redirect('userindex')

            else:
                messages.error(request,'invalid details')

        except:
            messages.error(request,'invalid')
    return render(request,'login.html')





def userindex(request):
    # Logic for the user page
    return render(request, 'userindex.html')



def profile_form(request):
    profiles, created = profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
              # Attach the logged-in user

            form.save()

            return redirect('userindex')
        else:
            print(form.errors)
            return render(request, 'profile_form.html', {'form': form})

    else:
        form = ProfileForm(instance=profiles)

    return render(request, 'profile_form.html', {'form': form})


def project_form(request):
    Project = project.objects.all()
    if request.method == 'POST':
        form = projectform(request.POST)
        if form.is_valid():
            Project = form.save(commit=False)
            Project.user = request.user
            Project.save()

            return redirect('listproject')  # Redirect to the page showing the list of skills
    else:
        form = projectform()

    return render(request, 'project_form.html', {'form': form, 'Project': Project})



def listinfo(request):
    if request.user.is_authenticated:
        try:
             Profile = profile.objects.get(user=request.user)  # Fetch the profile for the logged-in user
        except profile.DoesNotExist:
             Profile = None
    else:

        return redirect('login')
    return render(request,'listinfo.html',{'Profile':Profile})

def updateinfo(request):
    if request.user.is_authenticated:
        Profile, created = profile.objects.get_or_create(user=request.user)

        if request.method=="POST":
            form=ProfileForm(request.POST,files=request.FILES,instance=Profile)

            if form.is_valid():
                form.save()
                return redirect("listinfo")
        else:
            form=ProfileForm(instance=Profile)


        return render(request,'updateinfo.html',{'form':form})



def updateproject(request, project_id):
    Project = get_object_or_404(project, id=project_id)
    if request.method=="POST":
        form=projectform(request.POST,files=request.FILES,instance=Project)

        if form.is_valid():
            form.save()
            return redirect("listproject")
    else:
        form=projectform(instance=Project)


    return render(request,'updateproject.html',{'form':form})

def updateskill(request, skill_id):
    skill = get_object_or_404(Skill, id=skill_id)
    if request.method=="POST":
        form=SkillForm(request.POST,files=request.FILES,instance=skill)

        if form.is_valid():
            form.save()
            return redirect("listskill")
    else:
        form=SkillForm(instance=skill)


    return render(request,'updateskill.html',{'form':form})
def listproject(request):
    Projects = project.objects.filter(user=request.user)


    return render(request,'listproject.html',{'Projects':Projects})





def projectdetails(request,project_id):

    Project=project.objects.get(id=project_id)

    return render(request,'projectdetails.html',{'Project':Project})

def deleteproject(request,project_id):

    Project=project.objects.get(id=project_id)

    if request.method=="POST":
        Project.delete()
        return redirect("listproject")


    return render(request,'deleteproject.html',{'Project':Project})

def createprofile(request):

    Profile=profile.objects.all()

    if request.method == "POST":
        form = ProfileForm(request.POST, files=request.FILES)

        if form.is_valid():
            form.save()

            return redirect("listinfo")
    else:
        form = ProfileForm()

    return render(request, "createprofile.html", {'form': form, 'Profile': Profile})


def add_skill(request):

    skill= Skill.objects.all()
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.user = request.user
            skill.save()


            return redirect('listskill')  # Redirect to the page showing the list of skills
    else:
        form = SkillForm()

    return render(request, 'add_skill.html', {'form': form,'skill':skill})




def listskill(request):

    skills = Skill.objects.filter(user=request.user)

    return render(request, 'listskill.html',{'skills':skills})


def deleteskill(request,skill_id):

    skill=Skill.objects.get(id=skill_id)

    if request.method=="POST":
        skill.delete()
        return redirect("listskill")


    return render(request,'deleteproject.html',{'skill':skill})
