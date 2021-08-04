from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class TaskListTests(TestCase):
    def test_view_url_by_name(self):
        response = self.client.get(reverse('tasks'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('tasks'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'task/task_list.html')

class TaskCreateTests(TestCase):
    def test_view_url_by_name(self):
        response = self.client.get(reverse('task_create'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('task_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'task/task_create.html')
