from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Question
import ast
import random
from django.contrib.auth import decorators

def grouping(lst):
    lst.sort()
    result = {}
    for item in lst:
        key = item[-1]
        if key in result:
            result[key].append(item)
        else:
            result[key] = [item]
    return result
@decorators.login_required
def testIshla(request):
    if request.method == 'POST':
        form_data = request.POST
        questions = []
        choices = []
        rights = []
        javoblar = {}
        hammasi = form_data
        kalitlari = list(hammasi.keys())
        qiymatlari = list(hammasi.values())
        allData = dict(form_data.items())
        for key in form_data:
            if key.startswith('question-'):
                questions.append(key)
            elif key.startswith('choice-'):
                choices.append(key)
            elif key.startswith('right-choice'):
                j = kalitlari.index(key)
                rights.append(qiymatlari[j+1])
        sorted_choices = list(grouping(choices).values())
        for k in sorted_choices:
            for f in k:
                ind = k.index(f)
                k[ind] = allData[f]
        for n in questions:
            indx = questions.index(n)
            javoblar[allData[n]] = {
                'variantlar': sorted_choices[indx],
                'togri_javob': rights[indx]
            }
        for i in list(javoblar.keys()):
            q = Question(subject=allData['subject-title'], theme=allData['theme'], question_text=i, choices=javoblar[i]['variantlar'], right_choice=javoblar[i]['togri_javob'])
            q.save()
        return HttpResponse(f'{javoblar}')
    else:
        return render(request, 'imtihon/index.html')
def javop(request):
    if request.method == 'GET':
        data = {}
        all = Question.objects.all()
        flip = {
            'all':data
        }
        for i in all:
            savol = i.question_text
            variantlar = ast.literal_eval(i.choices)
            random.shuffle(variantlar)
            data[savol] = variantlar
        return render(request, 'imtihon/javop.html', flip)
    elif request.method == 'POST':
        sanoq = 0
        form_data = request.POST
        for savol in form_data.keys():
            if savol == "csrfmiddlewaretoken":
                continue
            evaData = list(Question.objects.filter(question_text=savol).values())
            for i in evaData:
                if i['right_choice'] == form_data[savol]:
                    sanoq += 1

        return HttpResponse(f'{sanoq}')