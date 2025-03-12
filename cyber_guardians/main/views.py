from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import trainingModule, quiz, question

# Create your views here.
def home(request):
	return render(request, 'home.html', {})

'''Registration'''
def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}!')
			return redirect('login')
	else:
		form = UserCreationForm()
	return render(request, 'register.html', {'form': form})


'''login'''
def login_view(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.error(request, 'Invalid username or password.')

	return render(request, 'login.html')


'''logout form'''
def logout_view(request):
	logout(request)
	messages.success(request, 'You have been logged out!')
	return redirect('home')

def training(request, module_id):
    module = get_object_or_404(trainingModule, id=module_id)
    quiz = module.quizzes.first()
    return render(request, 'training.html', {'module': module})

def training_list(request):
    modules = trainingModule.objects.filter(is_active=True).prefetch_related('quizzes')  # Only show active modules
    return render(request, 'training_list.html', {'modules': modules, 'quiz': quiz})

def submit_quiz(request, quiz_id):
    quiz = get_object_or_404(quiz, id=quiz_id)
    score = 0
    total_questions = quiz.questions.count()

    # Check if the request method is POST
    if request.method == 'POST':
        # Iterate through each question in the quiz
        for question in quiz.questions.all():
            # Get the selected answer from the POST data
            selected_answer_id = request.POST.get(f'question_{question.id}')
            if selected_answer_id:
                # Get the selected answer object
                selected_answer = get_object_or_404(answer, id=selected_answer_id)
                # Check if the selected answer is correct
                if selected_answer.is_correct:
                    score += 1

        # Redirect to the results page with the score
        return render(request, 'quiz_results.html', {'score': score, 'total_questions': total_questions})

    # If the request method is not POST, redirect back to the quiz page
    return redirect('training', module_id=quiz.training.id)