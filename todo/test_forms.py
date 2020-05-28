from django.test import TestCase
from .forms import ItemForm

# Create your tests here.


class TestItemForm(TestCase):
    def test_item_name_is_required(self):
        # Checking error when field is emty
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_field_is_not_required(self):
        # Checking that everything is right when field has an entry
        form = ItemForm({'name': 'Test Todo Item'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        # checking the different fields
        form = ItemForm()
        self.assertEqual(form.Meta.fields, {'name', 'done'})
