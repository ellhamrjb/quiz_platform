from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Question, UserScore

class QuizPlatformTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        
        Question.objects.create(text='Where is the capital of France?', correct_answer='Paris')
        Question.objects.create(text='Where is the capital of Germany?', correct_answer='Berlin')

    def test_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Are you ready to challenge your knowledge about the capitals of countries?")

    def test_login(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpassword'})
        self.assertRedirects(response, reverse('home'))

    def test_start_quiz(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('start_quiz'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Answer the Questions")

    def test_score_submission(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('start_quiz'), {'q1': 'Paris', 'q2': 'Berlin'})
        self.assertRedirects(response, reverse('view_score'))
        user_score = UserScore.objects.get(user=self.user)
        self.assertEqual(user_score.score, 2)
