from django.test import TestCase
from django.urls import reverse


from .models import Mineral
from .templatetags import mineral_extras

test_mineral_1 = {
    'name': 'Testing Minerals',
    'category': 'Stone',
    'formula': 'a^2 + b^2 = c^2',
    'mohs_scale_hardness': '3',
    'color': 'Blue',
    'crystal_system': 'Shiny',
    'unit_cell': 'Could be anything',
    'crystal_symmetry': 'Very symmetrical',
    'cleavage': 'N/A'
}

test_mineral_2 = {
    'name': 'Another Mineral',
    'image_filename': 'doesnotexist.jpg',
    'image_caption': 'Lorem ipsum',
    'category': 'Rare dirt',
    'formula': 'E = mc^2',
    'mohs_scale_hardness': '2',
    'color': 'Yellow',
    'unit_cell': 'Could be anything',
    'crystal_symmetry': 'Not symmetrical',
    'luster': 'Great luster',
    'streak': 'Not a good streak'
}


# Create your tests here.
class MineralModelTests(TestCase):

    def test_create_mineral(self):
        mineral = Mineral.objects.create(**test_mineral_1)
        self.assertEqual(mineral.name, test_mineral_1['name'])
        self.assertEqual(mineral.formula, test_mineral_1['formula'])
        self.assertEqual(len(mineral.unit_cell), len(test_mineral_1['unit_cell']))


class MineralViewsTests(TestCase):

    def setUp(self):
        self.mineral_1 = Mineral.objects.create(**test_mineral_1)
        self.mineral_2 = Mineral.objects.create(**test_mineral_2)

    def test_mineral_list(self):
        res = self.client.get(reverse('minerals:list'))
        self.assertEqual(res.status_code, 200)
        self.assertIn(self.mineral_1, res.context['minerals'])
        self.assertIn(self.mineral_2, res.context['minerals'])
        self.assertContains(res, self.mineral_1.name)

    def test_mineral_list_template(self):
        res = self.client.get(reverse('minerals:list'))
        self.assertTemplateUsed(res, 'minerals/mineral_list.html')

    def test_mineral_detail(self):
        res = self.client.get(reverse('minerals:detail', kwargs={
            'mineral_id': self.mineral_1.id
        }))
        self.assertEqual(self.mineral_1, res.context['mineral'])
        self.assertContains(res, self.mineral_1.name)
        self.assertContains(res, self.mineral_1.formula)
        self.assertContains(res, self.mineral_1.unit_cell)

    def test_mineral_detail_template(self):
        res = self.client.get(reverse('minerals:detail', kwargs={
            'mineral_id': self.mineral_2.id
        }))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'minerals/mineral_detail.html')


class TemplateTagsTests(TestCase):

    def test_field_or_na_no_field(self):
        # Should return N/A for an empty field
        result = mineral_extras.field_or_na(None)
        self.assertEqual(result, 'N/A')

    def test_field_or_na_valid_field(self):
        # Should return the field if its present
        result = mineral_extras.field_or_na(test_mineral_1.get('name'))
        self.assertEqual(result, test_mineral_1.get('name'))

    def test_random_mineral_id(self):
        # used in the random mineral URL
        result = mineral_extras.random_mineral_id()
        self.assertIsInstance(result, int)
