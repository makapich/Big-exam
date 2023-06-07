from django.test import TestCase
from .views import TriangleForm


class TriangleTriangleViewTests(TestCase):
    def test_triangle_view_status_code(self):
        response = self.client.get('/triangle/')
        self.assertEqual(response.status_code, 200)

    def test_triangle_view_uses_correct_template(self):
        response = self.client.get('/triangle/')
        self.assertTemplateUsed(response, 'triangle/triangle.html')

    def test_triangle_view_returns_form(self):
        response = self.client.get('/triangle/')
        self.assertIsInstance(response.context['form'], TriangleForm)

    def test_triangle_view_calculates_hypotenuse(self):
        response = self.client.get('/triangle/', {'leg1': 3, 'leg2': 4, 'Submit': True})
        self.assertEqual(response.context['hypotenuse'], 5.0)

    def test_triangle_view_does_not_calculate_hypotenuse_on_invalid_form(self):
        response = self.client.get('/triangle/', {'leg1': -3, 'leg2': 4, 'Submit': True})
        self.assertIsNone(response.context['hypotenuse'])

    def test_triangle_view_returns_empty_form_on_invalid_form(self):
        response = self.client.get('/triangle/', {'leg1': -3, 'leg2': 4, 'Submit': True})
        self.assertIsInstance(response.context['form'], TriangleForm)
