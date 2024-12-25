from django.shortcuts import render, redirect, reverse

# Create your views here.
def index(request):
    return render(request, 'board/index.html')

from .models import Board

def list(request):
    board_list = Board.objects.all().order_by('-id') # Board 모델 전체 목록 가져오기
    context = {
        'board_list':board_list,
    } # 응답에 사용할 수 있도록 딕셔너리 생성
    return render(
        request,
        'board/list.html', # render 함수를 통해 list template 응답
        context # 응답은 context 사용
    )

def read(request, id):
    board = Board.objects.get(pk=id) # 하나의 요소를 찾아서 read.html로 응답
    board.incrementReadCount()
    return render(request, 'board/read.html', {'board':board})

def regist(request):
    if request.method == 'POST':
        title = request.POST['title']
        writer = request.POST.get('writer')
        content = request.POST['content']
        Board(title=title, writer=writer, content=content).save()
        return redirect(reverse('board:list'))
    else:
        return render(request, 'board/regist.html')    

def edit(request, id):
    board = Board.objects.get(pk=id)
    if request.method == 'POST':
        board.title = request.POST['title']
        board.title = request.POST.get('writer')
        board.title = request.POST['content']
        board.save()
        return redirect(reverse('board:read', args=(id,)))
    else:
        return render(request, 'board/edit.html', {'board':board})    

def remove(request, id):
    board = Board.objects.get(pk=id)
    if request.method == "POST":
        board.delete()
        return redirect(reverse("board:list"))
    else:
        return render(request, 'board/remove.html', {'board':board})