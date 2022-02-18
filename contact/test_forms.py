# Testing code adapted from Code Institute BoutiqueAdo project
from django.test import TestCase
from .forms import ContactForm


class TestContactForm(TestCase):
    """ Tests for contact forms """

    def test_first_name_is_required(self):
        form = ContactForm({'first_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors.keys())
        self.assertEqual(
                         form.errors['first_name'][0],
                         'This field is required.'
        )

    def test_last_name_is_required(self):
        form = ContactForm({'last_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('last_name', form.errors.keys())
        self.assertEqual(
                         form.errors['last_name'][0],
                         'This field is required.'
        )

    def test_email_is_required(self):
        form = ContactForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')

    def test_subject_is_required(self):
        form = ContactForm({'subject': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('subject', form.errors.keys())
        self.assertEqual(form.errors['subject'][0], 'This field is required.')

    def test_message_is_required(self):
        form = ContactForm({'message': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('message', form.errors.keys())
        self.assertEqual(form.errors['message'][0], 'This field is required.')
