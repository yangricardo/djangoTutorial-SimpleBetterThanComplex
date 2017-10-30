from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from .models import Board, Topic, Post
from .forms import NewTopicForm

def home(request):
	boards = Board.objects.all()
	return render(request, 'home.html',{'boards': boards })


def board_topics(request, pk):
	board = get_object_or_404(Board,pk=pk)
	return render(request, 'topics.html',{'board': board })

def new_topic(request, pk):
	board = get_object_or_404(Board, pk=pk)
	user = User.objects.first() 
	
	if request.method == 'POST':
		"""
		subject = request.POST['subject']
		message = request.POST['message']
		"""
		form = NewTopicForm(request.POST)
		#instancia um form passando o dado vindo da chamada POST
		
		user = User.objects.first()

		if form.is_valid():
			topic = form.save(commit=False)
			topic.board = board
			topic.starter = user
			topic.save()
			post = Post.objects.create(
					message=form.cleaned_data.get('message'),
					topic=topic,
					created_by=user
				)
			return redirect('board_topics',pk=board.pk)

		"""
		topic = Topic.objects.create(
				subject = subject,
				board = board,
				starter = user
			)
		post = Post.objects.create(
				message = message,
				topic = topic,
				created_by = user
			)
		"""
	else:
		form = NewTopicForm()
	#return render(request, 'new_topic.html',{'board': board })
	return render(request, 'new_topic.html',{'board': board, 'form': form })




"""
def home(request):
	return HttpResponse('Hello, World!')
"""
"""
def home(request):
	boards = Board.objects.all()
	boards_names = list()

	for board in boards:
		boards_names.append(board.name)

	response_html = '<br>'.join(boards_names)

	return HttpResponse(response_html)

	
def board_topics(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404
    return render(request, 'topics.html', {'board': board})

"""

"""
def about(request):
    # do something...
    return render(request, 'about.html')

def about_company(request):
    # do something else...
    # return some data along with the view...
    return render(request, 'about_company.html', {'company_name': 'Simple Complex'})
"""