from django.core.exceptions import ValidationError
from django.test import TestCase
from eventex.core.models import Speaker, Contact


class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name="Ricardo",
            slug="ricardo",
            photo='https://yt3.ggpht.com/-X29yPlgJe9g/AAAAAAAAAAI/AAAAAAAAAAA/8nl_Feaiaag/s100-c-k-no-mo-rj-c0xffffff/photo.jpg'
        )


    def test_email(self):
        contact = Contact.objects.create(speaker=self.speaker, kind=Contact.EMAIL, value='ricardo@gmail.com')
        self.assertTrue(Contact.objects.exists())


    def test_phone(self):
        contact = Contact.objects.create(speaker=self.speaker, kind=Contact.PHONE, value='123')
        self.assertTrue(Contact.objects.exists())


    def test_choices(self):
        '''Contact kind should be limited to E or P'''
        contact = Contact(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)


    def test_str(self):
        contact = Contact(speaker=self.speaker, kind=Contact.PHONE, value='ricardo@gmail.com')
        self.assertEqual('ricardo@gmail.com', str(contact))