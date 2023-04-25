from django.shortcuts import render
from imtihon.models import Question

# Create your views here.
def home(request):

    fanlar = Question.objects.values('subject')
    fanlarSet = set(map(lambda fan: fan["subject"], fanlar))
    data = {
        'fanlar': fanlarSet
    }

    return render(request, 'user/user_main.html', data)