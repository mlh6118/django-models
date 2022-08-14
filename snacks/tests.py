from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from snacks.models import Snack


class SnacksTestPages(TestCase):
    """
    Tests each page's status and template usage.
    """

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass")
        self.snack = Snack.objects.create(
            name="Reese's", description="Chocolate peanut butter cups",
            purchaser=self.user)

    def test_snack_list_page_status_code(self):
        url = reverse('snacks')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_snack_list_page_template(self):
        url = reverse("snacks")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snack_list.html")
        self.assertTemplateUsed(response, "base.html")

    def test_snack_detail_page_status_code(self):
        url = reverse('snack_detail', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_snack_detail_page_template(self):
        url = reverse("snack_detail", args=[1])
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snack_detail.html")
        self.assertTemplateUsed(response, "base.html")

    """
    Test each element of a snack.
    """

    def test_string_representation(self):
        self.assertEqual(str(self.snack), 'Reese\'s: Chocolate peanut butter '
                                          'cups (tester)')

    def test_string_representation_fail(self):
        self.assertIsNot(str(self.snack), 'Reese\'s')

    def test_string_representation_name(self):
        self.assertEqual(str(self.snack.name), 'Reese\'s')

    def test_string_representation_name_fail(self):
        self.assertIsNot(str(self.snack.name), 'Reeses')

    def test_string_representation_description(self):
        self.assertEqual(str(self.snack.description), 'Chocolate peanut butter '
                                                      'cups')

    def test_string_representation_description_fail(self):
        self.assertIsNot(str(self.snack.description), 'Yummy!')

    def test_string_representation_purchaser(self):
        self.assertEqual(str(self.snack.purchaser), 'tester')

    def test_string_representation_purchaser_fail(self):
        self.assertIsNot(str(self.snack.purchaser), 'admin')
