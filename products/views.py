
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from products.forms import FeatureCommentForm, FeatureForm, BugForm, BugCommentForm

from django import forms


def bugs(request):
    return render(request, 'bugs.html')



#adding bugs for the users
@login_required
def publicise_bug(request):
    if request.method == "POST":
        form = BugForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index.html')
    else:
        form = BugForm()  
        
    return render(request, 'publicise_bug.html', {'form': form})


#creating the views/funtions for adding features
@login_required
def publicise_features(request):
    if request.method == "POST":
        form = FeatureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = FeatureForm()
        
    
    return render(request, 'publicise_feature.html', {'form': form})



#creating the views/funtions for adding comments on bugs
@login_required
def bug_comment(request):
    if request.method == "POST":
        form = BugCommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = BugCommentForm()
    return render(request, 'submit_bug_comment.html', {'form': form})


#creating the views/funtions for adding comments on features
@login_required
def feature_comment(request):
    if request.method == "POST":
        form = FeatureCommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = FeatureCommentForm()
    return render(request, 'submit_feature_comment.html', {'form': form})

def features(request):
    return render(request, 'features.html')



@login_required
def user_history(request):
    return render(request, 'user_history.html')

def pricing(request):
    return render(request, 'pricing.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def team(request):
    return render(request, 'team.html')

def mission(request):
    return render(request, 'mission.html')


@login_required
def view_bugs(request): 
    return render(request, 'view_bug.html')

@login_required
def view_features(request): 
    return render(request, 'view_feature.html')

def skills(request):
    return render(request, 'skills.html')

def planning(request):
    return render(request, 'planning.html')

def mobile(request):
    return render(request, 'mobile.html')

def it_solutions(request):
    return render(request, 'it_solutions.html')

