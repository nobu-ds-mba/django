from django.shortcuts import get_object_or_404, render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'



'''
def index(request):
    
    # システム上にある最新の5件の質問項目を間まで区切り，日付順に表示するビュー
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list, 
        }
    return render(request, 'polls/index.html', context)
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    
    # polls/index.htmlというテンプレートをロードし，そこにコンテキストを渡す
    # template = loader.get_template('polls/index.html')
    # return HttpResponse(template.render(context, request))
    
    # テンプレートをロードしてコンテキストに値を入れ，テンプレートをレンダリングした結果をHttpResponseオブジェクトで返すショートカット
    # render()関数：render(requestオブジェクト, テンプレート名, (任意))
    
    # return HttpResponse("Hello, world. You're at the polls index.")
'''

'''
def detail(request, question_id):
    
    try:
        question = Question.objects.get(pk = question_id)
    # リクエストしたIDを持つ質問が存在しないときにHttp404を提示
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
    
    # return HttpResponse("You're looking at question %s." % question_id)
    
    # get()を実行し，オブジェクトが存在しない場合にはHttp404を提示するショートカット
    # get_object_or_404()関数：get_object_or_404(Djangoモデル)，任意の数のキーワードを引数に取り，モデルのマネージャのget()関数に渡す
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/detail.html', {'question': question})
'''

'''
def results(request, question_id):
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)
    
    # 質問の投票をすると，vote()ビューは質問の結果ページにリダイレクトする
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/results.html', {'question': question})
'''

def  vote(request, question_id):
    # return HttpResponse("You're voting on question %s." % question_id)
    
    question = get_object_or_404(Question, pk = question_id)
    try:
        # request.POST['choice']: キーを指定すると送信したデータにアクセスできる，選択された選択肢のIDを文字列として返す
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    # POSTデータにChoiceがなければ，request.POST['choice']はKeyErrorを提示
    except (KeyError, Choice.DoesNotExist):
        # Rarisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args = (question.id,)))

