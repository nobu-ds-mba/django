from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    # path(route, view, (省略可)kwargs, (省略可)name)
    # route: URLパターンを含む文字列，urlpatternsの初めのパターンから開始し，リストを順に下に見ていく
    # view: マッチする正規表現を見つけると，指定されたビュー関数を呼び出す
    # kwargs: 任意のキーワード引数を辞書として大賞のビューに渡す
    # name: URLに名前をつける
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]