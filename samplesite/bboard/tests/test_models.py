from django.test import TestCase

from bboard.models import Bb


class BbTests(TestCase):
    """Тесты для модели Bb"""

    @classmethod
    def setUpTestData(cls):
        """Заносит данные в БД перед запуском тестов класса"""

        cls.bb = Bb.objects.create(
            title='Дом', content='Трехэтажный, кирпич', price=50000000
        )

    def test_title(self):
        """Тест параметра title"""

        real_title = getattr(self.bb_field, 'title')
        expected_title = 'Дом'

        self.assertEqual(real_title, expected_title)

    def test_model_verbose_name(self):
        """Тест поля verbose_name модели Bb"""

        self.assertEqual(Bb._meta.verbose_name, 'Объявление')

    def test_model_verbose_name_plural(self):
        """Тест поля verbose_name_plural модели Bb"""

        self.assertEqual(Bb._meta.verbose_name_plural, 'Объявления')

    def test_title(self):
        pass

    def test_max_length(self):
        pass

