from django.shortcuts import render
from .models import Question
import random
from app_user.decorator import login_required
# Create your views here.


@login_required
def question(request):
    all_questions_queryset = Question.objects.all().order_by('?')  # order by '?' randomizing  questions
    if request.method == 'GET' and not request.session['ans_submitted']:  # answer not submitted yet
        qa_list = []
        qa_dict = {}
        for q in all_questions_queryset:
            option_list = [q.op1, q.op2, q.op3, q.op4]
            random.shuffle(option_list)  # randomize options
            qa_dict['q_id'] = q.pk
            qa_dict['q'] = q.question
            qa_dict['a'] = option_list
            qa_list.append(qa_dict.copy())
        # print(f"QA List: {qa_list}")
        context = {
            'qa_list': qa_list
        }
        return render(request, 'quiz/question.html', context)
    elif request.method == 'GET' and request.session['ans_submitted']:  # to handle page refresh after submit
        return render(request, 'quiz/score.html')
    elif request.method == 'POST':  # verify answer and show score
        request.session['ans_submitted'] = True
        score = 0
        no_of_q = request.session['no_of_q']
        corr_ans_dict = {}
        for item in all_questions_queryset:
            corr_ans_dict[item.pk] = item.corr_ans

        for answer in range(1, no_of_q+1):
            if request.POST[str(answer)] == corr_ans_dict[answer]:
                score += 1

        # print(f"corr_ans_dict: {corr_ans_dict}")
        # print(f"Score: {score} out of {no_of_q}")

        request.session['score'] = score

        return render(request, 'quiz/score.html')
