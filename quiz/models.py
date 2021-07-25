from django.db import models
from random import shuffle

# Create your models here.
CATEGORIES_CHOICES = (
    ("Food", "Food"),
    ("Music", "Music"),
    ("Geography", "Geography"),
    ("Sports", "Sports"),
    ("History", "History"),
    ("Science", "Science"),
    ("Math", "Math"),
)

class Quiz(models.Model):
    title = models.CharField(max_length=500)

    category = models.CharField(max_length = 20 ,choices = CATEGORIES_CHOICES, default = 'Food')
    number_questions = models.SmallIntegerField()

    def __str__(self) -> str:
        return self.title

    def get_questions(self):
        questions = list(self.questions.all())
        shuffle(questions)
        return questions[:self.number_questions]

class Question(models.Model):
    question_text = models.CharField(max_length=900)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions', default='')

    def __str__(self) -> str:
        return self.question_text

    def get_answers(self):
        answers = list(self.answers.all())
        shuffle(answers)
        return answers

    def get_true_answer(self):
        answer = self.answers.filter(answer_is_true = True)
        return answer

class Answer(models.Model):
    answer_text = models.CharField(max_length=900)
    answer_is_true = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')

    def __str__(self) -> str:
        return self.answer_text


