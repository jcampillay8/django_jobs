from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt


# Create your views here.


def home(request):
    # if 'user' not in request.session:
    #     return redirect('/')
    current_user = User.objects.get(id=request.session['id'])
    jobs = Job.objects.all()
    taken = Job.objects.filter(employee=None)
    print(taken)
    context={
        'user': current_user,
        'jobs': jobs,
        'user_jobs': Job.objects.filter(employee=current_user),
        'taken':taken
    }
    return render(request, 'jobs/home.html', context)

def logout(request):
    del request.session['id']
    return redirect('/')

def new(request):
    user = User.objects.get(id=request.session['id'])
    context={
        'user':user
    }
    return render(request, 'jobs/new.html',context)

def add_new(request):
    error = Job.objects.info_Validator(request.POST)
    if len(error)>0:
        for key, value in error.items():
            messages.error(request, value, extra_tags='info')
        return redirect('/jobs/new')
    creator = User.objects.get(id=request.session['id'])
    Job.objects.create(title=request.POST['title'], location=request.POST['location'], desc=request.POST['desc'], creator=User.objects.get(id=request.session['id']))
    return redirect('/jobs/home')

def add_job(request, id):
    user = User.objects.get(id=request.session['id'])
    job = Job.objects.get(id=id)
    if job.employee:
        return redirect('/jobs/home')
    user.jobs.add(job)
    return redirect('/jobs/home')

def remove_job(request,id):
    job = Job.objects.get(id=id)
    job.delete()
    return redirect('/jobs/home')

def job_info(request, id):
    user=User.objects.get(id=request.session['id'])
    job = Job.objects.get(id=id)
    # user_in_job = job.filter(employee=user)
    context ={
        'user':user,
        'job':job,
        # 'user_in_job': user_in_job

    }
    return render(request, 'jobs/job_info.html', context)

def give_up(request,id):
    user=User.objects.get(id=request.session['id'])
    job = Job.objects.get(id=id)
    user.jobs.remove(job)
    return redirect('/jobs/home')

def done(request, id):
    job = Job.objects.get(id=id)
    job.delete()
    return redirect('/jobs/home')

def edit(request, id):
    job = Job.objects.get(id=id)
    user = User.objects.get(id=request.session['id'])
    context={
        'job':job,
        'user':user
    }
    return render(request, 'jobs/edit.html', context)

def edit_job(request, id):
    error = User.objects.editValidator(request.POST)
    job = Job.objects.get(id=id)
    if len(error)>0:
        for key, value in error.items():
            messages.error(request, value, extra_tags='edit')
        return redirect('/jobs/edit/'+str(id))
    job.title= request.POST['title']
    job.desc = request.POST['desc']
    job.location=request.POST['location']
    job.save()
    return redirect('/home')