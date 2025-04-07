from django.core.management.base import BaseCommand
from main.models import trainingModule, quiz, question, answer

class Command(BaseCommand):
    help = 'Create quizzes and their associated questions and answers'

    def handle(self, *args, **kwargs):
        # Create training modules if they don't exist
        incident_response_module, created = TrainingModule.objects.get_or_create(
            title="Incident Response Planning",
            defaults={
                'description': "Learn how to effectively respond to security incidents.",
                'content': "Content about incident response planning.",
                'duration_minutes': 30,
                'is_active': True
            }
        )

        secure_password_module, created = TrainingModule.objects.get_or_create(
            title="Secure Password Practice",
            defaults={
                'description': "Best practices for creating and managing secure passwords.",
                'content': "Content about secure password practices.",
                'duration_minutes': 20,
                'is_active': True
            }
        )

        malware_module, created = TrainingModule.objects.get_or_create(
            title="Malware",
            defaults={
                'description': "Understanding different types of malware and how to protect against them.",
                'content': "Content about malware.",
                'duration_minutes': 25,
                'is_active': True
            }
        )

        # Create quizzes
        incident_response_quiz = Quiz.objects.create(title="Incident Response Planning Quiz", training_module=incident_response_module)
        secure_password_quiz = Quiz.objects.create(title="Secure Password Practice Quiz", training_module=secure_password_module)
        malware_quiz = Quiz.objects.create(title="Malware Quiz", training_module=malware_module)

        # Add questions and answers for Incident Response Planning Quiz
        question1 = Question.objects.create(quiz=incident_response_quiz, question_text="What is the first step in incident response?")
        Answer.objects.create(question=question1, answer_text="Identification", is_correct=True)
        Answer.objects.create(question=question1, answer_text="Containment", is_correct=False)
        Answer.objects.create(question=question1, answer_text="Eradication", is_correct=False)
        Answer.objects.create(question=question1, answer_text="Recovery", is_correct=False)

        question2 = Question.objects.create(quiz=incident_response_quiz, question_text="What is the primary goal of incident response?")
        Answer.objects.create(question=question2, answer_text="To minimize damage", is_correct=True)
        Answer.objects.create(question=question2, answer_text="To inform the public", is_correct=False)
        Answer.objects.create(question=question2, answer_text="To blame the attackers", is_correct=False)
        Answer.objects.create(question=question2, answer_text="To shut down the system", is_correct=False)

        # Add questions and answers for Secure Password Practice Quiz
        question3 = Question.objects.create(quiz=secure_password_quiz, question_text="What is a strong password?")
        Answer.objects.create(question=question3, answer_text="123456", is_correct=False)
        Answer.objects.create(question=question3, answer_text="Password", is_correct=False)
        Answer.objects.create(question=question3, answer_text="A mix of letters, numbers, and symbols", is_correct=True)
        Answer.objects.create(question=question3, answer_text="Your name", is_correct=False)

        question4 = Question.objects.create(quiz=secure_password_quiz, question_text="How often should you change your passwords?")
        Answer.objects.create(question=question4, answer_text="Every month", is_correct=False)
        Answer.objects.create(question=question4, answer_text="Every year", is_correct=False)
        Answer.objects.create(question=question4, answer_text="Every 3-6 months", is_correct=True)
        Answer.objects.create(question=question4, answer_text="Never", is_correct=False)

        # Add questions and answers for Malware Quiz
 question5 = Question.objects.create(quiz=malware_quiz, question_text="What is malware?")
        Answer.objects.create(question=question5, answer_text="A type of software designed to harm or exploit any programmable device", is_correct=True)
        Answer.objects.create(question=question5, answer_text="A computer virus", is_correct=False)
        Answer.objects.create(question=question5, answer_text="A firewall", is_correct=False)
        Answer.objects.create(question=question5, answer_text="An antivirus program", is_correct=False)

        question6 = Question.objects.create(quiz=malware_quiz, question_text="Which of the following is a type of malware?")
        Answer.objects.create(question=question6, answer_text="Virus", is_correct=True)
        Answer.objects.create(question=question6, answer_text="Trojan", is_correct=True)
        Answer.objects.create(question=question6, answer_text="Worm", is_correct=True)
        Answer.objects.create(question=question6, answer_text="All of the above", is_correct=True)

        self.stdout.write(self.style.SUCCESS('Successfully created quizzes, questions, and answers.'))