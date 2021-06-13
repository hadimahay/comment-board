
from django.shortcuts import redirect, render
from .models import board
from django.http import HttpResponse , HttpResponseNotAllowed
from .forms import sendCommentForm  

# Create your views here.

def Board(request):
    Comment = board.objects.order_by('-created_at')
    return render(request , 'board/commentsboard.html' , {
                    'comment':Comment
    })

def Comment(request):
    if request.method == 'POST':
        form = sendCommentForm(request.POST)

        if form.is_valid():
            board.objects.create(
                comment = form.cleaned_data['comment']
            )
            return redirect('board:commentboard')

    else:
        form = sendCommentForm()
        

    return render(request, 'board/comment.html', {"form":form})

    