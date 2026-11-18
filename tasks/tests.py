from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Task


class TodoSecurityAndLogicTests(TestCase):
    def setUp(self):
        # Создаём двух разных тестовых пользователей перед каждым тестом
        self.user1 = User.objects.create_user(username="ali", password="password123")
        self.user2 = User.objects.create_user(username="ivan", password="password123")

    def test_guest_redirected_to_login(self):
        # Невошедший пользователь должен получить редирект (302) на страницу входа
        response = self.client.get(reverse("task_list"))
        self.assertEqual(response.status_code, 302)

    def test_user_can_create_own_task(self):
        # Входим под пользователем ali и создаём задачу через POST-запрос
        self.client.login(username="ali", password="password123")
        self.client.post(reverse("task_list"), {"title": "Сдать проект", "page_type": "work"})

        task = Task.objects.get(title="Сдать проект")
        self.assertEqual(task.user, self.user1)

    def test_user_cannot_delete_foreign_task(self):
        # Создаём задачу от имени ali, но пытаемся удалить её от имени ivan
        task = Task.objects.create(user=self.user1, title="Секретная задача")
        self.client.login(username="ivan", password="password123")

        response = self.client.get(reverse("delete_task", args=[task.id]))
        self.assertEqual(response.status_code, 404)
        self.assertTrue(Task.objects.filter(id=task.id).exists())
