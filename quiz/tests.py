from django.test import TestCase
from django.urls import reverse
from .models import Answer, Question, Quiz
from django.contrib.auth import get_user_model



# Create your tests here.
class HomePageTests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')


class SignupPageTests(TestCase):
    username = 'test'
    email = 'test@email.com'

    def test_signup_page_status_code(self):
        response = self.client.get('/users/signup/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(
            self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()
                         [0].username, self.username)
        self.assertEqual(get_user_model().objects.all()
                         [0].email, self.email)


class QuizAppTests(TestCase):
    def setUp(self):
        quiz1 = Quiz.objects.create(title='T1', number_questions=1)
        q1 = Question.objects.create(question_text='Q1', quiz=quiz1)
        Answer.objects.create(answer_text='A1', question=q1)
        Answer.objects.create(answer_text='A2', answer_is_true=True, question=q1)
        Answer.objects.create(answer_text='A3', question=q1)
        Answer.objects.create(answer_text='A4', question=q1)

    def test_quiz_models(self):
        test_quiz1 = Quiz.objects.get(title="T1")
        test_q1 = Question.objects.get(question_text="Q1")
        test_a1 = Answer.objects.get(answer_text="A1")
    
        self.assertEqual(test_quiz1.title, 'T1')
        self.assertEqual(str(test_q1.get_true_answer()[0]), 'A2')
        self.assertEqual(test_a1.question.question_text, 'Q1')

    def test_quiz_list_page_status_code(self):
        response = self.client.get(reverse('quiz_list'))
        self.assertEqual(response.status_code, 200)

    def test_quiz_list_uses_correct_template(self):
        response = self.client.get(reverse('quiz_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'quiz_list.html')

    def test_quiz_result_page_status_code(self):
        response = self.client.get(reverse('quiz_result'))
        self.assertEqual(response.status_code, 200)

    def test_quiz_result_uses_correct_template(self):
        response = self.client.get(reverse('quiz_result'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'quiz_result.html')

    def test_quiz_detail_page_status_code(self):
        response = self.client.get('/quiz/1', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_quiz_detail_uses_correct_template(self):
        response = self.client.get('/quiz/1', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'quiz_detail.html')