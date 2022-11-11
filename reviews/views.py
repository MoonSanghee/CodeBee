from django.shortcuts import render,redirect
from .forms import StudyForm, AcceptedForm
from .models import Study, Accepted
from accounts.models import User


# Create your views here.

def home(request):
    return render(request, 'home.html')

def index(request):
    studies = Study.objects.order_by('-pk')
    context = {
        'studies': studies
    }
    return render(request, 'reviews/index.html', context)

def create(request):
    if request.method =='POST':
        study_form = StudyForm(request.POST, request.FILES)
        if study_form.is_valid():
            study = study_form.save(commit=False)
            study.host = request.user
            study.save()
            Aform = Accepted(joined=True,study=study,users=study.host)
            Aform.save()
            return redirect('reviews:index')
    else:
        study_form = StudyForm()
    context = {'study_form' : study_form}
    return render(request, 'reviews/form.html', context)

def detail(request, study_pk):
    study = Study.objects.get(pk=study_pk)
    context = {
        'study':study
    }
    return render(request, 'reviews/detail.html', context)

def userlist(request, study_pk):
    users = Accepted.objects.filter(study_id=study_pk)
    study = Study.objects.filter(pk=study_pk)
    context = {
        'members':users,
        'study':Study.objects.get(pk=study_pk),
    }
    return render(request, 'reviews/userlist.html', context)
    

def update(request, study_pk):
    study = Study.objects.get(pk=study_pk)
    if request.user == study.host:
        if request.method == 'POST':
            study_form = StudyForm(request.POST, request.FILES, instance=study)
            if study_form.is_valid():
                study_form.save()
                return redirect('reviews:detail', study_pk)
        else:
            study_form = StudyForm(instance=study)
        context = {'study_form': study_form}
        return render(request, 'reviews/form.html', context)
    else:
        return redirect('reviews:detail', study_pk)

def delete(request, study_pk):
    study = Study.objects.get(pk=study_pk)
    study.delete()
    return redirect('reviews:index')



def join(requset, study_pk, user_pk):
    study = Study.objects.get(pk=study_pk)
    accepted = Accepted.objects.filter(study_id=study_pk)
    users = Accepted.objects.filter(users_id=user_pk)
    print(users)
    if study.limits > len(accepted):
        for joined in users:
            if joined in accepted:
                print('이미 가입되어 있습니다.')
                return redirect('reviews:index')
        else:
            Aform = Accepted(joined=False,study=study,users=requset.user)
            Aform.save()
            print('가입 신청')
            return redirect('reviews:index')
    else:
        return redirect('reviews:index')

def study_accepted(requeset, study_id, users_id):
    study = Study.objects.get(id=study_id)
    user = User.objects.get(id=users_id)
    aform = Accepted.objects.get(users=user, study=study)
    if requeset.user == study.host:
        aform.joined = True
        aform.save()
        return redirect('reviews:userlist', study_id)
    else:
        return redirect('reviews:userlist', study_id)

def study_kick(requeset, study_id, users_id):
    study = Study.objects.get(id=study_id)
    user = User.objects.get(id=users_id)
    aform = Accepted.objects.get(users=user, study=study)
    if requeset.user == study.host and user != study.host:
        aform.delete()
        return redirect('reviews:userlist', study_id)
    elif requeset.user == user and user != study.host:
        aform.delete()
        return redirect('reviews:index')
    else:
        return redirect('reviews:userlist', study_id)
    
