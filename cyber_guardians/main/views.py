from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import trainingModule, quiz, question, answer, incidentReport, Resource
from .forms import incidentReportForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.core.mail import send_mail
from django.conf import settings

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
    quiz_submit = get_object_or_404(quiz, id=quiz_id)
    score = 0
    total_questions = quiz_submit.questions.count()

    # Check if the request method is POST
    if request.method == 'POST':
        # Iterate through each question in the quiz
        for question in quiz_submit.questions.all():
            # Get the selected answer from the POST data
            selected_answer_id = request.POST.get(f'question_{question.id}')
            if selected_answer_id:
                # Get the selected answer object
                selected_answer = get_object_or_404(answer, id=selected_answer_id)
                # Check if the selected answer is correct
                if selected_answer.is_correct:
                    score += 1

        percentage_score = (score / total_questions) * 100 if total_questions > 0 else 0

        is_passing = score >= (total_questions / 2)

        # Redirect to the results page with the score
        return render(request, 'quiz_results.html', {'score': score, 'total_questions': total_questions, 'percentage_score': percentage_score, 'is_passing': is_passing, 'quiz': quiz_submit})

    # If the request method is not POST, redirect back to the quiz page
    return redirect('training', module_id=quiz_submit.training.id)

def quiz_view(request, quiz_id):
	quiz_instance = get_object_or_404(quiz, id=quiz_id)
	return render(request, 'quiz.html', {'quiz': quiz_instance})

@login_required
def report_incident(request):
	if request.method == 'POST':
		form = incidentReportForm(request.POST)
		if form.is_valid():
			incident_report = form.save(commit=False)  # Create the instance but don't save it yet
			incident_report.user = request.user  # Set the user field to the logged-in user
			incident_report.save() 
			return redirect('report_success')
	else:
		form = incidentReportForm()

		return render(request, 'report_incident.html', {'form': form})

def report_success(request):
	return render(request, 'report_success.html')

@login_required
def report_list(request):
    reports = incidentReport.objects.filter(user=request.user)  # Get reports for the logged-in user

    if request.method == 'POST':
        if 'delete' in request.POST:
            report_id = request.POST.get('report_id')
            report = get_object_or_404(incidentReport, id=report_id, user=request.user)
            report.delete()
            messages.success(request, 'Incident report deleted successfully.')
            return redirect('incident_report:report_list')

        if 'update_status' in request.POST:
            report_id = request.POST.get('report_id')
            new_status = request.POST.get('status')
            report = get_object_or_404(incidentReport, id=report_id, user=request.user)
            report.status = new_status
            report.save()
            messages.success(request, 'Incident report status updated successfully.')
            return redirect('incident_report:report_list')

    return render(request, 'report_list.html', {'reports': reports})

class ResourceListView(ListView):
	model = Resource
	template_name = 'resource_list.html'
	context_object_name = 'resources'

class ResourceDetailView(DetailView):
	model = Resource
	template_name = 'resource_detail.html'
	context_object_name = 'resource'

def about_us(request):
	return render(request, 'about_us.html')

def contact_us(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		message = request.POST.get('message')

		try:
			send_mail(
            	f'Contact Form Submission from {name}',
                message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_EMAIL],  # Set this in your settings.py
                fail_silently=False,
            )
            return render(request, 'contact_us.html', {
        	'success': True
        	})

        except Exception as e:
            # Handle the error (optional logging can be added here)
            print(f"Error sending email: {e}")
            return render(request, 'contact_us.html', {'error': True
            })

    return render(request, 'contact_us.html')

